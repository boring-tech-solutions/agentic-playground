# Agentic Playground

A small collection of sample scripts and workflows for exploring agentic automation.

## Overview

This repository contains example scripts and configurations used to prototype agentic flows. It is intended for experimentation and learning.

## Requirements

- Python 3.10 (tested)
- pip or `uv` package manager
- (Optional) virtual environment (venv/virtualenv)

## Quickstart

1. Clone the repo and change into its directory.
2. Create and activate a virtual environment (recommended):

```bash
python3.10 -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1
```

## Install dependencies

Using `uv` package manager:

```bash
uv pip install -r requirements.txt
```

Using standard `pip`:

```bash
pip install -r requirements.txt
```

## Tooling

If you need the `crewai` tool, install it via `uv`:

```bash
uv tool install crewai
```

Verify installation:

```bash
uv tool list
```

Expected output (example):

```
crewai v0.102.0
    - crewai
```

## Run

Start the sample project:

```bash
crewai run
```

## Troubleshooting

- If a package fails to install, confirm your Python version and virtual environment are active.
- For `uv`-specific issues, consult the `uv` documentation or use `pip` as an alternative.

## Contributing

Contributions and issues are welcome. Please open a PR or issue describing changes or problems.

## License

See LICENSE for details.
