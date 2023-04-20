# this was a loop written by chatgpt
# the intention was to better understand the possibilities for my ticking system console
# I thought I might be able to do it with a for loop, however, this particular loop uses while.

while True:
    print("Select an option:")
    print("1. Option 1")
    print("2. Option 2")
    print("3. Option 3")
    print("4. Option 4")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        # Do something for option 1
        print("Option 1 selected")
    elif choice == "2":
        # Do something for option 2
        print("Option 2 selected")
    elif choice == "3":
        # Do something for option 3
        print("Option 3 selected")
    elif choice == "4":
        # Do something for option 4
        print("Option 4 selected")
    elif choice == "5":
        # Exit the program
        print("Exiting program...")
        break
    else:
        print("Invalid choice. Please select again.")
