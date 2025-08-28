#!/usr/bin/env -S uv run --script

# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "polars",
# ]
# ///

import polars as pl

print(f"Hello polars version {pl.__version__}")

