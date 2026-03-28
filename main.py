#To do
print("Hello, what would you like to do today?")
y = ("Select '1' to Add Task \nSelect '2' to View List \nSelect '3' to Delete Task "
     "\nSelect '4' to Exit")

#This block handles the user input request
def accept():
    print(y)
    while True:
        to_do = input("Enter a number: ")
        try:
            selected = int(to_do)
            if selected in range(1, 5):
                break
            else:
                print()
                print("Enter 1, 2, 3 or 4")

        except ValueError:
            print()
            print("Enter a valid input")
            continue

    return selected

#choice = accept() -- Now called in the lower while block

mylist = []

#This block checks if the file exists
try:
    newfile = open("newfile.txt", "r")
except FileNotFoundError:
    newfile = open("newfile.txt", "w")
    newfile.close()
    newfile = open("newfile.txt", "r")

for x in newfile:
    cleaned = x.strip()
    mylist.append(cleaned)
newfile.close()

def show_list():
    i = 1
    for x in mylist:
        print(f"{i}. {x}")
        i += 1


while True:
    choice = accept()
    if choice == 4:
        break

    #This block handles Adding Tasks
    elif choice == 1:
        new_task = input("Enter a New Task: ")
        mylist.append(new_task)
        with open("newfile.txt", "a") as newfile:
            newfile.write(new_task + "\n")
        print(f"You have added {mylist[-1]}")

    #This block handles viewing the list
    elif choice == 2:
        if not mylist:
            print("The list is empty")
        else:
            print("Here is your current TO DO list:")
            show_list()

    # This block handles removing items from the list
    elif choice == 3:
        if not mylist:
            print("There are no tasks to remove")
        elif mylist:
            print("Current TO DO are: ", )
            show_list()
            while True:
                remove_task = input("Select number to remove task: ")
                try:
                    z = int(remove_task)
                    if z in range(1, len(mylist) + 1):
                        print(f"{mylist[z-1]} removed successfully")
                        mylist.pop(z-1)
                        with open("newfile.txt", "w") as newfile:
                            for x in mylist:
                                newfile.write(x + "\n")
                        break
                    else:
                        print("Enter a valid task number")
                except ValueError:
                    print("NaN! Enter a task number")



    print()
    
    
print("Exit Successfully")