class Animal: #Creates a parent class named Animal.
  def __init__(self, name):
      self.__name = name
    
  def eat(self):
      pass

  def make_sound(self):
      pass

class Lion(Animal): #Creates a child class Lion and declaring the Animal class as the superclass.
  def __init__(self, name):
      super().__init__(name)
      self.__name = name
    
  def eat(self):
      print(f"{self.__name} eats fresh meat.")

  def make_sound(self):
      print(f"{self.__name} roars loudly!")

class Elephant(Animal): #Creates a child class of the parent class Animal named Elephant.
  def __init__(self, name):
      super().__init__(name)
      self.__name = name
    
  def eat(self):
      print(f"{self.__name} eats grass and fruits.")

  def make_sound(self):
      print(f"{self.__name} trumpets!")

class Monkey(Animal): #Creates a child class of the parent class Animal named Monkey 
  def __init__(self, name):
      super().__init__(name)
      self.__name = name
    
  def eat(self):
      print(f"{self.__name} eats bananas.")

  def make_sound(self):
      print(f"{self.__name} chatters!")

#Instantiates three objects from the individual classes created above: Lion, Elephant, and Monkey.
lion = Lion("Scar")
elephant = Elephant("Meena")
monkey = Monkey("Wukong")

animals = [lion, elephant, monkey] #Compiles all three instantiated objects into one list named animals, which makes it easier to call and reiterate later.

#Creates a for loop which temporarily declares a variable "animal" as the objects of the list named "animal" in chronologica order, then the loop performs the assigned methods with respect to the object currently declared for every loop until all objects from the list are through.
for animal in animals:
  animal.make_sound()
  animal.eat()
  print("")







