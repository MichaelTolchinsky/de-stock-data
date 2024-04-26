class RawStockData:
  def __init__(self, date: str, open: float, high: float, low: float, close: float, volume: int) -> None:
      self.date = date
      self.open = open
      self.high = high
      self.low = low
      self.close = close
      self.volume = volume
