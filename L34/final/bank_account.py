class Bank_Account():
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        self.balance -= amount
    
    def get_balance(self):
        return self.balance

if __name__=='__main__':
    b = Bank_Account('test1',0)
    x = int(input('x> '))
    while x!=0:
        if x>0:
            b.deposit(x)
        else:
            b.withdraw(-x)
        
        print(b.get_balance())
        x = int(input('x> '))
