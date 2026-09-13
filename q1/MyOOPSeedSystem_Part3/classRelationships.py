class Instrument: #Creates a class named "Instrument".
    
    #Creates a function which lists down all the attributes of the object in one function.
    def __init__(self, Color, Type, IsTuned, IsPlayable):
        self.color = Color
        self.__type = Type
        self.IsTuned = IsTuned
        self.__IsPlayable = IsPlayable
        
    #Creates a function which materializes the method tune() and lets it get called and utilized later on (A method which changes an attribute and safely interacts with an attribute).
    def tune(self):
        self.IsTuned = True
        print("Status: Tuned")

    #Creates a function play() which plays the instrument (A method which receives a parameter and changes an attribute).
    def play(self, note):
        self.__IsPlayable = True
        print("Status: Playing", note)

    #Creates a function getColor() which calls and displays a public attribute "Color" (A method which reads or returns information about the object).
    def getColor(self):
        return self.color

    #Creates a function getType() which calls and displays a private attribute "Type".
    def getType(self):
        return self.__type

    #Creates a function getIsTuned() which calls and displays a public attribute "IsTuned".
    def getIsTuned(self):
        return self.IsTuned

    #Creates a function getIsPlayable() which calls and displays a private attribute "IsPlayable". 
    def getIsPlayable(self):
        return self.__IsPlayable
    
class Musician: #Creates a class named "Musician".

    #Creates a function which declares and lists down some of the attributes of the musician in one function.
    def __init__(self, Name):
        self.__name = Name
        self.__instruments = []

    #Creates a function that retrieves and returns the name of the musician declared by a sub-class.
    def getName(self):
        return self.__name

    #Creates a function which takes and stores the declared instruments of a sub-class into a list, which can be enumerated or used later.
    def add_instrument(self, instrument):
        self.__instruments.append(instrument)

    #Creates a function that retrieves and returns the instruments the musician possesses from the said list.
    def getInstruments(self):
        return self.__instruments

#Declares all of the atttributes of both the musician and the instruments that'll be connected later.
musician = Musician("Leo")

instrument1 = Instrument("Red","Guitar", True, True)
instrument2 = Instrument("Yellow","Piano",True, True)
instrument3 = Instrument("Blue","Flute",True, True)

print("")
print("---BEFORE RELATIONSHIP---") #Prints out the musician's name along with the instruments that're associated and added to his instrument list BEFORE the relationship.


print(f"Musician: {musician.getName()}")
print(f"Instruments: {len(musician.getInstruments())}")

print("")
print("---BUILDING RELATIONSHIP---") #This part essentially appends and adds all of the declared instruments from the "Instrument" class earlier (instrument1 --> instrument3) to the musician's instrument list from the "Musician" class.

print(f"Adding {instrument1.getType()}...")
musician.add_instrument(instrument1)

print(f"Adding {instrument2.getType()}...")
musician.add_instrument(instrument2)

print(f"Adding {instrument3.getType()}...")
musician.add_instrument(instrument3)

print("")
print("---AFTER RELATIONSHIP---")#Prints out the musician's name along with all the intruments from the other class that were added and connected to his instruments list AFTER the relationship.

print(f"Musician: {musician.getName()}")
print("Instruments:")

#Creates a loop which essentially prints out all of the contents (instruments) inside the musician's instrument list.
i=1
for instrument in musician.getInstruments():
    print(f"Instrument {i}: {instrument.getType()}")
    i+=1

