balance=0

def show_options():
    print(''' \nOptions:
    1. Check balance
    2. Deposit money
    3. Withdraw money
    4. Exit ''')

while True:
    show_options()
    choice = input("Please choose an option (1-4): ")
    if choice == '1':
        print(f'Your current balance is {balance}')

    elif choice == '2':
        deposit_amount = int(input("Please enter the amount you want to deposit: "))
        if deposit_amount>0:
            balance+=deposit_amount
            print(f'Deposit amount "{deposit_amount}" has been added successfully')
        else:
            print(f'Error: Please enter a valid amount')

    elif choice == '3':
        withdrawal_amt = int(input("Please enter the amount you want to withdraw: "))
        if withdrawal_amt>=balance:
            balance-=withdrawal_amt
            print(f'Amount "{withdrawal_amt}" has been withdrawn successfully')
        else:
            print(f'The withdrawal amount is greater than the current account balance')

    elif choice == '4':
        print("Exit!")
        break

    else:
        print("Invalid choice.")