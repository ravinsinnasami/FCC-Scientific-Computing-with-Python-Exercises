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

        # variable for def transfer
        self.transfer_amount = 0

        # variable for def check_funds
        self.check_funds_amount = 0


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
        self.balance = 0
        for element in self.ledger:
            self.balance += element['amount']
        self.current_balance = self.balance
        return self.current_balance

    # method to transfer funds.
    # transfer_category_obj is another instance
    # check if there is enough deposit to do transfer. if unable, return False. Else:
        # send info to withdraw method
        # append info to transfer_category_obj ledger
        # return True
    def transfer(self, amount, transfer_category_obj):
        self.transfer_amount = amount
        if self.deposit_amount > self.transfer_amount:
            self.withdraw(self.transfer_amount, f"Transfer to {transfer_category_obj.category}")
            transfer_category_obj.ledger.append({'amount': self.transfer_amount, 'description': f"Transfer from {self.category}"})
            return True
        else:
            return False

    # method to check balance
    # get balance from def get_balance and compare against given value.
    # if balance is more or equal to amount, return True. Else, return False.
    def check_funds(self, amount):
        self.check_funds_amount = amount
        if self.get_balance() >= self.check_funds_amount:
            return True
        else:
            return False

    # method to print the instance
    # each print is appended or concatenated to the final_print variable which is then returned.
    def __repr__(self):
        final_prints = ''
        final_prints += f"{self.category.title().center(30, '*')}\n"
        for element in self.ledger:
            number_to_2dp = str("{:.2f}".format(element['amount']))
            final_prints += f"{element['description'][:23].ljust(23)}{number_to_2dp.rjust(7)}\n"
        final_prints += f"Total: {self.get_balance()}"
        return final_prints


def create_spend_chart(categories):
    # Create a chart that maps the percentage of expenses spent based on total withdrawal

    # get the total expense spent [sum of all the categories]
    total_expense = 0

    for category in categories:
        total_expense += category.withdraw_amount

    # get the percentage of expenses spent based on total expense
    # appends the percentage of each category to a list.
    expenses_in_percentage = []

    for category in categories:
        percentage_spent = "{:.2f}".format((category.withdraw_amount/total_expense)*100)
        expenses_in_percentage.append(percentage_spent)