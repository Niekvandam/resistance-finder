class candlestick:
    """ Candlestick class, used to store OHLCV data.
    This will be the main way in which we analyze data during the analysis.
    """

    def __init__(self, open, high, low, close, volume):
        """ Create candlestick object

            Parameters:
                open: The open price
                high: The highest price
                low: The lowest price
                close: The closing price
                volume: The volume of the candlestick
        """
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __str__(self):
        return 'open: {}, high: {}, low: {}, close: {}, volume: {}'.format(self.open, self.high, self.low, self.close, self.volume)
