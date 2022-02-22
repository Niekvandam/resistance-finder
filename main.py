from pandas import DataFrame
from analytics import get_key_areas
import exchange as ex
import crypto as crypto
from timeframes import Timeframes
import logging
import streamlit as st
from keyareas import Keyareas


def create_set(df: DataFrame):
    set1 = {'x': df["Date"]}
    


if __name__ == "__main__":
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)
    logging.basicConfig(level=logging.DEBUG, filename='logs/resistancefinder.log',datefmt='%a, %d %b %Y %H:%M:%S', filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.debug("Starting")
    exchange = ex.Exchange('Binance')
    crypto = crypto.Crypto('BTCUSDT')
    exchange.add_crypto(crypto)
    data = exchange.get_data('BTC', 'USDT', Timeframes.ONE_HOUR)
    for area in get_key_areas(data, Keyareas.SUPPORT):
        logging.debug(f"{area} is a {Keyareas.SUPPORT.name} level")
    print(data["close"][:5000])
    st.candle(data["close"])
