# 🧠 Model Context Protocol Inspector (Local Dev with `uv`)

This project is a local development environment for running and inspecting the **Model Context Protocol (MCP)** using [`uv`](https://github.com/astral-sh/uv), a fast, modern Python package manager.

## 🚀 Quick Start

### 1. Initialize the Project

Start by initializing a new Python project using `uv`:

```bash
uv init <project_name>
cd <project_name>
```

This sets up a pyproject.toml with Poetry-style project metadata and creates a basic structure.

### 2. Create a Virtual Environment

Create and activate a virtual environment:

#### In Windows:
To create:
```bash
python -m venv <virtual env name>
```

To activate:
```bash
.venv\Scripts\activate
```

#### In Mac Os:

To create:
```bash
python -m venv <virtual env name>
```

To activate:

```bash
source .venv/bin/activate
```

### 3. Install Required Dependencies
Install your required libraries (e.g., for MCP and inspector logic). You can do this using:

```bash
pip install -r requirements.txt
```

### 4. Run the MCP Inspector
Once everything is set up, you can run the Model Context Protocol Inspector with:

```bash
uv run mcp dev main.py
```
This runs the main.py entry point within the MCP dev environment using uv's isolated runner.

🗂️ Project Structure (Example)
```text
mcp-server-app/
├── app/
│   ├── __init__.py
│   ├── main.py              # Entry point to run the MCP inspector
│   └── tools/               # Utility modules for protocol logic
│       ├── __init__.py
│       └── temperature.py   # Example utility module
├── requirements.txt         # (Optional) dependency list
├── pyproject.toml           # Project configuration and metadata
└── README.md
```

### UI Example
![mcp-server-app-ui](https://raw.githubusercontent.com/vishnuvardhanreddy-vvr/mcp-server-app/refs/heads/main/mcp-server-app-ui.png)

### 🛠 Development Tips

Add dev tools to pyproject.toml or install with uv pip install as needed.

### 📄 License
MIT License — see LICENSE for full details.
