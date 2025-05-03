from enum import Enum
from datetime import date

# ENUMS
class Gender(Enum):
    """Class to represent Enumeration of available genders."""
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

class FanLevel(Enum):
    """Class to represent Enumeration of fan levels."""
    BRONZE = "Bronze"
    SILVER = "Silver"
    GOLD = "Gold"

class TicketType(Enum):
    """Class to represent Enumeration of ticket types."""
    REGULAR = "Regular"
    VIP = "VIP"
    PREMIUM = "Premium"

class PaymentMethod(Enum):
    """Class to represent Enumeration of payment methods."""
    CARD = "Card"
    CASH = "Cash"
    WALLET = "Wallet"

class AccountStatus(Enum):
    """Class to represent Enumeration of account statuses."""
    ACTIVE = "Active"
    INACTIVE = "Inactive"

class DiscountEligibility(Enum):
    """Class to represent Enumeration of discount eligibility."""
    ELIGIBLE = "Eligible"
    NOT_ELIGIBLE = "Not Eligible"


# User Class
class User:
    """Class to represent a generic system user"""

    # Constructor (protected attributes due to being a parent in an inheritance relationship)
    def __init__(self, user_name: str, user_id: str, phone_number: int, user_gender: Gender):
        self._user_name = user_name
        self._user_id = user_id
        self._phone_number = phone_number
        self._user_gender = user_gender

    # Setter / Getter
    def set_user_name(self, user_name=""):
        self._user_name = user_name
    def get_user_name(self):
        return self._user_name

    def set_user_id(self, user_id=""):
        self._user_id = user_id
    def get_user_id(self):
        return self._user_id

    def set_phone_number(self, phone_number=0):
        self._phone_number = phone_number
    def get_phone_number(self):
        return self._phone_number

    def set_user_gender(self, user_gender=Gender.OTHER):
        self._user_gender = user_gender
    def get_user_gender(self):
        return self._user_gender

    # Display user information
    def display_user_info(self):
        print(self.__str__())

    # String representation of the User class
    def __str__(self):
        return f"User[ID: {self._user_id}, Name: {self._user_name}, Phone: {self._phone_number}, Gender: {self._user_gender.value}]"


# Fan Class
class Fan(User):
    """Class to represent a fan user (Inherits User)"""

    # Constructor (private attributes)
    def __init__(self, user_name, user_id, phone_number, user_gender, fan_level: FanLevel, fan_points: int):
        super().__init__(user_name, user_id, phone_number, user_gender)  # Inheritance relation with User
        self.__fan_level = fan_level
        self.__fan_points = fan_points
        self.__accounts = []  # Aggregation relation with Account

    # Setter / Getter
    def set_fan_level(self, fan_level=FanLevel.BRONZE):
        self.__fan_level = fan_level
    def get_fan_level(self):
        return self.__fan_level

    def set_fan_points(self, fan_points=0):
        self.__fan_points = fan_points
    def get_fan_points(self):
        return self.__fan_points

    # Return current points
    def check_points(self):
        return self.__fan_points

    # Return fan tier and points
    def view_status(self):
        return f"{self.__fan_level.value} with {self.__fan_points} points"

    # Manage related accounts (aggregation)
    def add_account(self, account):
        self.__accounts.append(account)
    def get_accounts(self):
        return self.__accounts

    # String representation of the Fan class
    def __str__(self):
        return f"{super().__str__()}, Fan Level: {self.__fan_level.value}, Points: {self.__fan_points}"


# Account Class
class Account:
    """Class to represent a fan account"""

    # Constructor (private attributes)
    def __init__(self, account_id: str, account_status: AccountStatus, creation_date: date, discount_eligibility: DiscountEligibility):
        self.__account_id = account_id
        self.__account_status = account_status
        self.__creation_date = creation_date
        self.__discount_eligibility = discount_eligibility
        self.__tickets = []  # Aggregation relation with Ticket

    # Setter / Getter
    def set_account_id(self, account_id=""):
        self.__account_id = account_id
    def get_account_id(self):
        return self.__account_id

    def set_account_status(self, account_status=AccountStatus.ACTIVE):
        self.__account_status = account_status
    def get_account_status(self):
        return self.__account_status

    def set_creation_date(self, creation_date=date.today()):
        self.__creation_date = creation_date
    def get_creation_date(self):
        return self.__creation_date

    def set_discount_eligibility(self, discount_eligibility=DiscountEligibility.NOT_ELIGIBLE):
        self.__discount_eligibility = discount_eligibility
    def get_discount_eligibility(self):
        return self.__discount_eligibility

    # Manage related tickets (aggregation)
    def add_ticket(self, ticket):
        self.__tickets.append(ticket)
    def get_tickets(self):
        return self.__tickets

    # Display account information
    def display_account_info(self):
        print(self.__str__())

    # String representation of the Account class
    def __str__(self):
        return f"Account[ID: {self.__account_id}, Status: {self.__account_status.value}, Created: {self.__creation_date}, Discount: {self.__discount_eligibility.value}]"


# Ticket Class
class Ticket:
    """Class to represent a ticket"""

    # Constructor (private attributes)
    def __init__(self, ticket_type: TicketType, ticket_id: str, ticket_price: float, discounted_amount: float):
        self.__ticket_type = ticket_type
        self.__ticket_id = ticket_id
        self.__ticket_price = ticket_price
        self.__discounted_amount = discounted_amount
        self.__payment = None  # Composition relation with Payment

    # Setter / Getter
    def set_ticket_type(self, ticket_type=TicketType.REGULAR):
        self.__ticket_type = ticket_type
    def get_ticket_type(self):
        return self.__ticket_type

    def set_ticket_id(self, ticket_id=""):
        self.__ticket_id = ticket_id
    def get_ticket_id(self):
        return self.__ticket_id

    def set_ticket_price(self, ticket_price=0.0):
        self.__ticket_price = ticket_price
    def get_ticket_price(self):
        return self.__ticket_price

    def set_discounted_amount(self, discounted_amount=0.0):
        self.__discounted_amount = discounted_amount
    def get_discounted_amount(self):
        return self.__discounted_amount

    # Manage payment (composition)
    def set_payment(self, payment):
        self.__payment = payment
    def get_payment(self):
        return self.__payment

    # Display ticket information
    def display_ticket_info(self):
        print(self.__str__())

    # String representation of the Ticket class
    def __str__(self):
        return f"Ticket[ID: {self.__ticket_id}, Type: {self.__ticket_type.value}, Price: {self.__ticket_price}, Discounted: {self.__discounted_amount}]"


# Payment Class
class Payment:
    """Class to represent a payment (Part-of Ticket)"""

    # Constructor (private attributes)
    def __init__(self, payment_method: PaymentMethod, payment_id: str, payment_date: date, discount_rate: str):
        self.__payment_method = payment_method
        self.__payment_id = payment_id
        self.__payment_date = payment_date
        self.__discount_rate = discount_rate

    # Setter / Getter
    def set_payment_method(self, payment_method=PaymentMethod.CARD):
        self.__payment_method = payment_method
    def get_payment_method(self):
        return self.__payment_method

    def set_payment_id(self, payment_id=""):
        self.__payment_id = payment_id
    def get_payment_id(self):
        return self.__payment_id

    def set_payment_date(self, payment_date=date.today()):
        self.__payment_date = payment_date
    def get_payment_date(self):
        return self.__payment_date

    def set_discount_rate(self, discount_rate=""):
        self.__discount_rate = discount_rate
    def get_discount_rate(self):
        return self.__discount_rate

    # Display payment information
    def view_payment_details(self):
        print(self.__str__())

    # String representation of the Payment class
    def __str__(self):
        return f"Payment[ID: {self.__payment_id}, Method: {self.__payment_method.value}, Date: {self.__payment_date}, Discount Rate: {self.__discount_rate}]"

