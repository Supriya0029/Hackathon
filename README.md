# Quantum Engine Module

## Overview

This module implements the quantum simulation component required for the SIH project.

The module provides:

- Qubit simulation
- Superposition
- Bell State creation
- Entanglement
- Quantum Teleportation
- Pauli Operations
- Measurement
- Measurement Statistics

This module is independent and can be integrated with the Detection Engine and Attack Engine later.

---

## Technologies Used

- Python 3.x
- Qiskit
- Qiskit Aer Simulator
- NumPy

---

## Folder Structure

MEMBER_2_QUANTUM/

├── quantum_engine.py

├── requirements.txt

├── README.md

└── sample_output/

    └── sample_result.txt

---

## Installation

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run

```bash
python quantum_engine.py
```

---

## Functions

### create_bell_state()

Creates an entangled Bell state using:

- Hadamard Gate
- CNOT Gate

Returns:

```python
{
    "operation": "Bell State",
    "counts": {...}
}
```

---

### create_superposition()

Creates a qubit in superposition using a Hadamard gate.

Returns measurement statistics.

---

### apply_pauli_x()

Applies Pauli-X gate.

Equivalent to a quantum NOT operation.

---

### apply_pauli_z()

Applies Pauli-Z gate.

Changes phase of the qubit.

---

### quantum_teleportation()

Simulates:

1. State Preparation
2. Bell Pair Creation
3. Entanglement
4. Bell-State Measurement
5. Pauli Correction
6. State Recovery

Returns measurement counts.

---

## Input

No external input required.

The simulator internally creates quantum states.

---

## Output

Python dictionaries containing:

- Operation name
- Measurement counts
- Statistics

Example:

```python
{
    "operation": "Bell State",
    "counts": {
        "00": 512,
        "11": 512
    }
}
```

---

## Dependencies

- qiskit
- qiskit-aer
- numpy

---

## Limitations

- Uses a simulator, not real quantum hardware.
- Intended for educational and prototype purposes.
- Does not implement advanced quantum algorithms.
- No graphical interface included.

---

## Future Integration

Can be integrated with:

- Attack Engine
- Detection Engine
- Dashboard/UI Module

for full SIH system demonstration.
