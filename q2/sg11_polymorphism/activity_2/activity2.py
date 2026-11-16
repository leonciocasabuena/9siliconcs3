class Car: #Creates a class named Car. L
    def move(self): #Creates a function named move() with an action respective to the vehicle's purpose.
        print("The car drives on the road.")

class Boat: #Creates a class named Boat. E
    def move(self): #Creates a function named move() with an action respective to the vehicle's purpose.
        print("The boat sails on water.")

class Drone: #Creates a class named Drone. O
    def move(self): #Creates a function named move() with an action respective to the vehicle's purpose.
        print("The drone flies in the sky.")

def start_trip(vehicle): #Creates a function named start_trip(vehicle) with a parameter vehicle which will serve as a placeholder for whatever object shall be assigned to the action move() of this function.
    vehicle.move()

vehicles = [Car(), Boat(), Drone()] #Creates a list containing objects that were instantiated from each of the three classes abovementioned.

for vehicle in vehicles: #Creates a for loop which enumerates the objects inside the list named "vehicles" and assigns them to the temporary placeholder variable "vehicle" and executes the action inside the loop in each interval——which is was the function named start_trip(vehicle) declared earlier.
    start_trip(vehicle)

