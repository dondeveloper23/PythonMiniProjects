from datetime import datetime, timedelta

class BankAccount():
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = float(balance)
        self._transactions = []
        self.__overdraft_limit = 0

    @property
    def balance(self):
        return self.__balance
    @property
    def overdraft_limit(self):
        return self.__overdraft_limit
    
    @balance.setter
    def balance(self, new_balance):
        new_balance = float(new_balance)
        if new_balance < 0:
            raise ValueError("Invalid entry! Balance can't be less than 0")
        self.__balance = new_balance

    @overdraft_limit.setter
    def overdraft_limit(self, limit_amount):
        limit_amount = float(limit_amount)
        if limit_amount < 0:
            raise ValueError("Invalid entry! Limit can't be less than 0")
        self.__overdraft_limit = limit_amount

    def deposit(self, amount):
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Invalid entry! Deposit amount can't be less than or 0!")
        self.__balance += amount
        self.add_transactions("DEPOSIT", amount)
        

    def withdraw(self, amount):
        amount = float(amount)
        if amount > self.__balance + self.__overdraft_limit:
            raise ValueError("You don't have enough money on your account for this transaction!")
        self.__balance -= amount
        self.add_transactions("WITHDRAW", amount)

    def __str__(self):
        return f"Your have {self.__balance}$ on your account"
        
    def __repr__(self):
        return f"BankAccount(owner={self.owner!r}, balance={self.__balance:.2f})"
    def transfer(self, other: "BankAccount", amount: float):
        if not isinstance(other, BankAccount):
            raise TypeError("Other must be a BankAccount!")
        amount = float(amount)
        if amount <= 0:
            raise ValueError("Invalid entry! Transfer amount can't be less than or 0!")
        self.withdraw(amount)
        other.deposit(amount)
        self.add_transactions("TRANSFER_OUT", amount)
        other.add_transactions("TRANSFER_IN", amount)

    def add_transactions(self, kind, amount):
        self._transactions.append((datetime.now(), kind, float(amount)))

    def statement(self):
        if self._transactions == []:
               return "No transactions yet"
        rows = ["DATE AND TIME | TYPE | AMOUNT"]
        for line in self._transactions:
            

            date = line[0].strftime("%A, %B %d, %Y %H:%M:%S")
            kind = line[1]
            amount = float(line[2])
            line = f"{date} | {kind} | {amount}"
            rows.append(line)

        return "\n".join(rows)


class SavingsAccount(BankAccount):
    def __init__(self, owner, balance):
        super().__init__(owner, balance)
        self.rate = 0.10
        self._last_interest_applied_at = None
        self.first_deposit_at = None

    def deposit(self, amount):
        super().deposit(amount)
        if self.first_deposit_at == None:
            self.first_deposit_at = datetime.now()

    def apply_interest(self, now=None):
        now = now or datetime.now()

        if self.first_deposit_at is None:
            return
        anchor = self._last_interest_applied_at or self.first_deposit_at
        if now - anchor < timedelta(days=365):
            return
        
        interest = self.balance * self.rate

        self._BankAccount_balance += interest

        self.add_transactions("INTEREST", interest)

        self._last_interest_applied_at = now