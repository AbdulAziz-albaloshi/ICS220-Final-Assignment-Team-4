
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import date
from Grand_Prix_Classes import *  # Import class definitions
from Grand_Prix_Pickling import save_users_to_file, load_users_from_file  # Import pickling functions


# Main Application Class for the GUI
class GrandPrixApp:
    # Constructor to initialize the GUI application
    def __init__(self, root):
        self.root = root
        self.root.title("Grand Prix Ticket Management System")
        self.root.geometry("600x400")
        self.current_user = None  # Stores the currently logged-in Fan

        # Load existing users from file at startup
        self.users = load_users_from_file()

        # Launch main menu
        self.create_main_menu()

    # Displays the main menu screen
    def create_main_menu(self):
        self.clear_window()

        title = tk.Label(self.root, text="Welcome to the Grand Prix Ticket System", font=("Arial", 16))
        title.pack(pady=20)

        btn_register = tk.Button(self.root, text="Create Account", width=25, command=self.create_account_screen)
        btn_login = tk.Button(self.root, text="Login", width=25, command=self.login_screen)
        btn_exit = tk.Button(self.root, text="Exit", width=25, command=self.root.quit)

        btn_register.pack(pady=5)
        btn_login.pack(pady=5)
        btn_exit.pack(pady=5)

    # Displays the account registration form
    def create_account_screen(self):
        self.clear_window()

        title = tk.Label(self.root, text="Create New Fan Account", font=("Arial", 14))
        title.pack(pady=10)

        tk.Label(self.root, text="Name").pack()
        entry_name = tk.Entry(self.root)
        entry_name.pack()

        tk.Label(self.root, text="User ID").pack()
        entry_userid = tk.Entry(self.root)
        entry_userid.pack()

        tk.Label(self.root, text="Phone Number").pack()
        entry_phone = tk.Entry(self.root)
        entry_phone.pack()

        tk.Label(self.root, text="Gender").pack()
        gender_cb = ttk.Combobox(self.root, values=[g.value for g in Gender])
        gender_cb.pack()

        # Sub-function to handle registration logic
        def register_user():
            name = entry_name.get()
            uid = entry_userid.get()
            phone = entry_phone.get()
            gender_val = gender_cb.get()

            # Check if all fields are filled
            if not all([name, uid, phone, gender_val]):
                messagebox.showerror("Input Error", "All fields are required.")
                return

            # Check if phone number is numeric
            if not phone.isdigit():
                messagebox.showerror("Input Error", "Phone number must contain digits only.")
                return

            # Check if user already exists
            if uid in self.users:
                messagebox.showwarning("Exists", "User ID already exists.")
                return

            # Create new fan and store in users
            fan = Fan(name, uid, int(phone), Gender(gender_val), FanLevel.BRONZE, 0)
            self.users[uid] = fan

            # Save updated user dictionary to binary file
            save_users_to_file(self.users)

            messagebox.showinfo("Success", "Account created successfully.")
            self.create_main_menu()

        tk.Button(self.root, text="Register", command=register_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    # Displays the login screen
    def login_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Login", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text="User ID").pack()
        entry_userid = tk.Entry(self.root)
        entry_userid.pack()

        # Sub-function to validate login credentials
        def login_user():
            uid = entry_userid.get()

            # Check if user ID exists
            if uid in self.users:
                self.current_user = self.users[uid]
                self.dashboard_screen()
            else:
                messagebox.showerror("Login Failed", "User not found.")

        tk.Button(self.root, text="Login", command=login_user).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.create_main_menu).pack()

    # Displays the dashboard after successful login
    def dashboard_screen(self):
        self.clear_window()

        tk.Label(self.root, text=f"Welcome, {self.current_user.get_user_name()}", font=("Arial", 14)).pack(pady=10)

        tk.Button(self.root, text="Purchase Ticket", command=self.ticket_purchase_screen).pack(pady=5)
        tk.Button(self.root, text="View Profile", command=self.view_profile).pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.logout).pack(pady=20)

    # Displays the ticket purchasing screen
    def ticket_purchase_screen(self):
        self.clear_window()

        tk.Label(self.root, text="Buy Ticket", font=("Arial", 14)).pack(pady=10)

        tk.Label(self.root, text="Ticket Type").pack()
        ticket_type_cb = ttk.Combobox(self.root, values=[t.value for t in TicketType])
        ticket_type_cb.pack()

        tk.Label(self.root, text="Ticket Price").pack()
        entry_price = tk.Entry(self.root)
        entry_price.pack()

        tk.Label(self.root, text="Discounted Amount").pack()
        entry_discount = tk.Entry(self.root)
        entry_discount.pack()

        tk.Label(self.root, text="Payment Method").pack()
        payment_method_cb = ttk.Combobox(self.root, values=[p.value for p in PaymentMethod])
        payment_method_cb.pack()

        def submit_ticket():
            t_type = ticket_type_cb.get()
            t_price = entry_price.get()
            t_discount = entry_discount.get()
            p_method = payment_method_cb.get()

            # Check if all fields are filled
            if not all([t_type, t_price, t_discount, p_method]):
                messagebox.showerror("Input Error", "All fields are required.")
                return

            # Validate ticket price and discounted amount
            try:
                t_price_float = float(t_price)
                t_discount_float = float(t_discount)
                if t_price_float < 0 or t_discount_float < 0:
                    messagebox.showerror("Input Error", "Prices must be non-negative.")
                    return
            except ValueError:
                messagebox.showerror("Input Error", "Price fields must be numeric.")
                return

            # Determine eligibility from discounted amount
            if t_discount_float == 0:
                discount_status = DiscountEligibility.NOT_ELIGIBLE
            else:
                discount_status = DiscountEligibility.ELIGIBLE

            # Create ticket and associated payment
            ticket = Ticket(TicketType(t_type), f"T{len(self.current_user.get_accounts()) + 1}", t_price_float,
                            t_discount_float)
            payment = Payment(PaymentMethod(p_method), f"P{len(self.current_user.get_accounts()) + 1}", date.today(),
                              f"{t_discount_float} off")
            ticket.set_payment(payment)

            # Create account using eligibility status
            account = Account(f"A{len(self.current_user.get_accounts()) + 1}", AccountStatus.ACTIVE, date.today(),
                              discount_status)
            account.add_ticket(ticket)
            self.current_user.add_account(account)

            # Save to file
            save_users_to_file(self.users)

            messagebox.showinfo("Success", "Ticket purchased and linked to your account.")
            self.dashboard_screen()

        tk.Button(self.root, text="Purchase", command=submit_ticket).pack(pady=10)
        tk.Button(self.root, text="Back", command=self.dashboard_screen).pack()

    # Displays the logged-in fan's profile
    def view_profile(self):
        self.clear_window()

        tk.Label(self.root, text="Your Profile", font=("Arial", 14)).pack(pady=10)
        tk.Label(self.root, text=self.current_user.__str__()).pack(pady=5)

        tk.Label(self.root, text="Accounts and Tickets:").pack()
        for acc in self.current_user.get_accounts():
            tk.Label(self.root, text=acc.__str__()).pack()
            for ticket in acc.get_tickets():
                tk.Label(self.root, text="  - " + ticket.__str__()).pack()

        tk.Button(self.root, text="Back", command=self.dashboard_screen).pack(pady=10)

    # Logs out the current user
    def logout(self):
        self.current_user = None
        self.create_main_menu()

    # Utility function to clear all widgets from the window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Entry point to run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    app = GrandPrixApp(root)
    root.mainloop()



