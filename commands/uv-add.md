---
description: "Add dependencies to the uv project"
---

# Add Dependencies with uv

Add Python packages to the project using uv.

## Instructions

1. Parse the user's arguments: $ARGUMENTS
2. Determine if these are regular dependencies or dev dependencies:
   - If arguments contain `--dev` or `-d`, use `uv add --dev <packages>`
   - Otherwise, use `uv add <packages>`
3. Run the appropriate uv add command
4. After adding, show the updated dependencies section from pyproject.toml
5. If errors occur (package not found, version conflicts), explain the issue and suggest alternatives

## Common usage patterns

- Regular dependency: `/uv-add requests`
- Multiple packages: `/uv-add requests httpx pydantic`
- Dev dependency: `/uv-add --dev pytest ruff`
- Specific version: `/uv-add "requests>=2.28"`

User arguments: $ARGUMENTS
