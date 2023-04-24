from bank_account import Bank_Account

class Checking_Account(Bank_Account):
    
    fee=10.00

    def __init__(self,name,balance):
        super().__init__(name,balance);
    
    def __str__(self):
        return f'[checking {self.name} balance:{self.balance}]'

    
    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if amount<= self.balance:
            self.balance -= amount
        else:
            print('insufficient funds!')    
    def get_balance(self):
        return self.balance
    
    def adjust(self):
        ''' process monthly fee '''
        self.balance -= Checking_Account.fee
    
        

if __name__=='__main__':
    b = Checking_Account('test1',0)
    x = int(input('x> '))
    while x!=0:
        if x>0:
            b.deposit(x)
        else:
            b.withdraw(-x)
        b.charge_fee()
        print(b.get_balance())
        x = int(input('x> '))
