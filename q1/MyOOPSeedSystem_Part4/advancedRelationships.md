# Advanced Class Relationships

---
## Previous Activities
Part 2: [View my OOPAct Part 2: Class Attributes and Methods](../MyOOPSeedSystem_Part2)

Part 3: [View my OOPAct Part 3: Class Relationships](../MyOOPSeedSystem_Part3)

---
## Existing System Description:
### What classes currently exist in your system?
● Class 1: Instrument

● Class 2: Musician

### What problem or limitation exists in your current design?

● Repeated attributes

● Repeated methods

● Generic attributes

---
## Inheritance Relationship:
|Parent|Child|Explanation|
|---|---|---|
|Instrument|Guitar| Guitar becomes the child class, and Instrument becomes the parent class because a guitar has an "IS-A" inheritance with an instrument; therefore, the guitar inherits some of the attributes and methods of the parent class it came from (Guitar IS-A Instrument)|

---
## Composition/Aggregation:
|Relationship|Explanation|
|---|---|
|Composition|I chose composition because I had previously created a child class named "Guitar", and I figured that it would make a good composition relationship with an object "String"——which is in fact a literal part of a guitar. |

---
## Hyperlinks:
Inheritance UML: [View my Inheritance UML Diagram](images/inheritanceDiagram.png)

Advanced UML Diagram: [View my Advanced UML Diagram](images/advancedClassDiagram.png)

Python Implementation: [View my Source Code](advancedRelationships.py)

Test Run: [View my Test Run](images/advancedTestRun.png)

Object Diagram: [View my Object Diagram](images/advancedObjectDiagram.png)

---
## Reflection
### Why did you choose your inheritance relationship? Explain why your child class is a type of your parent class.
I chose the inheritance relationship because I can create an infinite amount of child classes from the parent class with minimal effort with the usage of the super() function. On the other hand, the child class "Guitar" is considered a child class or a type of the parent class "Instrument" because the former essentially fits the categorical descriptions of the former: a device created or adapted to make musical sounds.

### How did inheritance reduce duplicate code? Identify attributes or methods that were reused.
Inheritance vastly reduced the duplicate code by using the super() function in the child class (class Child(Instrument)); this function predominantly copies the attributes from the parent class and inserts them into the child class once declared, with minimal code duplication.

### Why is your HAS-A relationship Composition or Aggregation? Explain the lifecycle relationship between the two objects.
I specifically chose composition because the component "String" is a dependent part of the object it inhabits; it cannot independently exist if the object "Guitar is removed. 

### What is the difference between Association from Part III and the advanced relationship you implemented?
In part IV, a relationship is used a broad and categorical term for any connection between classes——which in this case are inheritance and composition. However, in part III, an association is used between two classes (Musician and Instrument)——which is a specific type of relationship.

### How does your design follow the DRY principle?
In part IV, yes, the system has drastically followed the "Don't Repeat Yourself" principle of coding. Due to the existence of OOP, the hassle of creating and assigning different variables at large quantities has been dramatically decreased.
