from database import add_entry, get_entries, create_table


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
    add_entry(entry_content, entry_date)


def view_entries(entries):
    for entry in entries:
        print(f"Date: {entry['date']}\n{entry['content']}\n\n")


print(welcome)
create_table()


while (user_input := input(menu)) != "3":
    if user_input == "1":
        new_entry()
    elif user_input == "2":
        entries = get_entries()
        view_entries(entries)
    else:
        print("Invalid option, please try again!")
