from src.bank_account import BankAccount

def main() -> None:
    acc = BankAccount("Marko", 100)

    print("Owner:", acc.owner)
    print("Start balance:", acc.balance)

    acc.deposit(50)
    print("After deposit 50:", acc.balance)

    try:
        acc.withdraw(200)
    except ValueError as e:
        print("Withdraw error:", e)

    acc.withdraw(30)
    print("After withdraw 30:", acc.balance)

    try:
        acc.balance = -10
    except ValueError as e:
        print("Setter error:", e)

    acc.balance = 500
    print("After setter to 500:", acc.balance)

if __name__ == "__main__":
    main()
