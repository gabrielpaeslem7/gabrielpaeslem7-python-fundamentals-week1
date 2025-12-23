while True:
    try: 
        initial_balance = float(input("How much money do you want to deposit into your ATM account? "))
        if initial_balance > 0: #if the input is valid, break the loop
            break
        else:   
            print("Amount cannot be negative. Please enter a valid amount.") #if the input is invalid, ask again
    except ValueError:
        print("Invalid input. Please enter a numeric value.") #if the input is invalid, ask again

while True:
    print("\n--- ATM Menu ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
    choice = input("Please select an option (1-4): ")
    
    if choice == '1':
        print(f"Your current balance is: ${initial_balance:.2f}")
    
    elif choice == '2':
        while True:
            try:
                deposit_amount = float(input("Enter amount to deposit: "))
                if deposit_amount > 0:
                    break
                else:
                    print("Amount must be greater than zero.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        initial_balance += deposit_amount
        print(f"${deposit_amount:.2f} deposited successfully.")
    
    elif choice == '3':
        while True:
            try:
                withdraw_amount = float(input("Enter amount to withdraw: "))
                if 0 < withdraw_amount <= initial_balance:
                    break #stops the loop if input is valid
                else:
                    print("Invalid amount or insufficient funds.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    
        initial_balance -= withdraw_amount
        print(f"${withdraw_amount:.2f} withdrawn successfully.")

    
    elif choice == '4':
        print("Thank you for using the ATM. Goodbye!")
        break
    
    else:
        print("Invalid option. Please try again.")

