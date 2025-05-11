# 🐍 Intro to Python – Cheat Sheet

This cheat sheet summarizes key **terms**, **concepts**, **methods**, and **functions** from the _Intro to Coding (Python) Self-Paced_ course.

Note: When reading this file in VSCode, press the icon in the top left of your screen the shows two windows with a magnifying glass for a readable formatted version

---

## Python Basics

### Key Terms
- **Programming**: Writing instructions a computer can follow.
- **Syntax**: Rules of how code must be written.
- **Python**: Beginner-friendly programming language.

### Data Types
- `int` – Integer (e.g., `1`)
- `float` – Decimal (e.g., `3.14`)
- `str` – String/text (e.g., `"hello"`)
- `bool` – Boolean (`True` / `False`)

### Variables
```python
name = "Alice"
age = 30
pi = 3.14
is_student = True
```

### Operators
- `Arithmetic`: +, -, *, /, **, %
- `Comparison`: ==, !=, <, >, <=, >=
- `Logical`: and, or, not

## Strings and Numbers

### String Methods
```python
message = " Hello World "
message.lower()             # ' hello world '
message.upper()             # ' HELLO WORLD '
message.strip()             # 'Hello World'
message.replace("Hello", "Hi")  # ' Hi World '
len(message)                # 13

```

### Type Conversion
```python
int("10")       # 10
float("3.14")   # 3.14
str(100)        # "100"
```

### Other Functions
```python
abs(-7)                 # 7
round(3.14159, 2)       # 3.14
```

## Control Flow

### Conditional Statements
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### Loops: For Loops
```python
for i in range(5):
    print(i)
```

### Loops: While Loops
```python
count = 0
while count < 5:
    print(count)
    count += 1
```

## Lists

### List Basics
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
fruits.pop()
fruits[1]         # "banana"
```

### Common List Methods
- `.append(item)`
- `.remove(item)`
- `.pop(index)`
- `.insert(index, item)`
- `len(list)`

## Dictionaries

### Dictionary Basics
```python
person = {"name": "Alice", "age": 25}
person["name"]          # "Alice"
person.get("age")       # 25
```

### Common Dictionary Methods

- `.get(key)`
- `.keys()`
- `.values()`
- `.items()`
- `.update({key: value})`

## Functions 

### Key Concepts

- `Parameters`: Variables passed int a function
- `Return`: Sends output back to caller

## File Handling

### Write to a File
```python
with open("data.txt", "w") as f:
    f.write("Hello, world!")
```

### Read from a File
```python
with open("data.txt", "r") as f:
    content = f.read()
```

### File Modes

- `"r"`: read
- `"w"`: write (overwrite)
- `"a"`: append
- `"r+"`: read/write