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
| One-To-Many | A musician can posses and wield several instruments, and an instrument can belong to one person only. |

---
## Hyperlinks:
UML Class Relationship Diagram: [Class Relationship Diagram](images/classRelationshipDiagram.png)

Python Implementation: [View Python Source](classRelationships.py)

Test Run: [Relationship Test Run](images/relationshipTestRun.png)

Object Relationship Diagram: [Object Relationship Diagram](images/objectRelationshipDiagram.png)

---
## Analysis:
 What is the association between your two classes?
 
 What multiplicity did you choose and why?
 
 How did you implement the relationship in Python?
 
 Why did you store an object reference instead of copying its data?
 
 If your relationship uses many, why is a list appropriate?
