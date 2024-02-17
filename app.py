menu = """Select one the following options:
1) Record your thoughts in the diary.
2) Take a look at the diary.
3) Exit.

Your Selection:
"""

welcome = "Welcome to the diary!"

print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        print("Writing....")
    elif user_input == "2":
        print("Looking...")
    else:
        print("Invalid option, please try again!")
