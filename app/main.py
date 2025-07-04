"""MCP Server for accessing Tools"""
from mcp.server.fastmcp import FastMCP
from tools.temperature import temperature

mcp = FastMCP(name="Local MCP Server")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiply two numbers"""
    return a * b

@mcp.tool()
def get_temperature(city: str):
    """get temperature of any city"""
    return temperature(city=city)


# mcp.run(transport="streamable-http")
