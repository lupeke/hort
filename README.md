# ```hort```

A command-line tool to generate a Python API client from an OpenAPI (Swagger) specification.

## Installation

```bash
python3 -m venv .venv && \
source .venv/bin/activate && \
pip install .
```

## Usage

To generate a client, run the `hort` command with the path to your OpenAPI spec file.

```bash
hort <path-to-spec.json> --output-dir <path-to-output-dir>
```

**Example:**

```bash
hort swagger.json --output-dir my_tools
```

This will generate a `client.py` file in the `my_tools` directory.

## Development

To set up the development environment, create a virtual environment and install the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
pip install pytest pytest-httpx
```

### Running Tests

To run the test suite, use `pytest`:

```bash
pytest
```
