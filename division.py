try:
    fnum=int(input("Enter first number for division"))
    snum=int(input("Enter second number for division"))
    result=fnum/snum
    print("division of two numbers is  :",result)
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("please enter only number")        
print("remaining 10000 lines ")