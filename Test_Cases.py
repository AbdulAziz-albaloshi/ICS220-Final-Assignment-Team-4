import re  # For input validation using regular expressions
from Grand_Prix_Classes import *  # [Used from Grand_Prix_Classes.py] — All class, enum, and method definitions

# Create a Fan object with validation
def create_fan():
    print("\n--- Fan Account Creation ---")

    while True:
        fan_name = input("Enter fan_name: ").strip()
        if re.fullmatch(r"[A-Za-z ]+", fan_name):
            break
        else:
            print("Invalid name. Only letters and spaces are allowed.")

    fan_id = input("Enter fan_id: ").strip()

    while True:
        phone_number = input("Enter phone_number (digits only): ").strip()
        if phone_number.isdigit():
            break
        else:
            print("Phone number must be numeric.")

    while True:
        gender = input("Enter gender (Male/Female/Other): ").strip().lower()
        if gender in ["male", "female", "other"]:
            gender_enum = Gender[gender.upper()]  # [Used from Grand_Prix_Classes.py] — Gender Enum
            break
        else:
            print("Invalid gender. Please enter Male, Female, or Other.")

    while True:
        fan_level = input("Enter fan level (Gold/Silver/Bronze): ").strip().capitalize()
        if fan_level in ["Gold", "Silver", "Bronze"]:
            level_enum = FanLevel[fan_level.upper()]  # [Used from Grand_Prix_Classes.py] — FanLevel Enum
            break
        else:
            print("Invalid fan level. Please enter Gold, Silver, or Bronze.")

    while True:
        try:
            fan_points = int(input("Enter loyalty points: "))
            if fan_points < 0:
                raise ValueError
            break
        except ValueError:
            print("Loyalty points must be a non-negative number.")

    return Fan(fan_name, fan_id, int(phone_number), gender_enum, level_enum, fan_points)  # [Used from Grand_Prix_Classes.py] — Creates a Fan object


# Create an Account and add Ticket
def create_account_with_ticket(fan):
    print("\n--- Create Account & Purchase Ticket ---")

    account_id = input("Enter account_id: ").strip()
    creation_date = date.today()  # Auto-assign today's date

    while True:
        discount_elig = input("Is discount eligible? (yes/no): ").strip().lower()
        if discount_elig in ["yes", "no"]:
            discount_enum = DiscountEligibility.ELIGIBLE if discount_elig == "yes" else DiscountEligibility.NOT_ELIGIBLE
            break
        else:
            print("Please enter 'yes' or 'no'.")

    account = Account(account_id, AccountStatus.ACTIVE, creation_date, discount_enum)  # [Used from Grand_Prix_Classes.py] — Creates an Account object

    print("\n--- Ticket Details ---")
    while True:
        ticket_type = input("Enter ticket type (Regular/VIP/Premium): ").strip().lower()
        if ticket_type in ["regular", "vip", "premium"]:
            ticket_enum = TicketType[ticket_type.upper()]  # [Used from Grand_Prix_Classes.py] — TicketType Enum
            break
        else:
            print("Invalid ticket type. Choose Regular, VIP, or Premium.")

    ticket_id = input("Enter ticket_id: ").strip()

    while True:
        try:
            ticket_price = float(input("Enter ticket_price: "))
            if ticket_price < 0:
                raise ValueError
            break
        except ValueError:
            print("Ticket price must be a non-negative number.")

    if discount_enum == DiscountEligibility.ELIGIBLE:
        while True:
            try:
                discounted_amount = float(input("Enter discounted_amount: "))
                if discounted_amount < 0:
                    raise ValueError
                break
            except ValueError:
                print("Discounted amount must be a non-negative number.")
    else:
        discounted_amount = 0.0  # No discount for ineligible users
        print("Discount not applicable. Discounted amount set to 0.0.")

    ticket = Ticket(ticket_enum, ticket_id, ticket_price, discounted_amount)  # [Used from Grand_Prix_Classes.py] — Creates a Ticket object

    print("\n--- Payment Information ---")
    payment_id = input("Enter payment_id: ").strip()

    while True:
        payment_method = input("Enter payment method (Card/Cash/Wallet): ").strip().lower()
        if payment_method in ["card", "cash", "wallet"]:
            payment_enum = PaymentMethod[payment_method.upper()]  # [Used from Grand_Prix_Classes.py] — PaymentMethod Enum
            break
        else:
            print("Invalid method. Choose Card, Cash, or Wallet.")

    payment_date = date.today()  # Auto assign current date
    discount_rate = f"{discounted_amount} off"

    payment = Payment(payment_enum, payment_id, payment_date, discount_rate)  # [Used from Grand_Prix_Classes.py] — Creates a Payment object
    ticket.set_payment(payment)  # [Composition] Payment is part of Ticket

    account.add_ticket(ticket)  # [Aggregation] Account has-a Ticket
    fan.add_account(account)  # [Aggregation] Fan has-a Account

    return account


# Display all fan and account information
def show_fan_summary(fan):
    print("\n--- Fan Summary ---")
    print(fan)  # [Uses __str__() from Grand_Prix_Classes.py] — Fan

    for acc in fan.get_accounts():  # [Aggregation] Fan has-a Account
        print(acc)  # [Uses __str__() from Grand_Prix_Classes.py] — Account
        for ticket in acc.get_tickets():  # [Aggregation] Account has-a Ticket
            print(ticket)  # [Uses __str__() from Grand_Prix_Classes.py] — Ticket
            print(ticket.get_payment())  # [Composition] Ticket has-a Payment


# Run full test sequence
def run_test_case():
    fan = create_fan()
    account = create_account_with_ticket(fan)
    show_fan_summary(fan)


# Entry point
def main():
    print("==== GRAND PRIX SYSTEM TEST ====")
    try:
        run_test_case()
    except Exception as e:
        print(f"An error occurred: {e}")  # Basic error handler
    finally:
        print("\nThank you for using the Grand Prix Ticket System!")  # Always prints


if __name__ == "__main__":
    main()  # Runs the program

