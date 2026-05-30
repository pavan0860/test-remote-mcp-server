from fastmcp import FastMCP
import random
import json

mcp = FastMCP("Simple Calculator")

@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers.
    
    Args:
        a (int): The first number.
        b (int): The second number.

    Returns:
        int: The sum of the two numbers.
    """
    return a + b

@mcp.tool
def random_number(min_val: int, max_val: int) -> int:
    """Generate a random number between min_val and max_val.
    
    Args:
        min_val: Minimum value (default: 1).
        max_val: Maximum value (default: 100).

    Returns:
        int: A random number between min_val and max_val.
    """
    return random.randint(min_val, max_val)

@mcp.resource("info://server")
def server_info() -> str:
    """Get server information."""
    info = {
        "name": "Simple Calculator Server",
        "version": "1.0.0",
        "description": "A simple server that provides basic calculator functions.",
        "tools": ["add", "random_number"],
        "authors": ["Your Name"]
    }
    return json.dumps(info, indent=2)

if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)

