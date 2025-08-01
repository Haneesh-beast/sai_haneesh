#Exception Handling
#except--->try block unna code error vostey except execute
#else---->try block lo elanti errors leakpotey else block execute
#finally ---> always execute

# try:
#     print(a) #risky code
# except:
#     print("Error vachindi")
# else:
#     print("Error raledu")
# finally:
#     print("always I will execute")


# try:
#     print("a")
# except:
#     print("Error vahindi")
# else:
#     print("Error raledu")
# finally:
#     print("I will always execute")


#try block rastey compulsary ga except block rayali
# try:
#     print("p"+25)
# except:
#     print("Error occured")


# try:
#     number1=int(input("Enter number1:"))
#     number2=int(input("Enter number2:"))
#     print(number1/number2)
# except:
#     print("You can't divide by zero")

# try:
#     number=int("suresh")
#     print(number)
# except:
#     print("Error occured")


# try:
#     text="suresh"
#     new_string=text.reverse()
#     print(new_string)
# except:
#     print("this method doesn't exist for this object")


# try:
#     file=open("demo.txt",mode="r+")
#     c=file.read()
#     print(c)
# except:
#     print("The file was not found")

# try:
#     number=int(input("Enter a number:"))
#     print(number)
# except:
#     print("That is not a number")


#oka try block ki multiple except block lu rayachu
# try:
#     print("p"+25)
# except TypeError:
#     print("Type Error occured")
# except NameError:
#     print("Name Error occured")
# except AttributeError:
#     print("Attribute Error")


# try:
#     print("p"+25)
# except Exception as e:
#     print(f"Error occured:{e}")


# try:
#     number=int("suresh")
#     print(number)
# except (ValueError,TypeError,AttributeError) as pruthvi:
#     print(f"Error occured:{pruthvi}")


# try:
#     result=45/0
# except AttributeError:
#     print("Attribute Error")
# except ZeroDivisionError:
#     print("You cannot divide by zero")


# try:
#     print(a)
# except TypeError:
#     print("Type Error occured")
# except NameError:
#     print("Name Error occured")
# except ValueError:
#     print("Value Error occured")

#syntax error
# if True
#     print("Hello")

#Indentation Error
# if True:
# print("Hello")


#Type Error
# a=2+"p"
# print(a)

#key error
# my_dictionary={"name":"pruthvi","rollno":5}
# print(my_dictionary["age"])

#Index Error
# my_list=[2,3.5,True,"sai",[2,5]]
# print(my_list[8])

#Name Error
# print(g)


#keyboardInterrupt--->ctril+c
# while True:
#     print(" Welcome to PythonLife ",end="")


#EOF (End of File)--->ctrl+z
# while True:
#     print(input("Enter your name:"))


#attribute Error
# numbers=(5,3.5,True,3+5j)
# numbers.append("suresh")
# print(numbers)


#ModuleNotFoundError
# import Pushpa

#Value Error
# number=int(input("Enter a number:"))
# print(number)

# while True:
#     try:
#         number1=float(input("Enter the first number:"))
#         try:
#             number2=float(input("Enter the second number:"))
#             try:
#                 operator=input("Enter an operator:")
#                 if operator=="+":
#                     print(f"Result:{number1+number2}")
#                 elif operator=="-":
#                     print(f"Result:{number1-number2}")
#                 elif operator=="*":
#                     print(f"Result:{number1*number2}")
#                 elif operator=="/":
#                     try:
#                         print(f"Result:{number1/number2}")
#                     except:
#                         print("Cannot divide by zero")
#                 else:
#                     print("You chosen operator")
            
#             except Exception as e:
#                 print("Error occured :",e)
#         except ValueError:
#             print("Second number is not valid")
#     except ValueError:
#         print("First number is not valid")

# while True:
#     try:
#         number1=int(input("Enter number1:"))
#         try:
#             number2=int(input("Enter number2:"))
#             try:
#                 print("Result:",number1/number2)
#             except ZeroDivisionError:
#                 print("Cannot divide by zero...")
#         except ValueError:
#             print("second number input is not a number")
#     except ValueError:
#         print("First number input is not a number")


