# Python program to create Bankaccount class
class Bank_Account:

  def __init__(self):
    self.balance = 0
    print("Bank Account is 2324543098575")

  def deposit(self):
    amount = float(input("Enter amount to be Deposited: "))
    self.balance += amount
    print("\n Amount Deposited:", amount)

  def withdraw(self):
    amount = float(input("Enter amount to be Withdrawn: "))
    if self.balance >= amount:
      self.balance -= amount
      print("\n You Withdrew:", amount)
    else:
      print("\n Insufficient balance  ")

  def display(self):
    print("\n Net Available Balance=", self.balance)


# Driver code

# creating an object of class
s = Bank_Account()

# Calling functions with that class object
s.deposit()
s.withdraw()
s.display()
