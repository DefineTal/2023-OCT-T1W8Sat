import csv

def add_todo(file_name):
    print("Add todo")
    # ask the title of the todo
    todo_name = input("Enter a todo: ")
    # open file - list,csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
        # while inserting - title = user entered
                # - completed = false
        writer.writerow([todo_name, "False"])

def remove_todo(file_name):
    print("Remove todo")

def mark_todo(file_name):
    print("Mark todo")

def view_todo(file_name):
    print("View Todo")