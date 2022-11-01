#Dominic Oladapo-Tonade - 6469


import math

math.sqrt(-10)


"""
    output:
    
    Traceback (most recent call last):
  File "C:/.../ValueError - 6469.py", line 6, in <module>
    math.sqrt(-10)
ValueError: math domain error


solution



import math

d = int(input('Please enter a positive number: \n'))

try:
    print(f'Square Root of {d} is {math.sqrt(d)}')
except ValueError as verr:
    print(f'The number {d} you entered is not a positive number!')
"""
