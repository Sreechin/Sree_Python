#A dictionary in Python is an unordered, mutable collection of key-value pairs. Instead of accessing elements using a numerical index (like a list), you look up values using unique keys.

#Think of it like a real-world dictionary or contact list: you look up a word or contact name (the key) to find its definition or phone number (the value).

#Key Characteristics
#Key-Value Structure: Data is stored as key: value pairs enclosed in curly braces {}.

#Unique Keys: Every key in a dictionary must be unique. If you assign a new value to an existing key, it overwrites the old value.

#Key Hashability: Keys must be immutable types (e.g., strings, numbers, or tuples). Values can be any data type, including lists or other dictionaries.

#Mutable: You can add, modify, or remove key-value pairs after the dictionary is created.

user = {
    "name": "Sree",
    "age": 40,
    "height": "4.11"
}

print(user["age"])
user["age"]=39 # Modifying the value of the key "age" to 39
print(user["age"])