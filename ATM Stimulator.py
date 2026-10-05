balance = 10_000

while True:
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Choose an option: ")
    if choice == "1":
        print("Your balance is #", balance)
    elif choice == "2":
        amount = int(input("Enter amount to deposit: "))
        balance = balance + amount
        print("Deposit succesful. Neww balance: #", balance)
    elif choice == "3":
        amount = int(input("Enter amount to withdraw: "))
        if amount > balance: 
            print("Insufficient funds")
        else: 
            balance =  balance - amount
            print("Withdrawal successful. New balance: #", balance)
    elif choice == "4":
        print("Thank you for banking with us")
        break
    else:
        print("Invalid option")

