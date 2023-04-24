from checking_account import *
from savings_account import *

class Bank():

    savings_interest=3.0  // class variable 

    def __init__(self):
        self.accounts=[]  // instance variables
        self.account_counter=0
    
    def print_accounts(self):
        for i in range(len(self.accounts)):
            account = self.accounts[i]
            print(i,account)
    
    def open_account(self,type):
        account="none"
        nickname=type+'-'+str(self.account_counter)
        self.account_counter += 1

        if type=='checking':
            print('opening checking account')
            account=Checking_Account(nickname,0)
        elif type=="savings":
            print('opening savings account') 
            account=Savings_Account(nickname,0,Bank.savings_interest)
        self.accounts.append(account)
        print('opened account',account)
        print('-'*40)

    def get_account(self):
        self.print_accounts()
        account_number=int(input("account: "))
        account = self.accounts[account_number] 
        return account
    
    def get_action(self):
        print("select an action:")
        print("1. deposit")
        print("2. withdraw")
        print("3. transfer")
        print("4. monthly adjustments")
        print("5. show account balances")
        option = int(input("> "))
        return option

    def run_atm(self):
        ''' interact with user '''
        more = 'y'
        while more=='y':
            
            option = self.get_action()          

            if option==1:     
                account = self.get_account()          
                amount = float(input("how much to deposit? "))
                account.deposit(amount)
            elif option == 2:
                account = self.get_account()
                amount = float(input("how much to withraw? "))
                account.withdraw(amount)
            elif option == 3:
                print("account to transfer from: ")
                from_account = self.get_account()
                print("account to transfer to")
                to_account = self.get_account()
                amount = float(input("how much to tranfer? "))
                from_account.withdraw(amount)
                to_account.deposit(amount)
            elif option==4:
                for account in self.accounts:
                    account.adjust()
            elif option==5:
                pass
            self.print_accounts()
            more = input("more? (y or n) ")
    
if __name__=='__main__':
    b = Bank()
    b.open_account('checking')
    b.open_account('savings')
    
    print('-'*40)
    b.run_atm()
