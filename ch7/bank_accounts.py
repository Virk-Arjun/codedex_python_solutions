class BankAccount: 
  def __init__(self, first_name, last_name, account_id, account_type, pin, balance): 
    self.first_name = first_name 
    self.last_name = last_name 
    self.account_id = account_id 
    self.account_type = account_type 
    self.pin = pin 
    self.balance = balance
  def deposit (self, amount): 
    self.balance += amount
    print("You have deposited $" + str(amount))
  def withdraw (self, amount): 
    self.balance -= amount
    print("You have withdrawn $" + str(amount))
  def display_balance (self):  
    print("Your total balance is $" + str(self.balance)) 
  
example = BankAccount ('Anjali', 'Virk', 1099, 'Checking', 1919, 10000)
example.deposit(96) 
example.withdraw(25) 
example.display_balance() 
