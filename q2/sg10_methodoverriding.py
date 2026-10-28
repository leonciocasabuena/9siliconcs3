class Animal: #Creates a parent class named Animal.
  def __init__(self, name): #Creates a function which serve as the default constructor of th class containing all of its attributes for the objects that'l be instantiated later.
      self.__name = name
    
  def eat(self):
      pass

  def make_sound(self):
      pass

class Lion(Animal): #Creates a child class Lion and declaring the Animal class as the superclass.
  def __init__(self, name): #Creates a function which serve as the default constructor of th class containing all of its attributes for the objects that'l be instantiated later.
      super().__init__(name) #A built in function which calls the __init__ method of the parent class Animal, which allows the child class to reuse the method of the parent class alongside its attributes without completely overriding it.
      self.__name = name

#Creates two methods named eat() and make_sound() with names identical to those of the parent class. However, since the class Lion is a child class of the parent class Animal -- the program lets the child class overrride the said methods and let it display a new output with respect to the information given about the said animal.
  def eat(self):
      print(f"{self.__name} eats fresh meat.")

  def make_sound(self):
      print(f"{self.__name} roars loudly!")

class Elephant(Animal): #Creates a child class of the parent class Animal named Elephant.
  def __init__(self, name): #Creates a function which serve as the default constructor of th class containing all of its attributes for the objects that'l be instantiated later.
      super().__init__(name) #A built in function which calls the __init__ method of the parent class Animal, which allows the child class to reuse the method of the parent class alongside its attributes without completely overriding it.
      self.__name = name

#Creates two methods named eat() and make_sound() with names identical to those of the parent class. However, since the class Elephant is a child class of the parent class Animal -- the program lets the child class overrride the said methods and let it display a new output with respect to the information given about the said animal. 
  def eat(self):
      print(f"{self.__name} eats grass and fruits.")

  def make_sound(self):
      print(f"{self.__name} trumpets!")

class Monkey(Animal): #Creates a child class of the parent class Animal named Monkey 
  def __init__(self, name): #Creates a function which serve as the default constructor of th class containing all of its attributes for the objects that'l be instantiated later.
      super().__init__(name) #A built in function which calls the __init__ method of the parent class Animal, which allows the child class to reuse the method of the parent class alongside its attributes without completely overriding it.
      self.__name = name

#Creates two methods named eat() and make_sound() with names identical to those of the parent class. However, since the class Monkey is a child class of the parent class Animal -- the program lets the child class overrride the said methods and let it display a new output with respect to the information given about the said animal.   
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







