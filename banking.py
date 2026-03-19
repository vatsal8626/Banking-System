class Bank:
    transactions = []
    def __init__(self, acc_no, balance=0):
        self.acc_no = acc_no
        self.balance = balance
    
    def deposit(self, amt):
        if amt>0:
            self.balance += amt
            self.transactions.append(f'Deposited {amt}')
            print(f'{amt} deposited')
        else:
            print("Invalid amount")
    
    def withdraw(self, amt):
        if amt>0:
            self.balance -= amt
            self.transactions.append(f'Withdraw {amt}')
            print(f'{amt} withdrawn')
        else:
            print('invalid amount')
            
    def check_transactions(self):
        print('transactions: ')
        for i in self.transactions:
            print(i)
            
    def check_balance(self):
        print(f'Total balance: {self.balance}')
            

no = input("Enter account number: ")
acc = Bank(no, 0)

while True:
    print("bank menu")
    print("1. deposit")
    print("2. withdraw")
    print("3. transaction history")
    print("4. balance")
    print("5. exit")
    
    choice = int(input("enter choice: "))
    
    if choice==1:
        amt = float(input(("enter amount: ")))
        acc.deposit(amt)
    elif choice==2:
        amt = float(input(("enter amount: ")))
        acc.withdraw(amt)
    elif choice==3:
        acc.check_transactions()
    elif choice==4:
        acc.check_balance()
    elif choice==5:
        print("bye")
        break
    else:
        print("invalid choice")