from math import gcd
from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
from qiskit.circuit.library import QFT
from fractions import Fraction
import matplotlib.pyplot as plt

# ONLY WORKS FOR N=15 AND a=2

N = 15
a = 2

n_count = 4


def qpe_amod15(a):
    qc = QuantumCircuit(n_count + 4, n_count)
    for q in range(n_count):
        qc.h(q)
    qc.x(n_count)

    for q in range(n_count):
        qc.append(amod15(a, 2**q).control(),
                  [q] + [i + n_count for i in range(4)])
    qc.append(QFT(n_count, inverse=True, do_swaps=True), range(n_count))
    for q in range(n_count):
        qc.measure(q, q)
    return qc

def amod15(a, power):
    """Modular exponentiation gate for a^power mod 15."""
    U = QuantumCircuit(4)
    for _ in range(power):
        if a in [2, 7, 8, 13]:
            if a == 2:
                U.swap(0, 1)
                U.swap(1, 2)
                U.swap(2, 3)
            elif a == 7:
                U.swap(2, 3)
                U.swap(1, 2)
                U.swap(0, 1)
            elif a == 8:
                U.swap(1, 2)
                U.swap(2, 3)
                U.swap(0, 1)
            elif a == 13:
                U.swap(0, 1)
                U.swap(1, 2)
                U.swap(2, 3)
    return U.to_gate()

qc = qpe_amod15(a)
simulator = Aer.get_backend('qasm_simulator')
qc = transpile(qc, simulator)
result = simulator.run(qc, shots=1024).result()
counts = result.get_counts()

# Plot histogram
plot_histogram(counts)
plt.title("Shor's algorithm (N=15, a=2)")
plt.savefig("rsa_breaking_sim.png")

# get period
measured = max(counts, key=counts.get)
phase = int(measured, 2) / 2**n_count
print(f"Measured binary: {measured}, phase: {phase}")

frac = Fraction(phase).limit_denominator(N)
r = frac.denominator
print(f"period r: {r}")

if r % 2 == 0 and pow(a, r//2, N) != N-1:
    factor1 = gcd(pow(a, r//2) - 1, N)
    factor2 = gcd(pow(a, r//2) + 1, N)
    print(f"factors found: {factor1}, {factor2}")
else:
    print("factors not found")

"""
Explanation:
1. make sure N is 15, a is 2
2. build qpe circuit, run it on qasm simulator. output is saved as rsa_breaking_sim.png
3. using qpe, we get the period r
4. the period r is extracted from the most frequent measurement
5. if r is even, we can find the factors of N
"""
