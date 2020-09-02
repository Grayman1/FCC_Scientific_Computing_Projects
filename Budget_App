# WORKING VERSION - Initial Data Processing


# create Category class
class Category:
    # Construct instance variable ledger - list[]
    def __init__(self, name):
        self.name = name
        self.ledger = []

    # Construct deposit method - - dictionary format with arguments {amount, description}
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    # Construct withdrawl method - - dictionary format with arguments {amount, description}
    # Bool - return True if withdrawl took place; otherwise False
    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    # Construct transfer method - - dictionary format with arguments {amount, budget category}
    # Descriptions to describe origination and destination categories.
    #Cancel if insufficient funds
    # Bool - return True if transfer took place; otherwise False
    def transfer(self, amount, category):
        funds = self.check_funds(amount)
        if funds == True:
            transfer_cat = Category(category).name
            self.withdraw(
                amount, description='Transfer to ' + transfer_cat.name)
            transfer_cat.deposit(
                amount, description='Transfer from ' + self.name)
            return True
        else:
            return False

    # Construct get balance method based on deposits and withdrawls have occurred
    # list element format with arguments {amount}
    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    # Construct check funds method - - list element format with arguments {amount, description}
    # Bool - return True if sufficient funds after transaction; otherwise False
    def check_funds(self, amount):
        funds = 0
        for elem in self.ledger:
            funds += elem['amount']
        if funds >= amount:
            return True
        else:
            return False

    # Construct printing method - - tabulation of transactions, subtotals by category, overall total
    # formatting requirement: 1) title line of 30 characters where category name is centered;
    # padded with '*' characters. 2.a) A list of lines in the ledger; b) display 1st 23
    #characters,then amount; c) amount should be right aligned; d) amount contains 2 DP's;
    # e) amount maximum of 7 characters. 3) line displaying category total.
    #
    def __str__(self):
        output = "{:*^30s}\n".format(self.name)
        for elem in self.ledger:
            amt = ("{:>{width}.2f}".format(elem['amount'], width=7))
            desc = '{:23}'.format(elem['description'][:23])
            line = f"{desc}{amt}\n"
            output += line
        output += 'Total: ' + str(self.get_balance())

        return output


# create spend chart function
def create_spend_chart(categories):
    category_names = []
    cat_spent = []
    spent_percentages = []

    # Generate category labels, subtotals
    for cat in categories:
        total = 0
        for item in cat.ledger:
            if item['amount'] < 0:
                total -= item['amount']
        cat_spent.append(round(total, 2))
        category_names.append(cat.name)
    
    # Calculate % spend by category
    for amount in cat_spent:
        spent_percentages.append(round(amount / sum(cat_spent), 2) * 100)
    
    # Initialize graph string - Graph Title
    graph = "Percentage spent by category\n"

    # Initialize graph y-scale limits, increments
    y_labels = range(100, -10, -10)
    
    # Build bar chart main body - append increments, vertical bars
    # and data symbols, padded blank spaces
   
    for y_inc in y_labels:
        graph += str(y_inc).rjust(3) + "| "
        for percent in spent_percentages:
            if percent >= y_inc:
                graph += "o  "
            else:
                graph += "   "
        graph += "\n"

    # Add x-category dashed lines to string
    graph += "    ----" + ("---" * (len(category_names) - 1))
    graph += "\n     "

    # Find longest category name
    longest_name_length = 0
    for name in category_names:
        if longest_name_length < len(name):
            longest_name_length = len(name)
    
    # Build vertical names; add to graph string
    for i in range(longest_name_length):
        for name in category_names:
            if len(name) > i:
                graph += name[i] + "  "
            else:
                graph += "   "
        if i < longest_name_length - 1:
            graph += "\n     "

    return graph
