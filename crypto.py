import candlestick
import pandas as pd
from enums.timeframes import Timeframes
import logging
import os


class Crypto:
    def __init__(self, symbol: str) -> None:
        self.symbol = symbol.upper()
        self.data = {i: [] for i in Timeframes}
        self.data["raw"] = pd.DataFrame()

    def get_data(self, time: Timeframes, data_path: str) -> pd.DataFrame:

        logging.info(f"getting data for {self.symbol} at path {data_path}")

        path = f"{data_path}/{time.value}/{self.symbol}_{time.name}.csv"

        if os.path.exists(path):
            df = pd.read_csv(path)
            self.data[time] = df
            df.iloc[::-1]
            return df

        else:
            logging.warning("No data for {}".format(self.symbol))
            logging.info("Returning empty dataframe")
            return pd.DataFrame()
