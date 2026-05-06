# System Testing & Continuous Integration – Part 1

This repository contains the work for **Part 1** of the ST&CI Practical.

 Contents
- `part1.py` — Interest calculation function  
- `test_part1.py` — Pytest unit tests covering:
  - All interest tiers
  - Boundary values
  - Invalid partitions (string, boolean, negative)
- `.circleci/config.yml` — CircleCI pipeline configuration

Unit Testing
The tests verify:
- Correct interest calculation for all deposit tiers  
- Boundary conditions at €1,000, €11,000, and €100,000  
- Error handling for invalid inputs:
  - Strings  
  - Booleans  
  - Negative values  

 Continuous Integration (CI)
This project uses **CircleCI** to automatically:
1. Install dependencies  
2. Run pytest  
3. Display pass/fail results on every push  

 Lecturer Access
The required collaborator has been added:  
**peter.gosling@dkit.ie**


