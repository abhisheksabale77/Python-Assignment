
class BankAccount:
    def __init__(self, name, accno, bal, loan):
        self.name = name
        self.accno = accno
        self.balance = bal
        self.loan = loan

    def deposite(self, amount):
        if amount < 0:
            print("Error")
        else:
            self.balance += amount

    def withdrawl(self, amount):
        if self.balance < amount < 0:
            print("Error")
        else:
            self.balance -= amount

    def printbalance(self):
        print("\n======Bank Account=====\n")
        print(f'Name: {self.name}\nAccount no: {self.accno}\nBalance: {self.balance} \nLoan: {self.loan}')

class Loan(BankAccount):
    def __init__(self, name, accno, bal, loan):
        super().__init__(name,accno,bal,loan)

    def AssignLoan(self, amount):
        if amount > 0:
            self.loan += amount
            print(f"\nAccount Holder {self.name} with Account no {self.accno} has loan of {self.loan} ")

    def LoanList(self):
        if self.loan <= 0:
            print("\nNo loan is taken by the user")
        else:
            print("\n========Loan List=======\nName: ",self.name,"\nAccount: ",self.accno,"\nBalance: ",self.balance,"\nLoan: ",self.loan)

    def __del__(self):
        print("Destructor Called...")
c1 = Loan('Arron', 12345, 50000,0)
while(True):
    print(f'\n\n[+] Bank Operations\n1. Check Balance \n2. Deposite \n3. Withdrawl\n4. AssignLoan \n5. LoanList \n6. Exit')
    ch = int(input("<|>:"))
    if ch == 1:
        c1.printbalance()
    elif ch == 2:
        amount = int(input("Enter Amount: "))
        c1.deposite(amount)
    elif ch == 3:
        amount = int(input("Enter Amount: "))
        c1.withdrawl(amount)
    elif ch == 4:
        amount = int(input("Enter Amount: "))
        c1.AssignLoan(amount)
    elif ch == 5:
        c1.LoanList()
    else:
        exit(0)
