import sys
x = int(input("first number:"))
y = int(input("second number:"))
try:
    res=x/y
    print(res)
except ZeroDivisionError:
    print("division by zero")