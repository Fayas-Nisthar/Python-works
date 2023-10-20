class Bank:
    acno:int
    ac_type:str
    balance:int
    bank_name:str="sbi"  #static variable
    def __init__(self,acno,ac_type,balance):
        self.acno=acno
        self.ac_type=ac_type
        self.balance=balance

    def withdraw(self,amount):
        if amount>self.balance:
            print("Transaction declined")
        else:
            self.balance-=amount
            print(f"your {Bank.bank_name} acount debited with amount {amount} avl bal is {self.balance}")

    def deposite(self,amount):
        self.balance+=amount
        print(f"your {Bank.bank_name} acount credited with amount {amount} avl bal is {self.balance}")

    def balance_enq(self):
        print(f"your account balance is{self.balance}")

bank1=Bank(1234,"savings",10000)
bank1.withdraw(2000)
bank1.deposite(5000)
bank1.balance_enq()

bank2=Bank(9876,"current",50000)
bank2.withdraw(25000)
# bank2.balance_enq()
