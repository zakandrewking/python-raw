## Run

This project serves a FastAPI backend and a minimal NiceGUI frontend.

### Prereqs
- Python 3.13+
- Dependencies are managed via `uv` (see `pyproject.toml` / `uv.lock`).

### Install

```bash
uv sync
```

### Start the app

```bash
uv run fastapi dev main.py
```

Then open:
- API root: `http://127.0.0.1:8000/`
- NiceGUI UI: `http://127.0.0.1:8000/`
- API root moved to: `http://127.0.0.1:8000/api`

### References
- NiceGUI documentation: https://nicegui.io/documentation

