class Bank:
    def __init__(self, acc_name, acc_number):
        self.name = acc_name
        self.num = acc_number
        self.Balance = 0.0

    @classmethod
    def create_user(cls, data):
        acc_name, acc_number = data.split(',')
        return cls(acc_name, acc_number)

    def withdrawal(self, amount):
        self.Balance -= amount
        return f"You make a withdrawal of {amount} and your balance are {self.Balance}"

    def deposit(self, amount=0):
        self.Balance += amount
        return self.Balance

    def __repr__(self):
        return f"{self.name} account number is {self.num} and the balance on the account is {self.Balance}."


first = Bank.create_user('Akintobi,0097993499')
print(first.num)
first.withdrawal(2700)
first.withdrawal(2800)
first.deposit(9500)
first.withdrawal(2500)
print(f"Your balace is {first.Balance}. Thank you for banking with us")
print(first)
