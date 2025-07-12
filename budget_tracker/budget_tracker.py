#print welcome message for user
user_name = input("Input your name: ")
print(f"Hello {user_name} welcome to budget manager")

#Take user income
salary = float(input("What is your monthly salary: "))
bussiness = float(input("What is the amount earn from bussiness: "))
#Take user expenses
transport = float(input("How much do you spend on transport: "))
food = float(input("How much do you spend on food: "))

#calculate user's toatal income
total_income = salary + bussiness 
print(f"Total monthly income: $ {total_income:.2f}")

#Calculate user's total expense ed from your bussiness: "))

total_expense = transport + food
print(f"Total monthly expense: ${total_expense:.2f}")

#savings 
monthly_savings = total_income - total_expense
print(f"Hello {user_name} your monthly savings is {monthly_savings: .2f}")