import math  # For rounding and percentage calculations


# Step 1: User Input for Transactions
def get_user_transactions():
    transactions = []

    while True:
        # Ask for transaction type
        transaction_type = input("Enter transaction type (income/expense) or 'done' to finish: ").lower()
        if transaction_type == 'done':
            break
        elif transaction_type not in ['income', 'expense']:
            print("Invalid type. Please enter 'income' or 'expense'.")
            continue

        # Ask for transaction amount
        try:
            amount = float(input("Enter the transaction amount: $"))
        except ValueError:
            print("Invalid amount. Please enter a number.")
            continue

        # Ask for transaction description
        description = input("Enter a brief description: ")

        # Add the transaction to the list
        transactions.append({"type": transaction_type, "amount": amount, "description": description})

    return transactions


# Step 2: Categorize Transactions
def categorize_transactions(transactions):
    income_transactions = [t for t in transactions if t["type"] == "income"]
    expense_transactions = [t for t in transactions if t["type"] == "expense"]
    return income_transactions, expense_transactions


# Step 3: Calculate Totals
def calculate_totals(income_transactions, expense_transactions):
    total_income = sum(t["amount"] for t in income_transactions)
    total_expenses = sum(t["amount"] for t in expense_transactions)
    return total_income, total_expenses


# Step 4: Display Financial Health
def display_financial_health(total_income, total_expenses):
    net_savings = round(total_income - total_expenses, 2)
    if total_income > total_expenses:
        print("\nYou have a surplus of ${}".format(net_savings))
    elif total_income < total_expenses:
        print("\nYou are in deficit by ${}".format(abs(net_savings)))
    else:
        print("\nYour income and expenses are balanced.")
    return net_savings


# Step 5: Display Report with Rounded Totals and Percentages
def display_report(income_transactions, expense_transactions, total_income, total_expenses, net_savings):
    print("\nIncome Transactions:")
    for transaction in income_transactions:
        print(f"{transaction['description']}: ${transaction['amount']}")

    print("\nExpense Transactions:")
    for transaction in expense_transactions:
        print(f"{transaction['description']}: ${transaction['amount']}")

    print("\nTotal Income: ${}".format(math.ceil(total_income)))
    print("Total Expenses: ${}".format(math.floor(total_expenses)))
    print("Net Savings: ${}".format(net_savings))

    # Calculate expense percentage relative to income if income is greater than 0
    if total_income > 0:
        expense_percentage = (total_expenses / total_income) * 100
        print("Expenses are {:.2f}% of your income.".format(expense_percentage))


# Main function to run the tool
def main():
    print("Welcome to FinanceFlow!")
    transactions = get_user_transactions()
    income_transactions, expense_transactions = categorize_transactions(transactions)
    total_income, total_expenses = calculate_totals(income_transactions, expense_transactions)
    net_savings = display_financial_health(total_income, total_expenses)
    display_report(income_transactions, expense_transactions, total_income, total_expenses, net_savings)


# Run the tool
main()
