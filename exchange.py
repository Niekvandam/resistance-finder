from sqlite3 import TimeFromTicks
import pandas as pd
from crypto import Crypto
import sys
import os
from enums.timeframes import Timeframes
import logging


DATA_LOC = "data/"


class Exchange:
    """ The exchange class is the parent class for all exchanges.
    It contains a dictionary for all currencies and the data path for the exchange.
    """

    def __init__(self, name, cryptos: list = None):
        """
        Create Exchange object

            Parameters:
                name: The name of the exchange
                cryptos: A list of Crypto objects to add to the exchange
        """
        self.name = name.lower()

        # Currencies dictionary used to store all currencies and their respective data
        self.currencies = {}

        # Set data path for exchange
        self.data_path = f"{DATA_LOC}{self.name}/"

    def add_crypto(self, crypto: Crypto):
        """
        Add crypto to the crypto dictionary

            Parameters:
                crypto: The crypto object to add
        """
        logging.info(f"Crypto {crypto.symbol} added to {self.name}")
        self.currencies[crypto.symbol] = crypto

    def get_data(self, symbol: str, fiat: str, time: Timeframes):
        """
        Get data for a specific currency
            Parameters:
                symbol: The symbol of the crypto
                fiat: The fiat currency
                time: The timeframe to get the data for

            Returns:
                A dataframe containing OHLCV data
        """

        logging.info(f"getting data for {symbol}{fiat}")

        # Retrieve data from the currency table based on the symbol
        currency = self.currencies[f"{symbol}{fiat}"]

        # Does data exist for the currency and timeframe?
        if currency.data[time] == []:
            logging.warning(f"No data for {symbol}{fiat}")
            currency.get_OHLCV(time, self.data_path)
            logging.info("Data loaded")
        return currency.data[time]
