#!/usr/bin/env python3

import asyncio
from fastmcp import Client

async def test_server():
    """Test the MCP dummy server"""
    async with Client("./server.py") as client:
        # Test add tool
        result = await client.call_tool("add", {"a": 5, "b": 3})
        print(f"5 + 3 = {result.text}")
        
        # Test multiply tool
        result = await client.call_tool("multiply", {"a": 4, "b": 7})
        print(f"4 × 7 = {result.text}")

if __name__ == "__main__":
    asyncio.run(test_server()) 