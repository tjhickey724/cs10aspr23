from bank_account import Bank_Account

class Savings_Account(Bank_Account):
    def __init__(self,name,balance,interest=3):
        self.interest=interest
        super().__init__(name,balance);
    
    def __str__(self):
        return f'[saving {self.name} balance:{self.balance} interest:{self.interest}]'
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        self.balance -= amount  
    
    def get_balance(self):
        return self.balance
    
    def adjust(self):
        self.balance += (self.interest/100/12)*self.balance
    

if __name__=='__main__':
    b = Savings_Account('test1',0,4.5)
    x = float(input('x> '))
    while x!=0:
        
        if x>0:
            b.deposit(x)
        else:
            b.withdraw(-x) 
        b.pay_interest()   
        print("%10.2f"%(b.get_balance(),))
        x = float(input('x> '))
