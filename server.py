#!/usr/bin/env python3
"""
FastMCP Dummy Server

A minimal but professional example of a FastMCP server for learning and demonstration.
Supports both STDIO and HTTP transports via command line arguments.
"""

import argparse
import logging
import sys
from typing import Optional

from fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Server configuration
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8000
DEFAULT_TRANSPORT = "stdio"

# Create FastMCP server instance
mcp = FastMCP("MCP Dummy Server")


@mcp.tool
def add(a: int, b: int) -> int:
    """
    Add two numbers together.
    
    Args:
        a: First number to add
        b: Second number to add
    
    Returns:
        The sum of a and b
    
    Example:
        add(2, 3) -> 5
    """
    logger.info(f"Adding {a} + {b}")
    result = a + b
    logger.info(f"Result: {result}")
    return result


@mcp.tool
def multiply(a: float, b: float) -> float:
    """
    Multiply two numbers together.
    
    Args:
        a: First number to multiply
        b: Second number to multiply
    
    Returns:
        The product of a and b
    
    Example:
        multiply(4, 5) -> 20.0
    """
    logger.info(f"Multiplying {a} * {b}")
    result = a * b
    logger.info(f"Result: {result}")
    return result


def parse_arguments() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(
        description="FastMCP Dummy Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s                           # Run with STDIO transport (default)
  %(prog)s --transport http          # Run with HTTP transport
  %(prog)s --transport http --port 9000  # Run HTTP on port 9000
  %(prog)s --host 0.0.0.0 --port 8080    # Run HTTP on all interfaces
        """
    )
    
    parser.add_argument(
        "--transport", "-t",
        choices=["stdio", "http"],
        default=DEFAULT_TRANSPORT,
        help="Transport protocol to use (default: %(default)s)"
    )
    
    parser.add_argument(
        "--host",
        default=DEFAULT_HOST,
        help="Host to bind to for HTTP transport (default: %(default)s)"
    )
    
    parser.add_argument(
        "--port", "-p",
        type=int,
        default=DEFAULT_PORT,
        help="Port to bind to for HTTP transport (default: %(default)s)"
    )
    
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose logging"
    )
    
    return parser.parse_args()


def main() -> int:
    """Main entry point."""
    try:
        args = parse_arguments()
        
        # Configure logging level
        if args.verbose:
            logging.getLogger().setLevel(logging.DEBUG)
            logger.debug("Verbose logging enabled")
        
        # Log server configuration
        logger.info(f"Starting MCP Dummy Server with {args.transport} transport")
        
        if args.transport == "http":
            logger.info(f"HTTP server will be available at: http://{args.host}:{args.port}/mcp")
            mcp.run(
                transport="streamable-http",
                host=args.host,
                port=args.port
            )
        else:
            logger.info("Using STDIO transport")
            mcp.run(transport="stdio")
            
    except KeyboardInterrupt:
        logger.info("Server shutdown requested")
        return 0
    except Exception as e:
        logger.error(f"Server error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main()) 