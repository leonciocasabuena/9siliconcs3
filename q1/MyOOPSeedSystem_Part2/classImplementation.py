class Instrument: #Creates a class named "Instrument".
    
    #Creates a function which lists down all the attributes of the object in one function.
    def __init__(self, Color, Type, IsTuned, IsPlayable):
        self.__color = Color
        self.__type = Type
        self.__IsTuned = IsTuned
        self.__IsPlayable = IsPlayable
        
    #Creates a function which materializes the method tune() and lets it get called and utilized later on (A method which changes an attribute and safely interacts with an attribute).
    def tune(self):
        self.__IsTuned = True
        print("Status: Tuned")

    #Creates a function play() which plays the instrument (A method which receives a parameter and changes an attribute).
    def play(self, note):
        self.__IsPlayable = True
        print("Status: Playing", note)

    #Creates a function getColor() which calls and displays a private attribute "Color" (A method which reads or returns information about the object).
    def getColor(self):
        return self.__color

    #Creates a function getType() which calls and displays a private attribute "Type".
    def getType(self):
        return self.__type

    #Creates a function getIsTuned() which calls and displays a private attribute "IsTuned".
    def getIsTuned(self):
        return self.__IsTuned

    #Creates a function getIsPlayable() which calls and displays a private attribute "IsPlayable". 
    def getIsPlayable(self):
        return self.__IsPlayable


object1 = Instrument("Blue", "Guitar", False, True) #Assigns an object named "object1" which contains all of it's attributes in one compiled parameter.
object2 = Instrument("Red", "Piano", True, True) #Assigns another object named "object2" which also contains all of it's attributes in a compiled parameter.

print("---INITIAL STATE---") #Prints out all of the assigned attributes and calling all of the previous functions of both objects BEFORE the chosen method is performed.
print("OBJECT 1:")
print("Color:", object1.getColor())
print("Type:", object1.getType())
print("Tuned:", object1.getIsTuned())
print("Playable:", object1.getIsPlayable())

print("")

print("OBJECT 2:")
print("Color:", object2.getColor())
print("Type:", object2.getType())
print("Tuned:", object2.getIsTuned())
print("Playable:", object2.getIsPlayable())

print("")
print("Doing tune() method on OBJECT 1...")
object1.tune() #Calls the method tune() to tune "object1" and perform the assigned task of the said function.
print("")

print("---FINAL STATE---") #Prints the final state and attributes of both objects AFTER the method tune() was perfoemd on "object1" while leaving "object2" unchanged.    
print("OBJECT 1:")
print("Color:", object1.getColor())
print("Type:", object1.getType())
print("Tuned:", object1.getIsTuned())
print("Playable:", object1.getIsPlayable())

print()

print("OBJECT 2:")
print("Color:", object2.getColor())
print("Type:", object2.getType())
print("Tuned:", object2.getIsTuned())
print("Playable:", object2.getIsPlayable())



