# idr-sandbox

Scripts and notebooks for exploring the Image Data Resource.

## Environment setup

### Prerequisites

- [Python 3.10](https://www.python.org/downloads/)
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

`zeroc-ice` (required by `omero-py`) is installed from pre-built GitHub wheels. Platform-specific URLs are configured in `pyproject.toml`, so `uv sync` picks the right wheel for macOS, Linux, or Windows automatically.

### Install dependencies

From the project root:

```bash
uv sync --python 3.10
```

This creates a virtual environment (`.venv`) with Python 3.10 and installs all dependencies from `pyproject.toml` and `uv.lock`. If you don't have Python 3.10 installed, uv can download it automatically.

Other ways to specify the interpreter:

```bash
uv sync -p 3.10.18                    # exact patch version
uv sync -p python3.10                 # executable name on PATH
uv sync -p /usr/local/bin/python3.10  # full path
UV_PYTHON=3.10 uv sync                # via environment variable
```

If your default Python is already 3.10.x, plain `uv sync` is enough.

### Verify the setup

Run the connection test against the IDR public API:

```bash
uv run test_connection.py
```

You should see output like:

```
Success! Data Available: dict_keys([...])
image name: starvation p1 [Well 330, Field 1 (Spot 988)]
```

If the script prints `Failed with status code ...`, check your network connection and try again.
