tasks = []
next_id = 1

while True:

    print("\n========== TO-DO LIST ==========")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Search Task")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

   
    if choice == "1":

        title = input("Enter Task: ").strip()

        if title == "":
            print("Task cannot be empty.")
            continue

        task = {
            "id": next_id,
            "title": title
        }

        tasks.append(task)

        next_id += 1

        print("Task Added Successfully!")

   
    elif choice == "2":

        if len(tasks) == 0:

            print("\nNo Tasks Available.")

        else:

            print("\n------ YOUR TASKS ------")

            for task in tasks:

                print(f'{task["id"]}. {task["title"]}')

    elif choice == "3":

        keyword = input("Search: ").lower()

        found = False

        print()

        for task in tasks:

            if keyword in task["title"].lower():

                print(f'{task["id"]}. {task["title"]}')

                found = True

        if not found:
            print("Task Not Found.")

  
    elif choice == "4":

        print("\nThank you for using To-Do List!")

        break

  
    else:

        print("Invalid Choice.")