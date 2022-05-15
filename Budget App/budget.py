class Category():

    """Creates a Category Class"""

    def __init__(self, category):
        """ Initializes the variables that are necessary for the class and methods.
             - first initialization is for category naming.
             - second initialization is for creation of ledger list
             - rest is variables for methods.
            """

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


    def deposit(self, amount, description=''):
        """ Method for adding in deposit.
            Amount is required argument but description is optional.
            Both amount and description is appended into the list as a dictionary
            """

        self.deposit_amount = amount
        self.deposit_description = description
        self.ledger.append({'amount': self.deposit_amount, 'description': self.deposit_description})


    def withdraw(self, amount, description=''):
        """  Method for withdrawing funds.
             Amount is required argument but description is optional.
             Check if deposit amount is equal to or larger than withdrawal. Return True or false appropriately.
             """

        self.withdraw_amount = amount
        self.withdraw_description = description
        if self.deposit_amount > self.withdraw_amount:
            self.ledger.append({'amount': -abs(self.withdraw_amount), 'description': self.withdraw_description})
            return True
        else:
            return False


    def get_balance(self):
        """ Method to get balance based on items on the ledger list.
            Sets balance = 0, so that each time it loops through the list it starts at 0.
                - self.balance is not set in def __init__ because if set there, last final value will be used as initial value when checking balance of
                list.
            Returns the final balance value.
            """

        self.balance = 0
        for element in self.ledger:
            self.balance += element['amount']
        self.current_balance = self.balance
        return self.current_balance


    def transfer(self, amount, transfer_category_obj):
        """ Method to transfer funds to another category.
            transfer_category_obj is a class instance. It'll be treated as such without any self.[]
            Check if transfer amount is equal or lower than deposit value. If no, return False. Else:
                - sends info to withdraw method - to remove fund
                - appends into to ledger of the transfer_category_obj
                - returns True
            """

        self.transfer_amount = amount
        if self.deposit_amount > self.transfer_amount:
            self.withdraw(self.transfer_amount, f"Transfer to {transfer_category_obj.category}")
            transfer_category_obj.ledger.append({'amount': self.transfer_amount, 'description': f"Transfer from {self.category}"})
            return True
        else:
            return False


    def check_funds(self, amount):
        """ Method to check balance and compare with given value.
            uses get_balance method to get a value and then compares with given value.
            If balance is more than given value, return True, else return False.
            """

        self.check_funds_amount = amount
        if self.get_balance() >= self.check_funds_amount:
            return True
        else:
            return False

    def __repr__(self):
        """ Method to print a set things when the object is printed.
            creates a variable to store the strings.
                - adds a string containing category, centered
                - loop through the ledger list and prints the description (first 23 chars, left adjusted)
                    and then the amount (right adjust, max 7 characters, 2 decimal points)
                - adds a string with the final total
            returns the final variable
            """

        final_prints = ''
        final_prints += f"{self.category.title().center(30, '*')}\n"
        for element in self.ledger:
            number_to_2dp = str("{:.2f}".format(element['amount']))
            final_prints += f"{element['description'][:23].ljust(23)}{number_to_2dp.rjust(7)}\n"
        final_prints += f"Total: {self.get_balance()}"
        return final_prints


def create_spend_chart(categories):
    """ Create a chart that maps the percentage of expenses spent based on total withdrawal"""

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

    # get the number of spaces and dots required to map the percentage of expenses.
    # sets initial value to 0. Starts at 0 because if % expense = 100%, then no spaces and full of marks.
        # check value for spaces only.
    # appends the number of spaces needed into a list.
    check_spaces_needed = 0
    spaces_needed_for_each_category = []

    for percentage in expenses_in_percentage:
        percentage = float(percentage)

        if percentage == 100.00:
            check_spaces_needed = 0
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 90.00:
            check_spaces_needed = 1
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 80.00:
            check_spaces_needed = 2
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 70.00:
            check_spaces_needed = 3
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 60.00:
            check_spaces_needed = 4
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 50.00:
            check_spaces_needed = 5
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 40.00:
            check_spaces_needed = 6
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 30.00:
            check_spaces_needed = 7
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 20.00:
            check_spaces_needed = 8
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage >= 10.00:
            check_spaces_needed = 9
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage > 0.00:
            check_spaces_needed = 10
            spaces_needed_for_each_category.append(check_spaces_needed)
        elif percentage == 0:
            check_spaces_needed = 11
            spaces_needed_for_each_category.append(check_spaces_needed)

    # prints the spaces and marks based on the check_spaces_needed and appends to a list
    printed_spaces_and_dots = []

    for number in spaces_needed_for_each_category:
        printed_spaces_and_dots.append(f"{' '*number}{'o'*(11-number)}")

    # final variable to be returned.
    final_print = "Percentage spent by category\n"

    # print the percentage followed by spaces and/or marks line by line.
    # for percentage side value
        # printed starting from 100 and decreases by -10 until 0.
        # percentage side value is adjusted using r.just(5)
    # each character of each element in the printed_spaces_and_dots will be printed line after line.
        # each element is accessed using its index e.g. 0,1,2 and the character in the element is accessed using the line_value_increment_counter
    line_value_increment_counter = 0

    for side_value in range (100, -10, -10):
        final_print += f"{str(side_value).rjust(3)}| {printed_spaces_and_dots[0][line_value_increment_counter]}  {printed_spaces_and_dots[1][line_value_increment_counter]}  {printed_spaces_and_dots[2][line_value_increment_counter]}  \n"
        line_value_increment_counter += 1

    # print the dotted line after the percentage and marks.
    # dots are aligned using .rjust(14)
    final_print += ("-"*10).rjust(14) + "\n"

    # following gets the longest word in the list of categories.
    word_length = 0

    for category in categories:
        if len(category.category) > word_length:
            word_length = len(category.category)

    # print the categories vertically.
    # loops using the longest category word
        # if num is 0 as in, if it's the first character, then make it capital.
        # else if, num is the last digit, print the line but without the newline character
        # else, just print the line as it is.

    for number in range(word_length):
        if number == 0:
            final_print += f"{(categories[0].category[number:number + 1]).title().rjust(6)}{(categories[1].category[number:number + 1]).title().rjust(3)}{(categories[2].category[number:number + 1]).title().rjust(3)}  \n"
        elif number == (word_length-1):
            final_print += f"{(categories[0].category[number:number + 1]).rjust(6)}{(categories[1].category[number:number + 1]).rjust(3)}{(categories[2].category[number:number + 1]).rjust(3)}  "
        else:
            final_print += f"{(categories[0].category[number:number + 1]).rjust(6)}{(categories[1].category[number:number + 1]).rjust(3)}{(categories[2].category[number:number + 1]).rjust(3)}  \n"

    # return the final value.
    return final_print
