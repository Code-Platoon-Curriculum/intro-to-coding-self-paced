"""String Methods Practice  
-------------------------  
Description:  
    Use string methods to change the capitalization with a predefined variable. When using methods on a variable the normal
    syntax is by appending the method to the end of the variable.
        Example: my_variable.lower()
    
    Notice: Strings are immutable, which means they can't change. You have to re-assign the variable to see any change
    
Expected Input:
    "learning Python is FUN!"    

Expected Output:
    Lowercase: learning python is fun!  
    Uppercase: LEARNING PYTHON IS FUN!  
    Capitalized: Learning python is fun!
 
Task:
    1. Create a variable `text` and assign it the value: "learning Python is FUN!"
    2. Convert the entire string to lowercase using `.lower()` and re-assigning it
    3. Display the result
    4. Convert the entire string to uppercase using `.upper()` and re-assigning it
    5. Display the result
    6. Capitalize just the first character of the string using `.capitalize()` and re-assigning it
    7. Display the result.
                            
Your code below here"""

text = "hello"
text.upper()
print(text)