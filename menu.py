
#Aqui eu estou importando os def do arquivo csv.py
from csv import  load_users_from_csv, save_users_to_csv

#users = {}


#carregar usuários do arquivo csv
users = load_users_from_csv("users.csv")

while True:
    print("\nUser Manager:")
    print("1. Add user")
    print("2. Remove user")
    print("3. List all users")
    print("4. Search user by email")
    print("5. Exit")
    print(".....................................")
    print("6. Save the changes")
    print(".....................................")
    
    choice = str(input("Digite sua opção: "))
    #choice = "5"

    if choice == "1":
        name = input("Enter name: ")
        email = input("Enter email: ")
        
        if email in users:
            print("User with this email already exists.")
        else:
            users[email] = name
            save_users_to_csv("users.csv", users)
            print(f"{name} added successfully!")
            print("PLEASE, PRESS 6 TO SAVE YOUR INFORMATIONS")
                       

    elif choice == "2":
        email = input("Enter email to remove: ")
        
        if email in users:
            del users[email]
            save_users_to_csv("users.csv", users)
            print(f"User with email {email} removed successfully!")
        else:
            print("User not found.")

    elif choice == "3":
        if not users:
            print("No users in the list.")
        else:
            for email, name in users.items():
                print(f"Name: {name}, Email: {email}")

    elif choice == "4":
        email = input("Enter email to search: ")
        
        if email in users:
            print(f"Name: {users[email]}, Email: {email}")
        else:
            print("User not found.")

    elif choice == "5":
        print("Goodbye!")
        break
    elif choice == "6":
        save_users_to_csv("users.csv", users)
        print("Thanks, your informations are safe!")
        
        
    
        
