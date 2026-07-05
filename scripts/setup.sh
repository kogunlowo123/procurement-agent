#!/bin/bash
set -euo pipefail
echo "Setting up Procurement Agent..."
pip install -e ".[dev]"
echo "Setup complete!"
