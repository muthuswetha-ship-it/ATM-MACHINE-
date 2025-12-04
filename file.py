balance = 5000  # initial balance

while True:
    print("\n----- ATM MENU -----")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw") ji
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Current Balance:", balance)

    elif choice == 2:
        amt = int(input("Enter amount to deposit: "))
        balance += amt
        print("Amount Deposited. New Balance:", balance)

    elif choice == 3:
        amt = int(input("Enter amount to withdraw: "))
        if amt > balance:
            print("Insufficient Balance!")
        else:
            balance -= amt
            print("Withdrawal Successful. New Balance:", balance)

    elif choice == 4:
        print("Thank you for using the ATM!")
        break

    else:
        print("Invalid choice! Try again.")
