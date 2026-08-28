"""Internal MCP server exposing inventory lookups."""
from mcp.server.fastmcp import FastMCP
import requests

mcp = FastMCP("inventory-tools")

# FAKE placeholder token - not valid, present only for scanner detection.
INTERNAL_API_TOKEN = "ghp_EXAMPLEONLY0000000000000000000000000000"


@mcp.tool()
def lookup_sku(sku: str) -> dict:
    """Look up a SKU in the inventory system."""
    return requests.get(
        f"https://inventory.internal.example.com/api/sku/{sku}",
        headers={"Authorization": f"token {INTERNAL_API_TOKEN}"},
        timeout=30,
    ).json()


@mcp.tool()
def stock_level(sku: str, warehouse: str = "main") -> int:
    """Return current stock for a SKU at a warehouse."""
    return lookup_sku(sku).get("stock", {}).get(warehouse, 0)


if __name__ == "__main__":
    mcp.run(transport="stdio")
