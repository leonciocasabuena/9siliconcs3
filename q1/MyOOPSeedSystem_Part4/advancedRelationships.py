class Instrument:
  def __init__(self, Color, Type, IsTuned, IsPlayable):
    self.color = Color
    self.__type = Type
    self.IsTuned = IsTuned
    self.__IsPlayable = IsPlayable


class Guitar(Instrument):
  def __init__(self, Color, Type, IsTuned, IsPlayable, MarketPrice, ProductionYear):
    super().__init__(Color, Type, IsTuned, IsPlayable,)
    self.__marketprice = MarketPrice
    self.__productionyear = ProductionYear
    
