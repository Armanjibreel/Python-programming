# age=int(input("Enter your age:"))
# try:
#     if (age<18):
#         raise ValueError()
#     else:
#         print("your are eligible")
# except ValueError as Ve:
#     print("you can not vote")
#
#
# age=int(input("Enter your age:"))
# try:
#     if (age<18):
#         raise ValueError("you can not vote")
#     else:
#         print("your are eligible")
# except ValueError as Ve:
#     print("Ve")

# class UnderAgeException(Exception):
#     pass
# class Arman:
#     age=int(input("Enter your age:"))
#     try:
#         if(age<18):
#             raise UnderAgeException("u are under age")
#         else:
#         print("you are eligible")
#     Except UnderAgeException as uae:
#         print(uae)


class SvenDivisionError(Exception):
    def __init__(self,):
        print("you can not divide by seven")
    pass
class Main:
    num1=int(input("enter the first number:"))
    num2=int(input("enter the second number:"))
    try:
        if (num2==7):
            raise SvenDivisionError
        else:
            res=num1/num2
            print(res)
    except SvenDivisionError as sde:
        print(sde)