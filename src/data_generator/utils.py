"""
Utility functions for dataset generation.
"""

from pathlib import Path
import random

import numpy as np
import pandas as pd


def create_directory(directory: Path) -> None:
    directory.mkdir(parents=True, exist_ok=True)


def set_random_seed(seed: int) -> None:

    random.seed(seed)
    np.random.seed(seed)


def save_dataframe(df: pd.DataFrame, output_path: Path) -> None:
    """
    Save DataFrame as a Parquet file.
    """
    create_directory(output_path.parent)
    df.to_parquet(output_path, index=False)