# Budget App

This is my second Python certification project from freecodecamp.org.

A lightweight and interactive Python budget management application that allows users to create custom budget categories, track a financial ledger of transactions (deposits, withdrawals, and transfers), and generate a visual bar chart summarizing category expenditures. 

## Features

- **Custom Budget Categories:** Instantiate categories such as `Food`, `Clothing`, `Entertainment`, and more.
- **Ledger Tracking:** Automatic transaction logging containing amounts and explicit descriptions.
- **Smart Fund Checking:** Safety checks to ensure over-drafting or invalid withdrawals/transfers cannot happen.
- **Formated Financial Printing:** Printing a category object yields a clean, formatted receipt containing item descriptions, aligned values, and the current net balance.
- **Spend Visualization Chart:** Generates an ASCII bar chart depicting the percentage of spending allocated across different categories to understand habits at a glance.

## Class Specification: `Category`

The `Category` class handles the logic for a single budget domain.

### Methods

1. **`deposit(amount, description="")`**
   Appends a deposit object to the ledger list in the format: `{"amount": amount, "description": description}`.
   
2. **`withdraw(amount, description="")`**
   If there are enough funds, a negative amount is added to the ledger. Returns `True` if the transaction succeeded, and `False` otherwise.
   
3. **`get_balance()`**
   Returns the current balance of the budget category based on deposits and withdrawals.
   
4. **`transfer(amount, category)`**
   Transfers a specified amount from the current category to another category. Logs corresponding withdrawal and deposit descriptions and returns `True` if successful.
   
5. **`check_funds(amount)`**
   A helper method that returns `True` if the category balance is greater than or equal to the passed amount, and `False` otherwise.

### String representation (`__str__`)
Printing the class instance returns a beautifully formatted output:
* A title line of 30 characters with the category name centered inside asterisks (`*`).
* A list of items in the ledger showing the description (up to 23 characters) and amount right-aligned with 2 decimal places.
* A final line showing the category total balance.

---

## Usage Example

from budget import Category, create_spend_chart

### Create instances of budget categories
food = Category("Food")
clothing = Category("Clothing")
auto = Category("Auto")

### Perform financial transactions
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food")

clothing.deposit(500, "initial deposit")
food.transfer(50, clothing)
clothing.withdraw(25.55, "t-shirt")

### Check Category Print Representation
print(food)
print(clothing)

### Generate Spend Summary Chart
print(create_spend_chart([food, clothing, auto]))

## Example Console Output

### Category Receipt:

*************Food*************
initial deposit        1000.00
groceries                -10.15
restaurant and more fo   -15.89
Transfer to Clothing     -50.00
Total: 923.96

### Spend Chart:

Percentage spent by category
100|          
 90|          
 80|          
 70|          
 60|          
 50|          
 40|          
 30|          
 20|          
 10|    o    o    
  0|    o    o    o  
    ----------
        F    C    A  
        o    l    u  
        o    o    t  
        d    t    o  
             h       
             i       
             n       
             g
