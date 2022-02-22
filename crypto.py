import candlestick
import pandas as pd
from enums.timeframes import Timeframes
import logging
import os


class Crypto:
    """ The crypto class is used to store all data for a specific crypto.
    """

    def __init__(self, symbol: str) -> None:
        """
        Create Crypto object

            Parameters:
                symbol: The symbol of the crypto
        """
        self.symbol = symbol.upper()

        # Create data dictionary
        self.data = {i: [] for i in Timeframes}

    def get_OHLCV(self, time: Timeframes, data_path: str) -> pd.DataFrame:
        """
        Get OHLCV for a specific timeframe

            Parameters:
                time: The timeframe to get the data for
                data_path: The path to the data
        """
        logging.info(f"getting data for {self.symbol} at path {data_path}")

        path = f"{data_path}/{time.value}/{self.symbol}_{time.name}.csv"

        # Check if data path exists
        if os.path.exists(path):
            df = pd.read_csv(path)
            self.data[time] = df

            # Flip the dataframe so that the oldest data is on top
            df.iloc[::-1]
            return df

        # No data found, return empty dataframe
        else:
            logging.warning("No data for {}".format(self.symbol))
            logging.info("Returning empty dataframe")
            return pd.DataFrame()
