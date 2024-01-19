# Joyce C, Yingyi M
# Period 4
# 1/10/2024
# Shopping To-Do List

# Initialize
grocery_list = []

# Function to add grocery
# No parameters
def add_grocery():
    new_item = input("\nEnter a new item you would like to buy: ")
    grocery_list.append(new_item)

# Function to view shopping list
# No parameters
def view_list():
    print(grocery_list)

# Function to mark as bought
# No parameters
def mark_bought():
    bought_item = input("\nEnter the item that you have put in your cart: ")
    bought_index = grocery_list.index(bought_item)
    grocery_list.pop(bought_index)
    marked_item = bought_item + " [X]"
    grocery_list.insert((bought_index),marked_item)

# Function to remove grocery
# No parameters
def remove_grocery():
    delete_item = input("\nEnter the item that you would like to remove: ")
    grocery_list.pop(grocery_list.index(delete_item))

# Function to remove all items
# No parameters
def remove_all():
    grocery_list.clear()

# Function to sort list alphabetically
# No parameters
def sort_groceries():
    grocery_list.sort()

# Function to print number of items in list
# No parameters
def count_groceries():
    print(f"{len(grocery_list)} grocery items")

# Main
    
# While loop to keep program running
while True:
    # Introduce program
    print("\nWelcome to Grocery List Manager. What action would you like to take?: ")

    print("\n    1. Add Grocery Item")
    print("    2. View Current Grocery List")
    print("    3. Mark Grocery Item as Bought")
    print("    4. Remove Grocery Item")
    print("    5. Remove ALL Items")
    print("    6. Sort List Alphabetically")
    print("    7. Get Number of Items in List")
    print("    8. Exit")

    action_option = input("\nWhich action? (Enter a number 1 to 5): ")

    # Gives the index of each list for the choice of action
    if action_option == "1":
        add_grocery()

    elif action_option == "2":
        view_list()

    elif action_option == "3":
        mark_bought()

    elif action_option == "4":
        remove_grocery()

    elif action_option == "5":
        remove_all()

    elif action_option == "6":
        sort_groceries()

    elif action_option == "7":
        count_groceries()

    elif action_option == "8":
        break