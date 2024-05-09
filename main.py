import os
from time import sleep
from termcolor import colored

# TODO creating a parent class User
class User:
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def __str__(self):
        return f" Personal details\nname: {self.name} \nage: {self.age} \ngender: {self.gender}"

#  TODO child class Bank
class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 100
        
    def deposit(self, amount):
        self.amount = amount
        self.balance = self.balance+ amount
        print(f"account balance has been updated...The new balance is ${self.balance}")
        
    def withdrwal(self, amount):
        self.amount = amount
        if self.amount> self.balance:
            print(f"insufficient amount! your balance is ${self.balance}")
        else:
            self.balance = self.balance-self.amount
            return f"here is your ${self.amount}."
        
    def __str__(self):
        return f" Personal details\nname: {self.name} \nage: {self.age} \ngender: {self.gender}"
    def view_balance(self):
        self.balance
        print(f"your balance is ${self.balance}")
        

colored_text = colored("Welcome to J&A Bank","blue")

user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))
user_gender = input("Enter your gender: ")
   
user2 = Bank(user_name,user_age,user_gender)

user_login = True
print("""
Enter 'deposit' to deposit to your account.
Enter 'balance' to check your account balance.
Enter 'withdraw' to withdraw your money.
Enter 'q' to quit.
        """)

while user_login:
    menu = input("Menu >>").lower()

    if menu == "balance":
        print(user2.view_balance())
    
    elif menu == "deposit":
        print(user2.deposit(int(input("Enter amount you want to deposit: $"))))
        
    elif menu == "withdraw":
        print(user2.withdrwal(int(input("Enter amount you want to withdraw: $"))))
    elif menu =="q":
        print("Thank you for banking with us!")
        user_login = False
        sleep(2)
        os.system('clear')
    else:
        print ("We do not support that in this bank")




        
