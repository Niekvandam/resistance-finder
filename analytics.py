from os import supports_follow_symlinks
from pandas import DataFrame
from candlestick import candlestick
import logging
from enums.keyareas import Keyareas


def get_key_areas(df: DataFrame, areatype: Keyareas = Keyareas.SUPPORT):
    areas = {}
    logging.info(f"Getting key {areatype.name} areas")
    for idx, i in enumerate(df.iterrows()):
        if idx < 2 or idx > len(df)-2:
            logging.debug(f"skipping {idx}")
            continue
        if idx % 1000 == 0:
            logging.info(f"processing {idx} with price {i[1]['low']}")
        if areatype == Keyareas.RESISTANCE:
            if is_resistance(df, idx):
                areas[idx] = i[1]['high']
        if areatype == Keyareas.SUPPORT:
            if is_resistance(df, idx):
                areas[idx] = i[1]['low']
    return areas


def is_support(df, idx):
    support = df['low'][idx] < df['low'][idx-1] and \
        df['low'][idx] < df['low'][idx+1] and \
        df['low'][idx+1] < df['low'][idx+2] and \
        df['low'][idx-1] < df['low'][idx-2]
    return support


def is_resistance(df, i):
    resistance = df['high'][i] > df['high'][i-1] and\
        df['high'][i] > df['high'][i+1] and \
        df['high'][i+1] > df['high'][i+2] and \
        df['high'][i-1] > df['high'][i-2]
    return resistance
