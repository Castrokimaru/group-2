class BankAccount:
    bank_name = "Equity Bank"

    def __init__(self, owner):
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        if BankAccount.is_valid_amount(amount):
            self.balance += amount
        else:
            print("Invalid amount. Deposit must be greater than 0.")

    def get_info(self):
        print(f"Owner: {self.owner} | Balance: {self.balance} | Bank: {BankAccount.bank_name}")

    @classmethod
    def change_bank(cls, new_name):
        cls.bank_name = new_name

    @staticmethod
    def is_valid_amount(amount):
        return amount > 0
