
# Parent Class
class Transaction:

    def __init__(self, account_name, balance):
        self.account_name = account_name
        self.balance = balance


    # Method to be overridden
    def process(self):
        print("Processing transaction...")


    # Method overloading simulation
    def details(self, amount=None, transaction_type=None):

        if amount is not None and transaction_type is not None:
            print(
                f"Transaction: {transaction_type}"
            )
            print(
                f"Amount: {amount}"
            )

        else:
            print(
                f"Account Holder: {self.account_name}"
            )
            print(
                f"Balance: {self.balance}"
            )



# Child Class - Deposit
class Deposit(Transaction):

    def process(self, amount):

        self.balance += amount

        print(
            f"{amount} deposited successfully."
        )

        print(
            f"New Balance: {self.balance}"
        )



# Child Class - Withdrawal
class Withdrawal(Transaction):

    def process(self, amount):

        if amount <= self.balance:

            self.balance -= amount

            print(
                f"{amount} withdrawn successfully."
            )

            print(
                f"New Balance: {self.balance}"
            )

        else:
            print("Insufficient funds.")



# Child Class - Transfer
class Transfer(Transaction):

    def process(self, amount, receiver):

        if amount <= self.balance:

            self.balance -= amount

            print(
                f"{amount} transferred to {receiver}"
            )

            print(
                f"Remaining Balance: {self.balance}"
            )

        else:
            print("Transfer failed. Insufficient funds.")



# Demonstration

employee = Deposit(
    "John",
    5000
)

employee.process(2000)


print("--------------------")


withdraw = Withdrawal(
    "John",
    employee.balance
)

withdraw.process(1000)


print("--------------------")


transfer = Transfer(
    "John",
    withdraw.balance
)

transfer.process(
    1500,
    "Mary"
)


print("--------------------")


# Method overloading demonstration

transaction = Transaction(
    "John",
    5000
)

transaction.details()

transaction.details(
    2000,
    "Deposit"
)