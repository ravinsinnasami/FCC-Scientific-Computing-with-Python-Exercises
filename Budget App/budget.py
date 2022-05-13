class Category():

    # initialize Category class

    def __init__(self, category):
        self.category = category
        self.ledger = []
        # variables for methods. instance variables.

        # variables for def deposit
        self.deposit_amount = 0
        self.deposit_description = ''

    # a method to deposit.
    # requires amount, but description is optional
    # appends the amount and description as dictionary into ledger list.
    def deposit(self, amount, description=''):
        self.deposit_amount = amount
        self.deposit_description = description
        self.ledger.append({'amount': self.deposit_amount, 'description': self.deposit_description})



def create_spend_chart(categories):