"""CLI for the calculator package"""
from __future__ import annotations

import argparse

from . import evaluate

VERSION = "0.1.0"


def main():
    parser = argparse.ArgumentParser(prog="calculator", description="Evaluate arithmetic expressions.")
    parser.add_argument("expression", nargs="?", help="Expression to evaluate, e.g., '2+3*4'")
    parser.add_argument("--version", action="store_true", help="Show version and exit")
    args = parser.parse_args()

    if args.version:
        print(f"calculator {VERSION}")
        return

    if not args.expression:
        parser.print_help()
        return

    try:
        result = evaluate(args.expression)
        print(result)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":  # pragma: no cover
    main()
