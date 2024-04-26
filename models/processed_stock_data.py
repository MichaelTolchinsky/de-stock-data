class ProcessedStockData:
  def __init__(self, symbol: str, date: str, close: float) -> None:
      self.sybmol = symbol
      self.data = date
      self.close = close
