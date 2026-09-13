# Class Relationships: Association and Multiplicity
---
## Previous Work:
Part 1: [View my OOPAct Part 1: Classes and Objects](../MyOOPSeedSytem_Part1)

Part 2: [View my OOPAct Part 2: Class Attributes and Methods](../MyOOPSeedSystem_Part2)

---
## Existing Class:
| Class | Description |
|---|---|
| Instrument | This class represents an object that can be used for music. |

---
## New Related Class:
| Class | Description |
|---|---|
| Musician | A musician is someone who plays or wields a musical instrument; An instrument needs a musician for it to work and be used of its purpose. |

---
## Association:
| Relationship | Explanation |
|---|---|
| Musician HAS-AN Instrument. | The person in the class "Musician" can posses or wield an musical object from the class "Instrument". |

---
## Multiplicity:
| Multiplicity | Explanation |
|---|---|
| One-To-Many | A musician can possess and wield several instruments, and an instrument can belong to one person only. |

---
## Hyperlinks:
UML Class Relationship Diagram: [View my Class Relationship Diagram](images/classRelationshipDiagram.png)

Python Implementation: [View my Python Source](classRelationships.py)

Test Run: [View my Relationship Test Run](images/relationshipTestRun.png)

Object Relationship Diagram: [View my Object Relationship Diagram](images/objectRelationshipDiagram.png)

---
## Analysis:
### What is the association between your two classes?
 
The two classes (Musician and Instrument) have a "HAS-A" association, meaning one class (Musician) possesses the other (Instrument). My system denotes that the Musician class relates to the Instrument class through their connection in acting as a single unit when combined.
 
### What multiplicity did you choose and why?

I chose one-to-many multiplicity (specifically 1 ---> 1..*)  because it best fits my context and system. A musician may possess multiple instruments at once, and an instrument may only belong to one musician. 

### How did you implement the relationship in Python?

I implemented this relationship in Python by merging both classes into one file and letting them coexist and relate to each other. I pulled this off by copying the original "Instrument" class, then creating the other named "Musician" after it. After that, I instantiated 3 objects from the instrument class and 1 from the musician———then connected and related them through some methods.
 
### Why did you store an object reference instead of copying its data?

I stored an object reference because I wanted the Musician object to be directly connected to the actual Instrument objects. This allows the other subclasses from the "Musician" class to further access the instrument's methods and attributes through the relationship instead of only storing copied string information such as its name or type.
 
### If your relationship uses many, why is a list appropriate?

A list is appropriate because the relationship is one-to-many, meaning one musician can have multiple instruments. The list also allows me to store multiple Instrument objects and add more whenever needed instead of individually declaring every single instrument with a different variable every time.
