#!/bin/bash

# Remove the pytest cache, assets, __pycache__, and report.html
rm -rf .pytest_cache
rm -rf assets
rm -rf tests/__pycache__
rm -f report.html

echo "Pre-execution cleanup complete."