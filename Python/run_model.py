"""Python Model Example"""

import os

import numpy as np
import pandas as pd
import typer
from typing_extensions import Annotated
from pathlib import Path

def predict() :
    """Sample prediction function.

    pass


def main(
    input_dir: Annotated[str, typer.Option()] = "/input",
    output_dir: Annotated[str, typer.Option()] = "/output",
):
    """
    Run inference using data in input_dir and output predictions to output_dir.
    """
    input_path = Path(input_dir)
    output_path = Path(output_dir)
    output_path.mkdir(parents=True, exist_ok=True)

    pass


if __name__ == "__main__":
    typer.run(main)
