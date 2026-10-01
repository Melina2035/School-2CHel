import time

expenses = [] #undefined long array
a = "=========================="
b = "*******************************"

print(b+"\nWelcome to Budget Tracker!\n"+b+"\n\n")

budget = float(input("How much money do you have?"))
while True:
    print(a+"\n1 - Add an expense")
    print("2 - Show expenses")
    print("3 - Show remaining money")
    print("4 - Exit\n"+a)


    choice = input("Choose: ")

    if choice == "1":
        name = input("What did you buy? ")
        price = float(input("How much did it cost?"))
        expenses.append([name, price]) #2d array
        print()
        print()
        print()
        print("Expense added!")

    elif choice == "2":
        print()
        print("Your expenses:")

        if len(expenses) == 0: #if the array is empty
            print("No expenses yet.")
        else:
            for expense in expenses:
                print(f"{expense[0]} - {expense[1]:.2f} €") #:.2f to show 2 numbers after ,

    elif choice == "3":
        total = 0 #otherwise always keeps on adding when we use show remaining money

        for expense in expenses:	#adding all the array expense together to get the total
            total = total + expense[1]

        remaining = budget - total #calculating the remainer from how high ur budget is minus total spent money
        print(f"\nBudget: {budget:.2f}€") #:.2f to show 2 numbers after ,
        print(f"Spent: {total:.2f}€")
        print(f"Remaining: {remaining:.2f}€")
        time.sleep(2)
        if remaining < 0:
            print("You spent too much!")
        else:
            print("You are still within your budget.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Please choose 1, 2, 3 or 4.")
