import logging
import secrets

import pandas as pd

from src.model.model import model


def process_csv(input_csv: str) -> str:
    logging.info(f"Got CSV file: {input_csv}")

    try:
        data = pd.read_csv(input_csv)
        features = data.drop(["search_id"], axis=1)

        predictions = model.predict(features)

        result_df = pd.DataFrame(
            {"search_id": data["search_id"], "target": predictions}
        )

        # Generate a file name for temporary Gradio file storage
        output_csv = f"result_{secrets.token_hex(4)}.csv"
        result_df.to_csv(output_csv, index=False)

    except Exception as e:
        logging.error(str(e))
        raise e

    logging.info(f"Predicted successfully on {input_csv}")

    return output_csv, result_df
