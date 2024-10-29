def calculate_compound_interest(principal, rate, years, times_compounded):
    """Calculates the compound interest and returns the final amount after the given period."""
    return principal * (1 + rate / times_compounded) ** (times_compounded * years)

def get_user_input():
    """Gathers user input for principal, rate, years, and times compounded per year."""
    principal = float(input("Enter the initial investment amount: "))
    rate = float(input("Enter the annual interest rate (as a decimal, e.g., 0.05 for 5%): "))
    years = int(input("Enter the number of years: "))
    times_compounded = int(input("Enter the number of times interest is compounded per year: "))
    return principal, rate, years, times_compounded

def display_investment_growth(principal, rate, years, times_compounded):
    """Displays investment growth year by year with a simple text-based visualization."""
    print("\nYearly Growth of Investment:")
    for year in range(1, years + 1):
        amount = calculate_compound_interest(principal, rate, year, times_compounded)
        growth_bar = "=" * int(amount // 100)  # Simple bar visualization for growth
        print(f"Year {year}: ${amount:.2f} {growth_bar}")

def main():
    """Main function to run the program."""
    print("Welcome to the Compound Interest Calculator!")
    principal, rate, years, times_compounded = get_user_input()
    display_investment_growth(principal, rate, years, times_compounded)

if __name__ == "__main__":
    main()
