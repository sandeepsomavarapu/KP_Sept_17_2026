class BankAccount:
    countryName="India"
    count =0  #static variable
    def __init__(self,accno,accHolder,balance):
        BankAccount.count=BankAccount.count+1
        print(__name__)
        print("constructor is called")
        print("object is getting created ")
        self.accno=accno            #instance variables  self
        self.accHolder=accHolder
        self.balance=balance
    def __del__(self):
         print("Object is getting destroyed")  
    @staticmethod     
    def utility_method():
         print("utility logic")     
    @classmethod
    def info(cls):
        print("from class method objects count is :",cls.count)
        BankAccount.branch="hyderabad"#static variable

    def withdraw(self,withdrawAmount):
        self.dateOfTransaction='23-09-2026'
        self.balance=self.balance-withdrawAmount
        print(f"Hello Mr {self.accHolder} Aftrer Withdrawl updated balance {self.balance}")
    def deposit(self,depositAmount):
        self.balance=self.balance+depositAmount
        print(f"Mr {self.accHolder} After Deposit updated balance",self.balance)
        # self.balance_enquiry()
    def balance_enquiry(self):
            print(f"Hello Mr {self.accHolder}  Balance : ",self.balance)    

  
account=BankAccount(100,"sandeep",1000)#object creation syntax
account1=BankAccount(101,"suresh",2000)#object creation syntax
account.withdraw(200)
print(account)


account1.withdraw(200)
print(account.__dict__)

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
     count=123
     def __init__(self, accno, accHolder, balance):
          super().__init__(accno, accHolder, balance)
     def __str__(self):
          return "after overriding str...."
     def aadhar_otp_linking(self,otp):
        
        pass 
     def balance_enquiry(self):
            super().balance_enquiry()
            print(super().count)
            print(OnlineBankAccount.count)
            print(f"Hi Mr {self.accHolder}  Balance : ",self.balance)    
     
OAccount=OnlineBankAccount(222,"mahesh",9000)
OAccount.deposit(2000)     
OAccount.balance_enquiry()
print(OAccount.count)
print("Object Info:",OAccount)

BankAccount.info()
print("Branch",BankAccount.branch)

# class C(BankAccount,OnlineBankAccount):#multiple Inheritance
#      pass

# class C(BankAccount):#Hirarchie level Inheritance
#      pass

# class C(OnlineBankAccount):#multilevel Inheritance
#      pass