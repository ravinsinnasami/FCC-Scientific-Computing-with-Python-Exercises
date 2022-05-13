class Category():

    # initialize Category class

    def __init__(self, category):
        self.category = category
        self.ledger = []
        # variables for methods. instance variables.

        # variables for def deposit
        self.deposit_amount = 0
        self.deposit_description = ''

        # variable for def withdraw
        self.withdraw_amount = 0
        self.withdraw_description = ''

        # variable for def get_balance
        self.balance = 0

    # a method to deposit.
    # requires amount, but description is optional
    # appends the amount and description as dictionary into ledger list.
    def deposit(self, amount, description=''):
        self.deposit_amount = amount
        self.deposit_description = description
        self.ledger.append({'amount': self.deposit_amount, 'description': self.deposit_description})

    # method to withdraw
    # requires amount but description is optional.
    # check if deposit amount is more than withdrawal amount, if yes, append to ledger and returns True. Else, return False.
    def withdraw(self, amount, description=''):
        self.withdraw_amount = amount
        self.withdraw_description = description
        if self.deposit_amount > self.withdraw_amount:
            self.ledger.append({'amount': -abs(self.withdraw_amount), 'description': self.withdraw_description})
            return True
        else:
            return False

    # method to get balance
    # loop through every element in ledger list. Now the element is a dictionary. So the amount value is accessed used the key.
    # each time the value is obtained from ledger, it is added to the balance variable.
    # lastly, return balance variable.
    def get_balance(self):
        for element in self.ledger:
            self.balance += element['amount']
        return self.balance



def create_spend_chart(categories):