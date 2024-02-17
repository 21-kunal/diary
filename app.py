from database import add_entry,get_entries


menu = """Select one the following options:
1) Record your thoughts in the diary.
2) Take a look at the diary.
3) Exit.

Your Selection:
"""

welcome = "Welcome to the diary!"

def new_entry():
    entry_content = input("What is on your mind? ")
    entry_date = input("Enter the Date: ") 
    add_entry(entry_content,entry_date)


def view_entries(entires):
    for entry in entires:
        print(f"Date: {entry['date']}\n{entry['content']}\n\n")


print(welcome)

while (user_input := input(menu)) != "3":
    if user_input == "1":
        new_entry()
    elif user_input == "2":
        entires = get_entries()
        view_entries(entires)
    else:
        print("Invalid option, please try again!")
