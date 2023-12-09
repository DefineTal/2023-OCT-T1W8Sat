from todo_functions import add_todo, remove_todo, mark_todo, view_todo

file_name = "list.csv"

try:
    # open the file in read mode
    todo_file = open(file_name, "r")
    todo_file.close()
    print("In try block")
    # if it throws error = file doesnt exist. If error in read mode doesnt exist
    # if no error = file exists
except FileNotFoundError:
    # Now, we know the file doesnt exist
    todo_file = open(file_name, "w")
    # Create the file
    # We can also insert the first line into the file
    todo_file.write("title,completed\n")
    todo_file.close()
    print("In except block")


print("Welcome to your TODO List!")

def create_menu():
    print("1. Enter 1 to add item to your list")
    print("2. Enter 2 to remove item to your list")
    print("3. Enter 3 to mark itme as completed")
    print("4. Enter 4 to view your todo list")
    print("5. Enter 5 to exit")
    choice = input("Enter your selection: ")
    return choice


user_choice = ""

while user_choice != "5":
    user_choice = create_menu()
    if (user_choice == "1"):
        add_todo(file_name)
    elif (user_choice == "2"):
        remove_todo(file_name)
    elif (user_choice == "3"):
        mark_todo(file_name)
    elif (user_choice == "4"):
        view_todo(file_name)
    elif (user_choice == "5"):
        continue
    else:
        print("Invalid input")
        
print("Thankyou for using todo list!")