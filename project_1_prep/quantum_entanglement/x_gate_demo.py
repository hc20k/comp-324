from qiskit import QuantumCircuit, transpile
from qiskit_aer import Aer

qc = QuantumCircuit(1)
qc.x(0)

simulator = Aer.get_backend("statevector_simulator")
compiled_circuit = transpile(qc, simulator)
result = simulator.run(compiled_circuit).result()

statevector = result.get_statevector()
print(statevector)

"""
Output:

Statevector([0.+0.j, 1.+0.j],
            dims=(2,))
"""