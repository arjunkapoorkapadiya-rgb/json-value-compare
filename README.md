# json-value-compare

Compare JSON values with strict type checks and duplicate-key detection.

Maintained by @arjunkapoorkapadiya-rgb.

## Requirements

Python 3.9 or newer. No third-party packages required.

## Usage

    python main.py before.json after.json

## Behavior and limitations

Ignores object-key order and formatting. Array order matters. Integers and floating-point numbers are treated as different types, so 1 differs from 1.0. Rejects duplicate object keys and nonstandard NaN/Infinity constants. Loads both files into memory and uses Python numeric parsing. Exit codes: 0 equal, 1 different, 2 input error.