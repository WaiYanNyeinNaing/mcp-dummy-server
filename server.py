#!/usr/bin/env python3

from fastmcp import FastMCP

# Create MCP server
mcp = FastMCP("MCP Dummy Server")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run() 