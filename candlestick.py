class candlestick:
    def __init__(self, open, high, low, close, volume):
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume

    def __str__(self):
        return 'open: {}, high: {}, low: {}, close: {}, volume: {}'.format(self.open, self.high, self.low, self.close, self.volume)
    