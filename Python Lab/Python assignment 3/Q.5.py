class Bank:
    def __init__(self):
        self.account={}

    def create_account(self,account_number,initial_balance=0):
        if account_number not in self.account:
            self.account[account_number] = initial_balance
            print(f"Account created successfully.\nYour Account Number : {account_number}\nCurrent Balance : {initial_balance}")
        else:
            print(f"Account with {account_number} already exists.")
        print()

    def deposit(self,account_number,amount):
        if account_number in self.account:
            self.account[account_number]+=amount
            print(f"Deposited {amount} in account {account_number}\nCurrent Balance : {self.account[account_number]}")
        else:
            print(f"Account with {account_number} does not exists.")
        print()

    def withdraw(self,account_number,amount):
        if account_number in self.account:
            if self.account[account_number]>=amount:
                self.account[account_number]-=amount
                print(f"Withdraw {amount} from account {account_number}\nCurrent Balance : {self.account[account_number]}")
            else:
                print("ERROR :- Insufficient Balance")
        else:
            print(f"Account with {account_number} does not exists.")
        print()

    def check_balance(self,account_number):
        if account_number in self.account:
            print(f"Current Balance : {self.account[account_number]}")
        else:
            print(f"Account with {account_number} does not exists.")
        print()

                       
if __name__=="__main__":
    bank=Bank()
    print("\n\''' WELCOME TO THE BANKING TRANSACTIONS PORTAL \'''")
    while True:
        try:
            print("\nPress 1 to Create Account.\nPress 2 to Deposit amount.\nPress 3 to Withdraw amount.\nPress 4 to Check Balance.\nPress 5 to Exit.")
            choice=int(input("\nEnter your choice (1-5) : "))
        except:
            print("\nERROR :- Plesae enter a valid numeric value.")
        else:
            if choice==1:
                account_number = input("\nEnter Account Number : ")
                while True:
                    try:
                        initial_balance = float(input("Enter initial balance : "))
                        bank.create_account(account_number,initial_balance)
                        break
                    except:
                        print("\nERROR :- Please enter a valid amount.")

            elif choice==2:
                account_number = input("\nEnter Account Number : ")
                while True:
                    try:    
                        amount = float(input("Enter deposit amount : "))
                        bank.deposit(account_number,amount)
                        break
                    except:
                        print("\nERROR :- Please enter a valid amount.")

            elif choice==3:
                account_number = input("\nEnter Account Number : ")
                while True:    
                    try:        
                        amount = float(input("Enter withdraw amount : "))
                        bank.withdraw(account_number,amount)
                        break
                    except:
                        print("\nERROR :- Please enter a valid amount.")

            elif choice==4:
                account_number = input("\nEnter Account Number : ")
                bank.check_balance(account_number)

            elif choice==5:
                print("\nExiting the program....")
                break
            
            else:
                print("\nInvalid choice. please enter a number between 1 to 5.\n")
