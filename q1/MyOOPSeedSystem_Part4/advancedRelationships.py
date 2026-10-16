
class Instrument: #Creates a class named "Instrument".
  def __init__(self, Color, Type, IsTuned, IsPlayable):
      self.color = Color
      self.__type = Type
      self.IsTuned = IsTuned
      self.__IsPlayable = IsPlayable

  def get_color(self):
      return self.color

class guitar_components: #Creates a class "guitar_components" which iterates the components of the child class that will be used for a composition relationship later.

  def __init__(self, String):
      self.__string = String

  def get_strings(self):
      return self.__string

class Guitar(Instrument): #Creates a child class named "Guitar" and declares the class "Instrument" as parent class.
  def __init__(self, Color, Type, IsTuned, IsPlayable, MarketPrice, ProductionYear):
      super().__init__(Color, Type, IsTuned, IsPlayable,)
      self.__marketprice = MarketPrice
      self.__productionyear = ProductionYear
      self.string = guitar_components("6-strings") #Creates a composition relationship with an object inside the class "guitar_components" by calling the getter function from the said class.
    
  def get_color(self):
      return self.color

  #Creates a function that calls the declared attribute that made a composition relationship with an object from the "guitar_components" class
  def get_Strings(self):
      return self.string.get_strings()

#Instantiates an object from each parent and child class.
parent_instrument=Instrument("Indigo", "Guitar", "True", "True")  
guitar=Guitar("Indigo", "Guitar", "True", "True", "5000", "2026")

#Tests the inheritance system by calling the attributes of the parent class from the child class.
print("---TEST 1: INHERITANCE RELATIONSHIP---")
print("Parent attribute:") 
print(f"Color: {parent_instrument.get_color()}")
print("")
print("Child object:")
print("Guitar")
print(f"\t-Color: {guitar.get_color()}")

#Tests the composition system by performing the previously set-up composition system between the "guitar_components" and "Guitar" classes.
print("")
print("---TEST 2: COMPOSITION RELATIONSHIP---")
print(f"Guitar contains strings: {guitar.get_Strings()}")
