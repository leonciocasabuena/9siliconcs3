#INHERITANCE SYSTEM
class Instrument:
  def __init__(self, Color, Type, IsTuned, IsPlayable):
      self.color = Color
      self.__type = Type
      self.IsTuned = IsTuned
      self.__IsPlayable = IsPlayable

  def get_color(self):
      return self.color

class Guitar(Instrument):
  def __init__(self, Color, Type, IsTuned, IsPlayable, MarketPrice, ProductionYear, Strings):
      super().__init__(Color, Type, IsTuned, IsPlayable,)
      self.__marketprice = MarketPrice
      self.__productionyear = ProductionYear
      self.string = Strings #Creates a composition relationship with an object named "String"

  def get_color(self):
      return self.color
    
parent_instrument=Instrument("Indigo", "Guitar", "True", "True")  
guitar=Guitar("Indigo", "Guitar", "True", "True", "5000", "2026", "6 Strings")

print("---TEST 1: INHERITANCE---")
print("Parent attribute:") 
print(f"Color: {parent_instrument.get_color()}")
print("")
print("Child object:")
print(f"Color: {guitar.get_color()}")


print("")
print("---TEST 2: COMPOSITION---")
