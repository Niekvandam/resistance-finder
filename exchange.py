from sqlite3 import TimeFromTicks
import pandas as pd
from crypto import Crypto
import sys
import os
from enums.timeframes import Timeframes
import logging


DATA_LOC = "data/"


class Exchange:
    def __init__(self, name, cryptos: list = None):
        self.name = name.lower()
        self.currencies = {}
        self.data_path = f"{DATA_LOC}{self.name}/"

    def add_crypto(self, crypto: Crypto):
        logging.info(f"Crypto {crypto.symbol} added to {self.name}")
        self.currencies[crypto.symbol] = crypto

    def get_data(self, symbol: str, fiat: str, time: Timeframes):
        logging.info(f"getting data for {symbol}{fiat}")
        currency = self.currencies[f"{symbol}{fiat}"]
        if currency.data[time] == []:
            logging.warning(f"No data for {symbol}{fiat}")
            currency.get_data(time, self.data_path)
            logging.info("Data loaded")
        return currency.data[time]
