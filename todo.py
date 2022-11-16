"""A basic ToDo list application written in Python 3.10"""


def main():
    repeat = True
    while repeat:
        uAction = input(
            '"Add", "See", "Edit", "Complete"? (Type "exit" to quit) ').strip().lower()
# NOTE: Checking exit here instead of in match case to provide an earlier 'out'
# TODO: Remove this and reorder case block w/ exit at top
        if uAction.lower() == "exit" or uAction.lower() == "quit":
            repeat = False
            break
        else:
            match uAction:
                # TODO: Break cases out into discrete functions
                # TODO: Add Enchant spell-checker functionality
                case "add":
                    nTask = input("Please enter your new task now: ")
# TODO: Make this work with pathlib
                    with open("./data/tl.txt", "r") as tl:
                        tasks = tl.readlines()
# BUG: Does not allow proper names
                    tasks.append(nTask.capitalize() + "\n")
                    with open("./data/tl.txt", "w") as tl:
                        tl.writelines(tasks)

                case "see" | "show":
                    with open("./data/tl.txt", "r") as tl:
                        for i, t in enumerate(tl, 1):
                            t = t.strip('\n')
                            print(f"{i}: {t}")
# NOTE: Using first input to find element, second input to update list
                case "edit":
                    with open("./data/tl.txt", "r") as tl:
                        tasks = tl.readlines()
                    for i, t in enumerate(tasks, 1):
                        t = t.strip('\n')
                        print(f"{i}: {t}")
                    eTask = input(
                        "Enter number of the task you want to edit: ")
                    for item in enumerate(tasks, 1):
                        if item[0] == int(eTask):
                            # BUG: Does not allow proper names
                            ntask = input(
                                F"What would you like to change {item[1]} to? ").capitalize()
                            tasks[item[0]-1] = ntask + "\n"
                    with open("./data/tl.txt", "w") as tl:
                        tl.writelines(tasks)

                case "complete":
                    with open("./data/tl.txt", "r") as tl:
                        tasks = tl.readlines()
                    for i, t in enumerate(tasks, 1):
                        t = t.strip('\n')
                        print(f"{i}: {t}")
                    cTask = int(input(
                        "Enter the number of the task you want to complete: "))
                    completed = tasks.pop(cTask - 1).strip("\n")
                    print(F"'{completed}' is done.")
                    with open("./data/tl.txt", "w") as tl:
                        tl.writelines(tasks)

                case _:
                    print("Please type, either, 'Add', 'See' or 'Exit")


if __name__ == '__main__':
    main()

# """_________________________________________________________________________________"""
# task = input('Please enter your new task here: ')
# pattern = "^[A-Za-z0-9', ]*$"
taskList = []


# def getTask(task):
#     if re.match(pattern, task):
#         global taskList
#         taskList.append(task)
#         # return taskList
#     else:
#         return str("Sorry, I don't recognize that task. Please try again")
#
# def getTask(task):
#    if re.match(pattern, task):
#         return task
#     return ("I'm sorry, that is not a valid task")
