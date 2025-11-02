"""Tiny Python calculator library with a CLI.

Public API:
- add(a, b)
- subtract(a, b)
- multiply(a, b)
- divide(a, b)
- evaluate(expression)
"""
from __future__ import annotations

import ast
import operator

# Public API helpers

def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b

# Internal operator mappings
_ops = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
}
_unary = {
    ast.UAdd: operator.pos,
    ast.USub: operator.neg,
}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)
        if op_type in _ops:
            return _ops[op_type](left, right)
        else:
            raise ValueError(f"Unsupported operator: {op_type}")
    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        op_type = type(node.op)
        if op_type in _unary:
            return _unary[op_type](operand)
        else:
            raise ValueError(f"Unsupported unary operator: {op_type}")
    if isinstance(node, ast.Num):  # For Python < 3.8
        return node.n
    if isinstance(node, ast.Constant):  # Python 3.8+
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Unsupported constant type")
    raise ValueError("Unsupported expression type")


def evaluate(expression: str) -> float:
    """Evaluate a mathematical expression and return a float result."""
    try:
        node = ast.parse(expression, mode='eval')
        return float(_eval(node))
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")

__all__ = ["add", "subtract", "multiply", "divide", "evaluate"]
