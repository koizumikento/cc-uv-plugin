---
description: "Initialize a new uv Python project with pyproject.toml"
---

# uv Project Initialization

Initialize a new Python project using uv with the following steps:

1. First, check if pyproject.toml already exists in the current directory
2. If it doesn't exist, run `uv init` to create the project structure
3. If the user provided a project name as argument ($ARGUMENTS), use `uv init $ARGUMENTS`
4. After initialization, run `uv sync` to create the virtual environment
5. Show the contents of the generated pyproject.toml
6. Suggest next steps (adding dependencies, creating source files)

If pyproject.toml already exists, inform the user and ask if they want to proceed with `uv sync` instead.

User arguments: $ARGUMENTS
