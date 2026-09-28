account = {
    "name": "Rajath",
    "balance": 10000,
    "account_type": "Savings"
}
while True:
    print("1. Check Balance \n2. Deposit \n3 Withdraw \n4 Display Account Details \n5 Exit")

    choice=int(input("Enter Your choice:"))

    match choice:
        case 1:
            print(account["balance"])
        case 2:
            amount=int(input("Enter deposit amount:"))
            account["balance"]+=amount
            print('Current balance :',account["balance"])
        case 3:
            amount=int(input("Enter withdraw amount:"))
            if amount <account["balance"]:
                account["balance"]-=amount
            else:
                print("Insufficient balance")
            print('Current balance :',account["balance"])
    
        case 4:
            print(account)
        case 5:
            exit()
        case _:
            print("Enter a valid option")

    


