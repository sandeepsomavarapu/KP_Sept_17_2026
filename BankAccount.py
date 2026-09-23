class BankAccount:
    countryName="India"
    def __init__(self,accno,accHolder,balance,branch):
        print(__name__)
        print("constructor is called")
        print("object is getting created ")
        self.accno=accno            #instance variables  self
        self.accHolder=accHolder
        self.balance=balance
        self.branch=branch
    def __del__(self):
         print("Object is getting destroyed")  
    def withdraw(self,withdrawAmount):
        self.dateOfTransaction='23-09-2026'
        self.balance=self.balance-withdrawAmount
        print(f"Hello Mr {self.accHolder} Aftrer Withdrawl updated balance {self.balance}")
    def deposit(self,depositAmount):
        self.balance=self.balance+depositAmount
        print(f"Mr {self.accHolder} After Deposit updated balance",self.balance)
    def balance_enquiry(self):
            print("Hello Mr {self.accHolder}  After Balance : ",self.balance)    

account=BankAccount(100,"sandeep",1000,"Hyderabad")#object creation syntax
account1=BankAccount(101,"suresh",2000,"delhi")#object creation syntax
account.withdraw(200)
account1.withdraw(200)

account.withdraw(100)
account1.deposit(345)
account.idno=123456

print(account.idno,account.balance,account.accHolder,account.dateOfTransaction)
print(account1.countryName)
print(BankAccount.countryName)
print(account1.__dict__)
#car    -->huyndai car,honda car,audi car...
#tree   -->mango tree,banana tree....

if __name__=="__main__":
    #this block only runs when executing 'py calci.py' directly

    print("---running tests inside the BankAccount.py")

class OnlineBankAccount(BankAccount):

     def __init__(self, accno, accHolder, balance, branch):
          super().__init__(accno, accHolder, balance, branch)
             
     def aadhar_otp_linking(self,otp):
        pass 
OAccount=OnlineBankAccount(222,"mahesh",9000,'hyderabad')
OAccount.deposit(2000)     

