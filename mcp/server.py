#!/usr/bin/env python3
"""
MCP Server for uv Python package manager integration.

This server provides tools for Claude Code to interact with uv,
enabling Python development workflows directly through the assistant.
"""

import asyncio
import os
import subprocess
from typing import Any

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import (
    Tool,
    TextContent,
    CallToolResult,
)

# Create the MCP server instance
server = Server("uv-tools")

# Store workspace directory from initialization
_workspace_dir: str | None = None


def get_workspace_cwd(arguments: dict[str, Any]) -> str:
    """Get the working directory, requiring explicit cwd for project operations."""
    cwd = arguments.get("cwd")
    if cwd:
        return cwd
    # Fall back to workspace if set during initialization
    if _workspace_dir:
        return _workspace_dir
    # Last resort: use PWD from environment (set by Claude Code)
    return os.environ.get("PWD", os.getcwd())


def run_uv_command(args: list[str], cwd: str | None = None) -> dict[str, Any]:
    """Execute a uv command and return the result."""
    try:
        result = subprocess.run(
            ["uv"] + args,
            capture_output=True,
            text=True,
            cwd=cwd,
            timeout=300,  # 5 minute timeout
        )
        return {
            "success": result.returncode == 0,
            "stdout": result.stdout,
            "stderr": result.stderr,
            "returncode": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "stdout": "",
            "stderr": "Command timed out after 5 minutes",
            "returncode": -1,
        }
    except FileNotFoundError:
        return {
            "success": False,
            "stdout": "",
            "stderr": "uv is not installed. Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh",
            "returncode": -1,
        }
    except Exception as e:
        return {
            "success": False,
            "stdout": "",
            "stderr": str(e),
            "returncode": -1,
        }


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List all available uv tools."""
    return [
        Tool(
            name="uv_init",
            description="Initialize a new Python project with uv. Creates pyproject.toml and sets up the project structure. IMPORTANT: Always specify cwd to target the user's workspace.",
            inputSchema={
                "type": "object",
                "properties": {
                    "name": {
                        "type": "string",
                        "description": "Project name (optional, uses directory name if not specified)",
                    },
                    "python": {
                        "type": "string",
                        "description": "Python version to use (e.g., '3.11', '3.12')",
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory (user's project path). Required to avoid operating on wrong directory.",
                    },
                },
                "required": ["cwd"],
            },
        ),
        Tool(
            name="uv_add",
            description="Add dependencies to the project. Supports regular and development dependencies. IMPORTANT: Always specify cwd.",
            inputSchema={
                "type": "object",
                "properties": {
                    "packages": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of packages to add (e.g., ['requests', 'httpx>=0.25'])",
                    },
                    "dev": {
                        "type": "boolean",
                        "description": "Add as development dependency",
                        "default": False,
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory (user's project path). Required.",
                    },
                },
                "required": ["packages", "cwd"],
            },
        ),
        Tool(
            name="uv_remove",
            description="Remove dependencies from the project. IMPORTANT: Always specify cwd.",
            inputSchema={
                "type": "object",
                "properties": {
                    "packages": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of packages to remove",
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory (user's project path). Required.",
                    },
                },
                "required": ["packages", "cwd"],
            },
        ),
        Tool(
            name="uv_sync",
            description="Sync the project environment with dependencies defined in pyproject.toml. IMPORTANT: Always specify cwd.",
            inputSchema={
                "type": "object",
                "properties": {
                    "frozen": {
                        "type": "boolean",
                        "description": "Sync without updating the lock file",
                        "default": False,
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory (user's project path). Required.",
                    },
                },
                "required": ["cwd"],
            },
        ),
        Tool(
            name="uv_run",
            description="Run a command in the project environment. IMPORTANT: Always specify cwd.",
            inputSchema={
                "type": "object",
                "properties": {
                    "command": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "Command and arguments to run (e.g., ['python', 'main.py'] or ['pytest', '-v'])",
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory (user's project path). Required.",
                    },
                },
                "required": ["command", "cwd"],
            },
        ),
        Tool(
            name="uv_pip_list",
            description="List installed packages in the project environment. IMPORTANT: Always specify cwd.",
            inputSchema={
                "type": "object",
                "properties": {
                    "format": {
                        "type": "string",
                        "enum": ["columns", "json"],
                        "description": "Output format",
                        "default": "columns",
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory (user's project path). Required.",
                    },
                },
                "required": ["cwd"],
            },
        ),
        Tool(
            name="uv_lock",
            description="Generate or update the lock file (uv.lock). IMPORTANT: Always specify cwd.",
            inputSchema={
                "type": "object",
                "properties": {
                    "check": {
                        "type": "boolean",
                        "description": "Check if lock file is up to date without modifying it",
                        "default": False,
                    },
                    "cwd": {
                        "type": "string",
                        "description": "Working directory (user's project path). Required.",
                    },
                },
                "required": ["cwd"],
            },
        ),
        Tool(
            name="uv_python_install",
            description="Install a specific Python version.",
            inputSchema={
                "type": "object",
                "properties": {
                    "version": {
                        "type": "string",
                        "description": "Python version to install (e.g., '3.11', '3.12.1')",
                    },
                },
                "required": ["version"],
            },
        ),
        Tool(
            name="uv_python_list",
            description="List available and installed Python versions.",
            inputSchema={
                "type": "object",
                "properties": {
                    "installed_only": {
                        "type": "boolean",
                        "description": "Only show installed versions",
                        "default": False,
                    },
                },
            },
        ),
        Tool(
            name="uv_version",
            description="Get the installed uv version.",
            inputSchema={
                "type": "object",
                "properties": {},
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict[str, Any]) -> CallToolResult:
    """Handle tool calls."""
    # Get workspace directory - never default to plugin directory
    cwd = get_workspace_cwd(arguments)

    if name == "uv_init":
        args = ["init"]
        if arguments.get("name"):
            args.append(arguments["name"])
        if arguments.get("python"):
            args.extend(["--python", arguments["python"]])
        result = run_uv_command(args, cwd)

    elif name == "uv_add":
        args = ["add"]
        if arguments.get("dev"):
            args.append("--dev")
        args.extend(arguments["packages"])
        result = run_uv_command(args, cwd)

    elif name == "uv_remove":
        args = ["remove"] + arguments["packages"]
        result = run_uv_command(args, cwd)

    elif name == "uv_sync":
        args = ["sync"]
        if arguments.get("frozen"):
            args.append("--frozen")
        result = run_uv_command(args, cwd)

    elif name == "uv_run":
        args = ["run"] + arguments["command"]
        result = run_uv_command(args, cwd)

    elif name == "uv_pip_list":
        args = ["pip", "list"]
        if arguments.get("format") == "json":
            args.append("--format=json")
        result = run_uv_command(args, cwd)

    elif name == "uv_lock":
        args = ["lock"]
        if arguments.get("check"):
            args.append("--check")
        result = run_uv_command(args, cwd)

    elif name == "uv_python_install":
        args = ["python", "install", arguments["version"]]
        result = run_uv_command(args, cwd)

    elif name == "uv_python_list":
        args = ["python", "list"]
        if arguments.get("installed_only"):
            args.append("--only-installed")
        result = run_uv_command(args, cwd)

    elif name == "uv_version":
        args = ["--version"]
        result = run_uv_command(args, cwd)

    else:
        return CallToolResult(
            content=[TextContent(type="text", text=f"Unknown tool: {name}")]
        )

    # Format the response
    output_parts = []
    if result["stdout"]:
        output_parts.append(f"Output:\n{result['stdout']}")
    if result["stderr"]:
        output_parts.append(f"Errors:\n{result['stderr']}")
    if not output_parts:
        output_parts.append("Command completed with no output.")

    status = "Success" if result["success"] else "Failed"
    response = f"[{status}]\n" + "\n".join(output_parts)

    return CallToolResult(content=[TextContent(type="text", text=response)])


async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(read_stream, write_stream, server.create_initialization_options())


if __name__ == "__main__":
    asyncio.run(main())
