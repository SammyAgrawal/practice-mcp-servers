from typing import Any
import httpx
from fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("weather")

@mcp.tool()
def add(a, b):
    """Adds two numbers"""
    return a + b

""" Local stdio server
if __name__ == "__main__":
    mcp.run()
"""

## http transport for remote server
if __name__ == "__main__":
    mcp.run(transport="http", port=8000)