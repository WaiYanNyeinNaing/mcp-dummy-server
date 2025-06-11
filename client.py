#!/usr/bin/env python3
"""
FastMCP Dummy Client

A client for testing and demonstrating the FastMCP Dummy Server.
Supports both STDIO and HTTP connections via command line arguments.
"""

import argparse
import asyncio
import logging
import sys
from typing import Any, Dict, List

from fastmcp import Client

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Default configuration
DEFAULT_SERVER_PATH = "server.py"
DEFAULT_HTTP_URL = "http://127.0.0.1:8000/mcp"


async def list_tools(client: Client) -> List[Any]:
    """List all available tools on the server."""
    try:
        tools = await client.list_tools()
        logger.info(f"Found {len(tools)} tools:")
        for tool in tools:
            logger.info(f"  - {tool.name}: {tool.description}")
        return tools
    except Exception as e:
        logger.error(f"Failed to list tools: {e}")
        return []


async def test_add_tool(client: Client, a: int = 2, b: int = 3) -> None:
    """Test the add tool with given parameters."""
    try:
        logger.info(f"Calling add tool with a={a}, b={b}")
        result = await client.call_tool("add", {"a": a, "b": b})
        if result:
            answer = result[0].text
            logger.info(f"Result: {answer}")
            print(f"add({a}, {b}) = {answer}")
        else:
            logger.warning("No result returned from add tool")
    except Exception as e:
        logger.error(f"Failed to call add tool: {e}")


async def test_multiply_tool(client: Client, a: float = 4.0, b: float = 5.0) -> None:
    """Test the multiply tool with given parameters."""
    try:
        logger.info(f"Calling multiply tool with a={a}, b={b}")
        result = await client.call_tool("multiply", {"a": a, "b": b})
        if result:
            answer = result[0].text
            logger.info(f"Result: {answer}")
            print(f"multiply({a}, {b}) = {answer}")
        else:
            logger.warning("No result returned from multiply tool")
    except Exception as e:
        logger.error(f"Failed to call multiply tool: {e}")


async def run_interactive_mode(client: Client) -> None:
    """Run in interactive mode for manual testing."""
    print("\nInteractive Mode - Type commands or 'quit' to exit:")
    print("Available commands:")
    print("  add <a> <b>      - Add two numbers")
    print("  multiply <a> <b> - Multiply two numbers")
    print("  list             - List available tools")
    print("  quit             - Exit interactive mode")
    
    while True:
        try:
            cmd = input("\n> ").strip().split()
            if not cmd:
                continue
                
            if cmd[0] == "quit":
                break
            elif cmd[0] == "list":
                await list_tools(client)
            elif cmd[0] == "add" and len(cmd) == 3:
                a, b = int(cmd[1]), int(cmd[2])
                await test_add_tool(client, a, b)
            elif cmd[0] == "multiply" and len(cmd) == 3:
                a, b = float(cmd[1]), float(cmd[2])
                await test_multiply_tool(client, a, b)
            else:
                print("Invalid command. Type 'quit' to exit.")
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Invalid numbers provided.")
        except Exception as e:
            logger.error(f"Command error: {e}")


async def main(args: argparse.Namespace) -> int:
    """Main client logic."""
    try:
        # Determine connection method
        if args.mode == "http":
            connection = args.url
            logger.info(f"Connecting to HTTP server at: {connection}")
        else:
            connection = args.server_path
            logger.info(f"Connecting to server script: {connection}")
        
        # Create and connect client
        client = Client(connection)
        
        async with client:
            logger.info("Connected to server")
            
            # List available tools
            await list_tools(client)
            
            if args.interactive:
                await run_interactive_mode(client)
            else:
                # Run default tests
                await test_add_tool(client, args.add_a, args.add_b)
                await test_multiply_tool(client, args.multiply_a, args.multiply_b)
        
        logger.info("Client session completed")
        return 0
        
    except Exception as e:
        logger.error(f"Client error: {e}")
        return 1


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="FastMCP Dummy Client",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                                    # Connect to server.py via STDIO
  %(prog)s --mode http                        # Connect to HTTP server
  %(prog)s --mode http --url http://localhost:9000/mcp  # Custom HTTP URL
  %(prog)s --add-a 10 --add-b 20              # Test add with custom values
  %(prog)s --interactive                      # Run in interactive mode
        """
    )
    
    parser.add_argument(
        "--mode", "-m",
        choices=["stdio", "http"],
        default="stdio",
        help="Connection mode (default: %(default)s)"
    )
    
    parser.add_argument(
        "--server-path",
        default=DEFAULT_SERVER_PATH,
        help="Path to server script for STDIO mode (default: %(default)s)"
    )
    
    parser.add_argument(
        "--url",
        default=DEFAULT_HTTP_URL,
        help="URL for HTTP mode (default: %(default)s)"
    )
    
    parser.add_argument(
        "--add-a",
        type=int,
        default=2,
        help="First number for add test (default: %(default)s)"
    )
    
    parser.add_argument(
        "--add-b",
        type=int,
        default=3,
        help="Second number for add test (default: %(default)s)"
    )
    
    parser.add_argument(
        "--multiply-a",
        type=float,
        default=4.0,
        help="First number for multiply test (default: %(default)s)"
    )
    
    parser.add_argument(
        "--multiply-b",
        type=float,
        default=5.0,
        help="Second number for multiply test (default: %(default)s)"
    )
    
    parser.add_argument(
        "--interactive", "-i",
        action="store_true",
        help="Run in interactive mode"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_arguments()
    
    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)
    
    sys.exit(asyncio.run(main(args))) 