pin = 3175
balance = 75000

Name = input("Enter your name :")
user_pin = int(input("enter you pin:"))

if pin == user_pin:
    print("HELLO",Name,"to XYZ ATM")

    while True:
        print("\n 1. check balance")
        print(" 2. deposit Money")
        print(" 3. Withdraw Money")
        print(" 4. Exit")

        choice=int(input("enter your choice from(1/2/3/4):"))

        if choice==1:
            print("Your Current Balance Is Rs:",balance)
         
        elif choice==2:
            amount=int(input("Enter Deposit Amount:"))
            if amount>0:
                balance=balance+amount
                print("Amount Deposited Successfully!")
                print ("Updated Balance:",balance)
            else:
                print("Enter A Valid Amount !")
        elif choice==3:
            amount=int(input("Enter Withdrawal Amount"))
            if amount<0:
                print("Enter A Valid Amount!")
            elif amount<=balance:
                balance=balance-amount
                print("Collect Your Cash")
                print("Remaininig Balance:Rs",balance)
            else:
                print("Insufficient Balance!")
        elif choice==4:
                 print("Thank You ")
                 break
        else:
            print("Invalid Choice Try Again.")
else:
        print("Incorrect Pin Access Denied")


        