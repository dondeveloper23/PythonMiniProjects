class BankAccount():
    def __init__(self, owner: str, balance: int):
        self.owner = owner
        self.__balance = float(balance)
    
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        value = float(value)
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self.__balance = value

    def deposit(self, value):
        value = float(value)
        if value <= 0:
            raise ValueError("Value must be bigget than 0!")
        else:
            self.__balance += value

    def withdraw(self, value):
        value = float(value)
        if value > self.__balance or value <= 0:
            raise ValueError(f"Value must be more than 0 and less than {self.__balance}")
        
        self.__balance -= value