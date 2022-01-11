from typing import Reversible


def reverse_string(input_string): #defining a function having a input 
    reverse_str = ""

    reverse_str = input_string[::-1]
    print(reverse_str)

#Putting value into the function reverse_string

reverse_string("Python") # prints nohtyP
reverse_string("Python is fun") #prints nuf si nohtyP