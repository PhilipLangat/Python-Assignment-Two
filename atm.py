# Initialize the user's balance
balance = 1000  # Starting with Ksh.1000

# Define the ATM menu
def atm_menu():
    print("\nWelcome to the ATM")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")
    
# Run the ATM program in a loop
while True:
    atm_menu()  # Display the menu
    choice = input("Please choose an option (1-4): ")
    
    # Handle user's choice
    if choice == '1':
        # Check balance
        print(f"Your current balance is: Ksh.{balance}")
    
    elif choice == '2':
        # Deposit money
        deposit_amount = float(input("Enter amount to deposit: Ksh."))
        if deposit_amount > 0:
            balance += deposit_amount  # Update balance
            print(f"Ksh.{deposit_amount} deposited successfully.")
            print(f"New balance is: Ksh.{balance}")
        else:
            print("Invalid deposit amount.")
    
    elif choice == '3':
        # Withdraw money
        withdraw_amount = float(input("Enter amount to withdraw: Ksh."))
        if 0 < withdraw_amount <= balance:
            balance -= withdraw_amount  # Update balance
            print(f"Ksh.{withdraw_amount} withdrawn successfully.")
            print(f"New balance is: Ksh.{balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")
    
    elif choice == '4':
        # Exit the program
        print("Thank you for using the ATM. Goodbye!")
        break  # Exit the loop and end the program
    
    else:
        # Handle invalid menu choice
        print("Invalid option. Please choose a number between 1 and 4.")
