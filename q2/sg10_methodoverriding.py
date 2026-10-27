class Animal:
  def __init__(self, name):
      self.__name = name
    
  def eat(self):
      pass

  def make_sound(self):
      pass

class Lion(Animal):
  def __init__(self, name):
      super().__init__(name)
      self.__name = name
    
  def eat(self):
      print(f"{self.__name} eats fresh meat.")

  def make_sound(self):
      print(f"{self.__name} roars loudly!")

class Elephant(Animal):
  def __init__(self, name):
      super().__init__(name)
      self.__name = name
    
  def eat(self):
      print(f"{self.__name} eats grass and fruits.")

  def make_sound(self):
      print(f"{self.__name} trumpets!")

class Monkey(Animal):
  def __init__(self, name):
      super().__init__(name)
      self.__name = name
    
  def eat(self):
      print(f"{self.__name} eats bananas.")

  def make_sound(self):
      print(f"{self.__name} chatters!")

lion = Lion("Scar")
elephant = Elephant("Meena")
monkey = Monkey("Wukong")

animals = [lion, elephant, monkey]

for animal in animals:
  animal.make_sound()
  animal.eat()
  print("")







