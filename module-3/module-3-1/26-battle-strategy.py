"""Choosing an Adventurer's Class  **OPTIONAL CHALLENGE**
-------------------------  
Description:  
    As an Optional challenge take a crack at using Conditional statements within Conditional 
    Statements. Create a program that helps a new adventurer choose their class based on their attributes.  
    Use **nested `if`, `elif`, and `else` statements** to determine which class is best suited for the 
    adventurer.  

    The decision is based on three attributes:  
        1. Strength (measured from 1 to 20)  
        2. Intelligence (measured from 1 to 20)  
        3. Agility (measured from 1 to 20)

Class Logic:  
    - First, check the adventurer’s strength.  
        - If their strength is above a certain threshold, they could be a Warrior or Barbarian depending on 
        Agility. Barbarians might be more Agile than Warriors. 
        - If strength is lower, check intelligence to suggest other classes like Mage or Rogue depending on
        Agility. Rogues tend to be more Agile than a Bookworm like Mages.
    - If neither strength nor intelligence is high, suggest a more balanced class like Monk or Bard.  

    Example:
        If they have HIGH strength, but low Agility they should be a Warrior since they are probably
        wearing heavier armor than Barbarians therefore less Agile. THERE ARE NO WRONG ANSWERS, just
        make a decision.

Expected Input:  
    Strength: 15  
    Intelligence: 10  
    Agility: 8

Expected Output:  
    job_class : "Warrior"

Tasks  
    1. Create variables for `strength`, `intelligence`, and `Agility` (numbers between 1 and 20)
    2. Create an empty string Variable called job_class to reassign to their respective class
    3. Use nested conditional statements to evaluate which class fits best
    4. Re-assign them their new official class
    5. Print the suggested class based on the given attributes  

Your code below here:"""

