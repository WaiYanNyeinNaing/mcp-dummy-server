#!/usr/bin/env python3

from fastmcp import FastMCP
from typing import Union

# Create MCP server
mcp = FastMCP("MCP Calculation Server")

Number = Union[int, float]

@mcp.tool
def add(a: Number, b: Number) -> float:
    """Add two numbers"""
    return float(a + b)

@mcp.tool
def subtract(a: Number, b: Number) -> float:
    """Subtract second number from first number"""
    return float(a - b)

@mcp.tool
def multiply(a: Number, b: Number) -> float:
    """Multiply two numbers"""
    return float(a * b)

@mcp.tool
def divide(a: Number, b: Number) -> float:
    """Divide first number by second number"""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return float(a / b)

@mcp.tool
def power(a: Number, b: Number) -> float:
    """Raise first number to the power of second number"""
    return float(a ** b)

@mcp.tool
def percentage(value: Number, percent: Number) -> float:
    """Calculate percentage of a value (e.g., 15% of 100)"""
    return float(value * (percent / 100))

@mcp.tool
def percentage_increase(value: Number, percent: Number) -> float:
    """Calculate value with percentage increase (e.g., 100 + 15%)"""
    return float(value * (1 + percent / 100))

@mcp.tool
def percentage_decrease(value: Number, percent: Number) -> float:
    """Calculate value with percentage decrease (e.g., 100 - 15%)"""
    return float(value * (1 - percent / 100))

if __name__ == "__main__":
    mcp.run() 