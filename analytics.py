from os import supports_follow_symlinks
from pandas import DataFrame
from candlestick import candlestick
import logging
from enums.keyareas import Keyareas

# TODO - Implement resistance/support flipping
# TODO - Implement MA + S


def get_key_areas(df: DataFrame, areatype: Keyareas = Keyareas.SUPPORT) -> DataFrame:
    """Returns the key areas of a dataframe.
        Key areas can be areas of support and resistance, used to determine buy and sell signals.

        Parameters:
            df: The dataframe to get the key areas for
            areatype: The type of key areas to get, either support or resistance

        Returns:
            A list of key areas
    """
    areas = {}
    logging.info(f"Getting key {areatype.name} areas")
    # Loop over dataframe rows with enumerate, so that we can get the index
    for idx, i in enumerate(df.iterrows()):

        # Index check to prevent index out of range
        if idx < 2 or idx > len(df)-2:
            logging.debug(f"skipping {idx}")
            continue

        # Logging every 1000 iters
        if idx % 1000 == 0:
            logging.info(f"processing {idx} with price {i[1]['low']}")
        # Check if support or resistance
        if areatype == Keyareas.RESISTANCE:
            if is_resistance(df, idx):
                # Is resistance, add to dict based on the dataframe index
                areas[idx] = i[1]['high']
        if areatype == Keyareas.SUPPORT:
            if is_resistance(df, idx):
                # Is support, add to dict based on the dataframe index
                areas[idx] = i[1]['low']
    return areas


def is_support(df, idx):
    """ Checks if the current row is a support.
        Support is checked by checking if the current row is the lowest the last two rows, and the lowest of the upcoming two rows. 

        Parameters:
            df: The dataframe to check
            idx: The index of the current row

        Returns:
            True if the current row is a support, False otherwise
    """
    support = df['low'][idx] < df['low'][idx-1] and \
        df['low'][idx] < df['low'][idx+1] and \
        df['low'][idx+1] < df['low'][idx+2] and \
        df['low'][idx-1] < df['low'][idx-2]
    return support


def is_resistance(df, i):
    """ Checks if the current row is a resistance.
        Resistance is checked by checking if the current row is the highest the last two rows, and the highest of the upcoming two rows.

        Parameters:
            df: The dataframe to check
            i: The index of the current row

        Returns:
            True if the current row is a resistance, False otherwise
    """
    resistance = df['high'][i] > df['high'][i-1] and\
        df['high'][i] > df['high'][i+1] and \
        df['high'][i+1] > df['high'][i+2] and \
        df['high'][i-1] > df['high'][i-2]
    return resistance
