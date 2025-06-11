#!/usr/bin/env python3

import asyncio
from fastmcp import Client

async def test_server():
    """Test the MCP calculation server"""
    async with Client("./server.py") as client:
        # Test add tool with decimals
        result = await client.call_tool("add", {"a": 18.75, "b": 2.81})
        print(f"18.75 + 2.81 = {result[0].text}")
        
        # Test subtract tool
        result = await client.call_tool("subtract", {"a": 100, "b": 25.5})
        print(f"100 - 25.5 = {result[0].text}")
        
        # Test multiply tool
        result = await client.call_tool("multiply", {"a": 12.56, "b": 0.15})
        print(f"12.56 × 0.15 = {result[0].text}")
        
        # Test divide tool
        result = await client.call_tool("divide", {"a": 50, "b": 4})
        print(f"50 ÷ 4 = {result[0].text}")
        
        # Test percentage tool
        result = await client.call_tool("percentage", {"value": 18.75, "percent": 15})
        print(f"15% of 18.75 = {result[0].text}")

if __name__ == "__main__":
    asyncio.run(test_server()) 