# Calculator

A tiny Python calculator library with a CLI.

## Features
- Basic arithmetic: addition, subtraction, multiplication, division
- Safe expression evaluation with parentheses and exponent support
- Command line interface via the Python -m calculator entry point

## Usage

Importing in Python:

```python
from calculator import evaluate
print(evaluate("2 + 3 * 4"))  # 14.0
```

Command line:

```sh
python -m calculator "2 + (3 * 4) / 2"  # 7.0
```

You can also call other helpers:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)

## Design notes
- The evaluate function parses arithmetic expressions safely using Python's ast module, avoiding arbitrary code execution.
- Only numbers and arithmetic operators are allowed.

"""Calculator library with a minimal CLI for quick calculations."""
