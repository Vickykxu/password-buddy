from re import A
from tkinter.messagebox import YES
import random
passwords_list = []
passwords = {}
username = ""
f = open("pf.txt", "r")
for line in f:
    for word in line.split():
        passwords_list.append(word)
for i in range(len(passwords_list)):
     if i%2 == 0:
        passwords[passwords_list[i]] = passwords_list[i+1]
f2 = open("user.txt", "r")
username = f2.read()
f.close()
f2.close()
actions = ["Generate a new password", "Add a password", "Access an existing password", "Update a password","Exit"]

## Generate a new password between lengths (5-10)
def random_password_gen(user_pass_len_choice):
    correct_password_platform = False
    random_password = ""
    while len(random_password) < user_pass_len_choice:
        random_num = random.randint(0,9)
        random_password += (str(random_num))
        if len(random_password) >= user_pass_len_choice:
            break
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        random_capital_char = random.choice(alphabet)
        random_password += (random_capital_char)
        if len(random_password) >= user_pass_len_choice:
            break
        random_special_char = "!@#$%^&*"
        random_special_char_chosen = random.choice(random_special_char)
        random_password += (random_special_char_chosen)
        if len(random_password) >= user_pass_len_choice:
            break
    print("Your password is:", random_password)
    while correct_password_platform == False:
        password_platform = input("What platform is this password for? (Ex. Netflix, Facebook, etc.)\n--> ").lower().strip()
        correct_password_user = input("Is " + password_platform + " correct?\n --> ").lower().strip()
        if correct_password_user == "yes":
            passwords[password_platform] = random_password
            correct_password_platform = True

user_finished = False
valid_pass_lengths = ["6","7","8","9","10","11","12","13"]
print("Are you an existing member? (Yes/No)")
user_is_member = input(" --> ").lower().strip()
if user_is_member == "yes" or user_is_member == "y":
   print("==================================================================================")
   print("Hello " + username + "!!")
   while user_finished == False:
        print("==================================================================================")
        print("Which would you like to do")
        for i in range(5):
            print([i+1], actions[i])
        users_action_choice = input(" --> ").strip()
        print("==================================================================================")
        if users_action_choice == "1":
            user_len_valid = False
            while user_len_valid == False:
                user_pass_len_choice = input(str("How long do you want your password (6-13)\n--> ")).strip()
                if user_pass_len_choice in valid_pass_lengths:
                    user_pass_len_choice = int(user_pass_len_choice)
                    random_password_gen(user_pass_len_choice)
                    user_len_valid = True
        elif users_action_choice == "2":
            correct_password_platform = False
            while correct_password_platform == False:
                password_platform = input("What platform is this password for? (Ex. Netflix, Facebook, etc.)\n--> ").lower().strip()
                correct_platform = input("Is " + password_platform + " correct?\n --> ").lower().strip()
                if correct_platform == "yes":
                    correct_password_platform = True
            correct_existing_password = False
            while correct_existing_password == False:
                existing_password = input("What is your existing password for " + password_platform + "?\n --> ")
                correct_password = input("Is " + existing_password + " correct?\n --> " ).lower().strip()
                if correct_password == "yes":
                    correct_existing_password = True
            passwords[password_platform] = existing_password
        elif users_action_choice == "3":
            print(passwords)
            search_user_choice = input("Would you like to search for a specific password?\n --> ").lower().strip()
            if search_user_choice == "yes":
                platform_name = input("What is the platform that you are trying to access? (Ex. Netflix, Facebook, etc.)\n--> ").lower().strip()
                print("Your password is: " + passwords.get(platform_name, "None"))
        elif users_action_choice == "4":
            locate_platform = input("Which platform's password are you trying to update?\n --> ").lower().strip()
            if locate_platform in passwords:
                reassign_password = input("What is your new password for " + locate_platform + "?\n --> ").strip()
                passwords[locate_platform] = reassign_password 
        elif users_action_choice == "5":
            user_finished = True
elif user_is_member == "no" or user_is_member == "n":
    new_user = input("Enter your name to be part of the list! --> ").lower().strip()
    print("Please restart the program to access your passwords")
    username += new_user

f = open("pf.txt", "w")
f2 = open("user.txt", "w")
try:
    f2.write(username)
    for platform, password in passwords.items():
        f.write(platform + " " + password + "\n")
finally:
    f.close()
    f2.close()

