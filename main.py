class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f"{self.name:*^30}\n"
        items = "".join(
            f"{item['description'][:23]:23}{item['amount']:7.2f}\n" for item in self.ledger)
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def check_funds(self, amount):
        return self.get_balance() >= amount

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False


def create_spend_chart(categories):
    total_spent = sum(-item["amount"]
                      for category in categories for item in category.ledger if item["amount"] < 0)
    percentages = [(-sum(item["amount"] for item in category.ledger if item["amount"]
                    < 0) / total_spent) * 100 for category in categories]

    chart = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        chart += f"{i:>3}| "
        for percentage in percentages:
            chart += "o  " if percentage >= i else "   "
        chart += "\n"

    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"
    max_length = max(len(category.name) for category in categories)
    for i in range(max_length):
        chart += "     "
        for category in categories:
            chart += f"{category.name[i] if i < len(category.name) else ' '}  "
        chart += "\n"

    return chart.rstrip('\n')
