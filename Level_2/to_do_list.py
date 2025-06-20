import os
def add_task():
    # Add Task
    if os.stat("to_do_list.txt").st_size == 0:
        lines_to_write = []
        task = input("Enter Task : ")
        lines_to_write.append(task)
        with open("to_do_list.txt", "w") as file:
            file.writelines(lines_to_write)
    else:
        lines_to_write = []
        with open("to_do_list.txt", "r") as file:
            for line in file:
                task = line.strip()
                lines_to_write.append(task + "\n")
        task = input("Enter Task : ")
        lines_to_write.append(task)
        with open("to_do_list.txt", "w") as file:
            file.writelines(lines_to_write)

def see_task(): 
    if os.stat("to_do_list.txt").st_size == 0:
        print("No Tasks To See!")
    else:
        # See Task
        number = 0
        with open("to_do_list.txt", "r") as file:
            for line in file:
                number += 1
                print(f"{number} : {line.strip()}")

def delete_task():
    see_task()

    if os.stat("to_do_list.txt").st_size == 0:
        print("No Task to Delete!")
    else:
        task_num = int(input("Enter the Task Number : "))
        # Getting all the tasks
        lines_to_write = []
        with open("to_do_list.txt", "r") as file:
            for line in file:
                task = line.strip()
                lines_to_write.append(task + "\n")
        lines_to_write.pop(task_num - 1)
        with open("to_do_list.txt", "w") as file:
            file.writelines(lines_to_write)

    

user_input = int(input("Enter 1 to add 2 to view 3 to delete"))

if user_input == 1:
    add_task()
elif user_input == 2:
    see_task()
elif user_input == 3:
    delete_task()
else:
    print("Invalid Input")