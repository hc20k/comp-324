from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

qc = QuantumCircuit(1, 1)

qc.h(0) # hadamard gate
qc.measure(0, 0)

simulator = Aer.get_backend("qasm_simulator")
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit, shots=1000).result()

counts = result.get_counts(qc)
print("Measurement counts:", counts)

plot_histogram(counts)
plt.savefig("quantum_superposition.png")