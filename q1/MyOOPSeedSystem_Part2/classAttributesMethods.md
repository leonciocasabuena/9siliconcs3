# Class Attributes and Methods

---
## - Previous Design
Link to my previous activity: [View my OOP Seed System Part 1](../MyOOPSeedSytem_Part1)

---
## - Design Revision
No major changes were needed from my original design.

---
## - Visibility Decisions
| Attribute | Data Type | Visibility | Reason |
|---|---|---|---|
|Color| String | Private | I kept this attribute private because it changes a physical state (color) and makes it susceptible to invalid syntaxes from sub-classes (e.g color: trasparent, color: none, etc.)——which may destroy my object. |
| Type | String | Private | I also kept this attribute private because it is the primary foundation of the other attributes and methods, for it serves as the basis for the latter: whether it be a piano, guitar, etc.  |
| IsTuned | Boolean | Private | I kept this attribute hidden too because this attribute can also destroy or render the object useless if modified recklessly. |
| IsPlayable | Boolean | Private  | Lastly, this attribute is the most important and must be kept private at all times. This attribute serves as the core function and essence of the any instrument and shall not be modified in any way unless the instrument is to be rendered unplayable. |

---
## - Hyperlinks

Updated UML Class Diagram: [View my Updated Class Diagram](images/classDiagramSG5.png)

Python Implementation: [View my Python Source](classImplementation.py)

Test Run: [View my Test Run](images/classTestRun.png)

Object Diagram: [View my Object Diagram](images/objectDiagram.png)

---
## - Analysis

### Why did you make your chosen attribute private?
I chose all of these attributes to be private because they all have the capacity to alter the object's overall state, and making it public makes it susceptible to invalid syntaxes from other classes which may possibly render my object defective and useless.

### Which method changes the state of your object?
The method in which changes the state of my object is tune(), which automatically changes the attribute "IsTuned" to True.

### How did your two objects demonstrate that instances are independent?
When I executed the method tune() on Object 1——Object 2 kept its original attributes and remained at its previous all while Object 1's "IsTuned" attribute changed to True.

### What is the difference between your class diagram and your object diagram?
The class diagram solely delineates the class blueprint or design, while the object diagram shows the two independent instances branching out form the blueprint in their changed states after the method was successfully executed.
