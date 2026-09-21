class Instrument:
  def __init__(self, Color, Type, IsTuned, IsPlayable):
    self.color = Color
    self.__type = Type
    self.IsTuned = IsTuned
    self.__IsPlayable = IsTuned


class Guitar(Instrument):
  def __init__(self, Color, Type, IsTuned, IsPlayable):
    super().__init__(MarketPrice, ProductionYear)
      self.__marketprice = MarketPrice
      self.__productionyear = ProductionYear
    
