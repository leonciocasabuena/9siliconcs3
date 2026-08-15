# Computational Thinking Exercise
## Smart School Canteen Queue
### Name: Leoncio B. Casabuena III
### Section: 9-Silicon
### Last Name: Casabuena
### Date: Date Completed
---

## Step 1: Identify the Big Problem
### The canteen lacks an efficient system that automates simple tasks (e.g. Suggestion System, Automated Computer, Stock Monitor, etc.), which takes a significant amount of time that causes the prolonged transactions and long queues.
---
## Step 2: Identify the Sub-Problems
1. The lack of a suggestion system where students are presented with best-selling or delectable products to help them decide faster.
2. The lack of an automated computing system that automatically computes the total amount and changes.
3. The lack of a stock monitoring system that actively change whenever a product is added or reduced in real time.
4. An insufficient number of cashiers and lines which divides one full line into several ones to make queueing faster.
---
## Step 3: Apply Computational Thinking Skills
| Sub-Problem | CT Skill | Proposed Solution |
|---|---|---|
| No Suggestion System | Pattern Recognition | Cashiers are encouraged to interact and socialize with students so that they have scant ideas of what individual students' frequently bought products and favorites are to give them a chance to suggest whether it be the usual or not.
| No Automated Computing System | Algorithm Design | Creating an automated algorithm that inserts the product price along the payment and calculates the exact change of the buyer in an instant.|
| No Stock Monitoring System | Algorithm Design | Creating an automated system where product quantities and stocks are stored into a cache where it then automatically gets subtracted whenever a product is taken or bought. |
| Insufficient Queue Lines | Decomposition | Canteen queue lines should be separated into three to five lines at least with a reliable and competent cashier behind the counters, so that the canteen could accommodate multiple students at once efficiently. |
---
## Step 4: Algorithmic Solution
### Selected Sub-Problem
The Lack of an Automated Computing System
### Pseudocode:

START

INPUT ProductPrice
INPUT BuyerAmount

IF BuyerAmount>=ProductPrice

  Change = BuyerAmount minus ProductPricwe

  OUTPUT "Change:", Change

ELSE 

  OUTPUT "Insufficient Payment."

END

---
