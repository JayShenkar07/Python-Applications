class HDFC:
    ROI=9.5   #class variable (It is same for all the objects)

    def __init__(self, name, amount):    #__init__ method gets called automatically as soon as objet gets called
        self.balance=amount     #Instace variable
        self.AccountHolder=name  #Instace variable
        print("Welcome ",self.AccountHolder)
        print("Account has been succesfully created with inital balance: ",self.balance)

    def DisplayBalance(self):   #Instance Method
        print("Dear",self.AccountHolder)
        print("Your account balance is : ",self.balance)    

    def withdrawal(self,amount):    #Instance Method
        if(self.balance<amount):
            print("There is no sufficient balance to withdraw: ")
        else:
            self.balance=self.balance-amount
            print("Amount withdrawed succesfully..")

    def deposit(self,amount):    #Instance Method       
        self.balance=self.balance+amount
        print("Amount has been deposited ")

    @classmethod    #decorator (To seperate out from other methods)
    def DisplayBankInfo(cls):   #class method
        print("Welcome to HDFC Bank Portal ")
        print("We are family")
        print("We provide the rate of intrest on savings account is ",cls.ROI)   #Accessing the class variable  using cls.
#Class method should access the class varible


    @staticmethod    #decorator(annotations in JAVA)
    def DisplayKYCinfo():   #(it is not allowed to access any other content from class)
            print("According to the rules of RBI you must provide the below documents to complete the KYC")
            print(" Adhaar Card")   
            print(" PAN")
            print(" Passport Photo") 
            print("-----",HDFC.ROI)



def main():

#Common things which are for eveyone we do it with class method 
#User specific operations are to be done with instance method

    HDFC.DisplayBankInfo()  #Wihtout creating the object of the class we can access class method
    print()

    HDFC.DisplayKYCinfo()

    print()

    print("Rate Of Intrest of HDFC BANK is", HDFC.ROI) #Wihtout creating the object of the class we can access class varible
    print()
    #(We are passing the initial account balance as the only parameter)
    print("Creating new account")
    obj1 = HDFC("Piyush",5000)   #Object1  __init__(100,5000)   100->address of our object1
    print("Creating new account")
    obj2 = HDFC("Jay",3000)    #Object2    __init__(200,3000)  200->address of our object2
    
    obj1.deposit(7000)
    obj1.DisplayBalance()

    obj1.withdrawal(11000)
    obj1.withdrawal(1500)

    obj2.deposit(50000)


    


if __name__=="__main__":
    main()    


# Instance varibles
#     account holder name
#     amount

# Instance methods  (Powerfull as it can access anything)
#     deposit
#     withdraw
#     display balance

# (Instance method should access the instance variables )

# Class variable
#    ROI 

# Class method (Cannot access an instance variables)
#     Display bank Info
# Class method should be called only with the class name like  HDFC.displayBankInfo


# Static Method (This method is different)
#   DisplayKYCdetails 