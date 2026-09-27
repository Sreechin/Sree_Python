#Argument Passing in Python

# the_world_is_flat = True

# if the_world_is_flat:
#     print("Be careful not to fall off!")

##==============================================
# data Types in Python 
# NUMBER, (1,2,) 
# FLOAT (1.1, 2.2), 
# STRING ("Hello"), 
# BOOLEAN (True, False), 
# LIST ([1, 2, 3]), 
# TUPLE ((1, 2, 3)), 
# SET ({1, 2, 3}), 
# DICTIONARY ({"key": "value"})

number1=100
number2=20

print(number1 + number2) # addition
print(number1 - number2) # subtraction
print(number1 / number2) # division
print(number1 * number2) # multiplication
print(number1 % number2) # modulo
print(number1 ** 2) # exponentiation - Square of number1 raised to the power of 2
print(number1 // number2) # floor division - Gives the quotient of the division, rounded down to the nearest whole number.

#==============================================
# Concatination of strings
prefix='py'
prefix1='thon'

word=prefix+prefix1
print(word) # Concatenation of prefix and prefix1

#==============================================

#SUBSTRING
word='python'
print(len(word)) # prints 6 - length of the string
print(word[0:1]) # prints 'p' - substring from index 0 to 1 (exclusive)
print(word[0:2]) # prints 'py' - substring from index 0 to 2 (exclusive)
print(word[0:3]) # prints 'pyt' - substring from index 0 to 3 (exclusive)
print(word[:4])
#==============================================

## len() funcion

word='supercalifragilisticexpialidocious'
print(len(word)) # prints 34 - length of the string

## Lists -- group of items in a single variable seperated by comma
# Unlike strings, lists are mutable, meaning you can change their content without changing their identity.
my_list = [1, 2, 3, 4, 5]

print(my_list[0]) # prints 1 - first element of the list

# Append list
my_list.append(6) # adds 6 to the end of the list
print(my_list) # prints [1, 2, 3, 4, 5, 6]

# replace list element
my_list[0] = 10 # replaces the first element with 10
print(my_list) # prints [10, 2, 3, 4, 5, 6]

word_list=['red','yellow','green','blue']   
word_list.append('orange') # adds 'orange' to the end of the list
print(word_list) # prints ['red', 'yellow', 'green', 'blue', 'orange']

word_list[0] = 'purple' # replaces the first element with 'purple'
print(word_list) # prints ['purple', 'yellow', 'green', 'blue', 'orange']

num_list=[1,2,3,4,5]
num_list.append(6) # adds 6 to the end of the list
print(num_list) # prints [1, 2, 3, 4, 5, 6]  

num_list[0:3] = [10, 20, 30] # replaces the first three elements with 10, 20, 30
print(num_list) # prints [10, 20, 30, 4, 5, 6]  

## Fibonacci series
a=0
b=1

while a<=10:
        print(a,end=' ')
        temp=a
        a=b
        b=temp+b

## For loop

animal_list = ['cat', 'dog', 'rabbit', 'hamster']

for animal in animal_list:
        print(animal,len(animal)) # prints each animal in the list

#######################
users={'Alice': 25, 'Bob': 30, 'Charlie': 35}

for name,age in users.copy().items():
        if age >= 35:
                del users[name] # removes users with age greater than or equal to 30    
                print(name,age) # prints each name and age in the dictionary

print(users) # prints the updated dictionary after removing users with age greater than or equal to 30

young_users = {}
for name, age in users.items():
        if age < 30:
                young_users[name] = age # adds users with age less than 30 to the new dictionary
print(young_users) # prints the new dictionary with users under 30

####  Range function:If you do need to iterate over a sequence of numbers, the built-in function range() comes in handy. It generates arithmetic progressions:

for i in range(5):
        print(i) # prints numbers from 0 to 4   

a=['priya','sneha','snehal','priyanka']
for i in range(len(a)):
        print(i,a[i])

## even and odd numbers
for i in range(1,20):
    if i%2==0:
        print("Even number:",i) 
    else:
        print("Odd number:",i)

### Defining a function

def fibonacci(a):

        """Print the Fibonacci series up to a given number."""
        b, c = 0, 1
        while b < a:
                print(b, end=' ')
                b, c = c, b + c
fibonacci(100) # prints the Fibonacci series up to 10

#Lambda function: A lambda function is a small anonymous function that can take any number of arguments,
#but can only have one expression. 
#It is often used for short, throwaway functions that are not reused elsewhere in the code.
lambda_function = lambda x: x * 2
print(lambda_function(5)) # prints 10 - result of the lambda function

lambda_function = lambda x: x * 2/5
print(lambda_function(5)) # prints 10 - result of the lambda function