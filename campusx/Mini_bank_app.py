class Customer:
    """This is developed by Machindra.
    Its a mini bank app"""
    bankname = 'Gpaybank'
    def __init__(self,name,balance=0.0):
        self.name = name
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance+amount
        print('After deposite, balance:',self.balance)
    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds,cannot perform this operation.")
        else:
            self.balance = self.balance-amount
            print("After withdraw, balance is:",self.balance)


print("Welcome to",Customer.bankname)
name = input("Enter your name:")
c = Customer(name)

while True:
    print("d - Deposite \n w - Withdraw \n e - Exit")
    option = input("choose your option:")
    if option.lower() == "d":
        amount = float(input("Enter amount to deosite:"))
        c.deposit(amount)
    elif option.lower() == "w":
        amount = float(input("Enter amount to withdraw:"))
        c.withdraw(amount)
    elif option.lower() == "e":
        print("Thanks for banking")
        break
    else:
        print("Your option is invalide, Please choose valid option")
