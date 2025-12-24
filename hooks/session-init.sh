#!/bin/bash
# SessionStart hook for uv environment initialization
# This script runs at the start of each Claude Code session

set -e

# Output JSON for Claude Code hook system
output_json() {
    local status="$1"
    local message="$2"
    echo "{\"status\": \"$status\", \"message\": \"$message\"}"
}

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    output_json "warning" "uv is not installed. Install it with: curl -LsSf https://astral.sh/uv/install.sh | sh"
    exit 0
fi

# Get uv version
UV_VERSION=$(uv --version 2>/dev/null || echo "unknown")

# Check if we're in a uv project (has pyproject.toml)
if [ -f "pyproject.toml" ]; then
    # Check if uv.lock exists and is up to date
    if [ -f "uv.lock" ]; then
        # Try to verify lock file
        if uv lock --check &> /dev/null; then
            LOCK_STATUS="up to date"
        else
            LOCK_STATUS="needs update"
            # Auto-sync if lock is outdated
            uv sync --quiet 2>/dev/null || true
        fi
    else
        LOCK_STATUS="not found"
        # Create lock file and sync
        uv lock --quiet 2>/dev/null || true
        uv sync --quiet 2>/dev/null || true
    fi

    # Get Python version from the environment
    PYTHON_VERSION=$(uv run python --version 2>/dev/null || echo "not configured")

    output_json "success" "uv project detected. $UV_VERSION, Python: $PYTHON_VERSION, Lock: $LOCK_STATUS"
else
    output_json "info" "No pyproject.toml found. Use /uv-init to create a new project. $UV_VERSION available."
fi

exit 0
