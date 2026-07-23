#!/bin/bash
# Double-click to start the CountingPhotons lectures in JupyterLab.
# Works fully offline - everything needed is in this folder.

cd "$(dirname "$0")"

if [ ! -d .venv ]; then
    echo "ERROR: the .venv environment is missing."
    echo "One-time setup (needs internet):"
    echo "  python3.12 -m venv .venv"
    echo "  .venv/bin/pip install -r requirements/requirements.txt"
    read -r -p "Press enter to close."
    exit 1
fi

echo "Starting JupyterLab (close this window or press Ctrl+C to stop)..."
exec .venv/bin/jupyter lab lectures/
