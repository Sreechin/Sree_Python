#Lists in Python are ordered, mutable (changeable) sequences used to store collections of items. They are one of the most versatile and frequently used built-in data types.

#Key Characteristics
#Ordered: Items maintain their specific position. Access items via zero-based indexing (list[0]).

#Mutable: You can change, add, or remove elements after creation without creating a new list.

#Allows Duplicates: Lists can contain repeated values.

#Heterogeneous: A single list can hold mixed data types (integers, strings, floats, booleans, or even other lists).

Fruits = ["apple", "banana", "cherry", "date"]
Fruits[1] = "blueberry"  # Change the second item
Fruits.append("elderberry")  # Add a new item at the end
Fruits.remove("date")
print(Fruits)  