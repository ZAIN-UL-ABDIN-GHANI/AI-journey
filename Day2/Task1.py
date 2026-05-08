# =========================================================
# MINI BANKING SYSTEM PROJECT (OOP)
# =========================================================

# ================= QUESTION =================
# Create a Python Banking Application using OOP.

# The program should allow the user to:
#
# 1. Create Bank Account
#    - Enter name
#    - Enter initial balance
#
# 2. Deposit Money
#    - Enter account name
#    - Enter deposit amount
#
# 3. Withdraw Money
#    - Enter account name
#    - Enter withdraw amount
#    - Check balance before withdrawing
#
# 4. Check Balance
#    - Show current balance of an account
#
# 5. Show All Accounts
#    - Display all stored accounts
#
# ================= REQUIREMENTS =================
# - Use Class 
# - Use functions inside class
# - Use list to store all accounts
# - Use loops for menu system
# - Use try-except for error handling
# - Use variables, functions, OOP, lists

# =========================================================
# CLASS DEFINITION
# =========================================================

class BankAccount:

    # Create account function (NO constructor used)
    def create_account(self, name, balance):
        self.name = name
        self.balance = balance

    # Deposit money function
    def deposit(self, amount):

        # Check valid amount
        if amount > 0:
            self.balance += amount
            print("Deposit Successful")
            print("New Balance:", self.balance)

        else:
            print("Invalid Amount")

    # Withdraw money function
    def withdraw(self, amount):

        # Check invalid amount
        if amount <= 0:
            print("Invalid Amount")

        # Check insufficient balance
        elif amount > self.balance:
            print("Insufficient Balance")

        else:
            self.balance -= amount
            print("Withdraw Successful")
            print("Remaining Balance:", self.balance)

    # Show balance function
    def show_balance(self):
        print("Current Balance:", self.balance)


# =========================================================
# STORAGE FOR ALL ACCOUNTS
# =========================================================

accounts = []

# =========================================================
# FUNCTION TO FIND ACCOUNT
# =========================================================

def find_account(name):

    # Loop through all accounts
    for account in accounts:

        # Case-insensitive match
        if account.name.lower() == name.lower():
            return account

    return None


# =========================================================
# MAIN MENU LOOP
# =========================================================

while True:

    # Show menu
    print("\n===== BANKING SYSTEM =====")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Check Balance")
    print("5. Show All Accounts")
    print("6. Exit")

    # Take user choice
    choice = input("Enter Choice: ")

    # =====================================================
    # CREATE ACCOUNT
    # =====================================================
    if choice == "1":

        # Input name
        name = input("Enter Name: ")

        try:
            # Input balance
            balance = float(input("Enter Initial Balance: "))

            # Create object
            account = BankAccount()

            # Call function
            account.create_account(name, balance)

            # Store in list
            accounts.append(account)

            print("Account Created Successfully")

        except ValueError:
            print("Invalid Balance Input")

    # =====================================================
    # DEPOSIT MONEY
    # =====================================================
    elif choice == "2":

        name = input("Enter Account Name: ")

        account = find_account(name)

        if account:

            try:
                amount = float(input("Enter Deposit Amount: "))
                account.deposit(amount)

            except ValueError:
                print("Invalid Amount")

        else:
            print("Account Not Found")

    # =====================================================
    # WITHDRAW MONEY
    # =====================================================
    elif choice == "3":

        name = input("Enter Account Name: ")

        account = find_account(name)

        if account:

            try:
                amount = float(input("Enter Withdraw Amount: "))
                account.withdraw(amount)

            except ValueError:
                print("Invalid Amount")

        else:
            print("Account Not Found")

    # =====================================================
    # CHECK BALANCE
    # =====================================================
    elif choice == "4":

        name = input("Enter Account Name: ")

        account = find_account(name)

        if account:
            account.show_balance()

        else:
            print("Account Not Found")

    # =====================================================
    # SHOW ALL ACCOUNTS
    # =====================================================
    elif choice == "5":

        if len(accounts) == 0:
            print("No Accounts Available")

        else:
            print("\n--- ALL ACCOUNTS ---")

            for account in accounts:
                print("Name:", account.name)
                print("Balance:", account.balance)
                print("-------------------")

    # =====================================================
    # EXIT PROGRAM
    # =====================================================
    elif choice == "6":

        print("Thank You For Using Banking System")
        break

    # =====================================================
    # INVALID OPTION
    # =====================================================
    else:
        print("Invalid Choice")