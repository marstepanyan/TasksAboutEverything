# Subsystem classes

class Account:
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance

    def get_balance(self):
        return self.balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return True
        else:
            return False


class Transaction:
    def make_transaction(self, sender_account, receiver_account, amount):
        if sender_account.withdraw(amount):
            receiver_account.deposit(amount)
            return True
        else:
            return False


class Notification:
    def send_notification(self, account, message):
        print(f"Notification: Account {account.account_number} - {message}")


# Facade class

class BankingSystemFacade:
    def __init__(self):
        self.account = Account("12345", 1000)
        self.transaction = Transaction()
        self.notification = Notification()

    def get_balance(self):
        return self.account.get_balance()

    def deposit(self, amount):
        self.account.deposit(amount)
        self.notification.send_notification(self.account, f"Deposited {amount} dollars.")

    def withdraw(self, amount):
        if self.account.withdraw(amount):
            self.notification.send_notification(self.account, f"Withdrew {amount} dollars.")
            return True
        else:
            self.notification.send_notification(self.account, "Insufficient balance for withdrawal.")
            return False

    def make_transaction(self, receiver_account_number, amount):
        receiver_account = Account(receiver_account_number, 0)
        if self.transaction.make_transaction(self.account, receiver_account, amount):
            self.notification.send_notification(self.account,
                                                f"Transferred {amount} dollars to account {receiver_account_number}.")
            self.notification.send_notification(receiver_account,
                                                f"Received {amount} dollars from account {self.account.account_number}.")
            return True
        else:
            self.notification.send_notification(self.account, "Transaction failed. Insufficient balance.")
            return False


# Client code

facade = BankingSystemFacade()

print(f"Account balance: ${facade.get_balance()}")

facade.deposit(500)
print(f"Account balance after deposit: ${facade.get_balance()}")

facade.withdraw(200)
print(f"Account balance after withdrawal: ${facade.get_balance()}")

facade.make_transaction("67890", 300)
print(f"Account balance after transaction: ${facade.get_balance()}")
