# Calculates the monthly loan payment
def calculate_monthly_payment(loan_amount, annual_interest_rate, years):
    monthly_interest_rate = annual_interest_rate / 12 / 100  # Convert annual rate to monthly
    months = years * 12  # Convert years to months
    monthly_payment = loan_amount * monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** -months)
    return monthly_payment

# Calculates the total payment over the loan term
def calculate_total_payment(monthly_payment, years):
    return monthly_payment * 12 * years  # Total payment is monthly payment times total months

# Calculates the total interest paid on the loan
def calculate_total_interest(total_payment, loan_amount):
    return total_payment - loan_amount  # Total interest is total payment minus loan amount

# Main function to get input, calculate, and display the results
def main():
    loan_amount = float(input("Enter the loan amount: "))
    annual_interest_rate = float(input("Enter the annual interest rate (in %): "))
    years = int(input("Enter the loan term (in years): "))

    # Calculate monthly payment, total payment, and total interest
    monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, years)
    total_payment = calculate_total_payment(monthly_payment, years)
    total_interest = calculate_total_interest(total_payment, loan_amount)

    # Display the results
    print(f"\n--- Loan Repayment Details ---")
    print(f"Monthly Payment: ${monthly_payment:.2f}")
    print(f"Total Payment: ${total_payment:.2f}")
    print(f"Total Interest Paid: ${total_interest:.2f}")

# Run the main function
if __name__ == "__main__":
    main()
