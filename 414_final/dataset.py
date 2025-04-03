from pathlib import Path

from loguru import logger
from tqdm import tqdm
import typer

from 414_final.config import PROCESSED_DATA_DIR, RAW_DATA_DIR

app = typer.Typer()


@app.command()
def main(
    # ---- REPLACE DEFAULT PATHS AS APPROPRIATE ----
    input_path: Path = /Users/brynnsaffer/Documents/414_final_project/ "GSS_414_Raw.csv",
    output_path: Path = /Users/brynnsaffer/Documents/414_final_project/ "Cleaned_Data.csv",
    # ----------------------------------------------
):
    # ---- REPLACE THIS WITH YOUR OWN CODE ----
    logger.info("Processing dataset...")
    for i in tqdm(range(10), total=10):
        if i == 5:
            logger.info("Something happened for iteration 5.")
    logger.success("Processing dataset complete.")
    # -----------------------------------------


if __name__ == "__main__":
    app()
