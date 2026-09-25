#custom exception creation 
#create a class make that class as child to the anyone root exception class
#and take constructor inside the class
class InsufficientBalance(BaseException):
    def __init__(self, message):
        super().__init__(message)

f=open("inactive.txt")

balance=100
withdrawlAmount=200
if balance<withdrawlAmount:
    raise InsufficientBalance("a cannot be less then b")
try:
    print(f.read())
    fnum=int(input("Enter first number for division"))
    snum=int(input("Enter second number for division"))
    result=fnum/snum
    print("division of two numbers is  :",result)
    list=[1,2,3]
    print(list[2])
    print(list.append(12))   
except ZeroDivisionError:
    print("Cannot divide by zero")
except ValueError:
    print("please enter only number")    
except IndexError:
    print("invalid index...")  
except AttributeError:
    print("invalid method usage")     
except FileNotFoundError:
    print("the given file not there for reading")  
except FileExistsError:
    print("unable to create file its already there") 
except BaseException as ex:
    print("some other exception",ex.__class__)         
else:
    print("this will execute only when there is no error")            
finally:
    f.close()   
    print("cleanup code  always executes.....") 

print("remaining 10000 lines ")