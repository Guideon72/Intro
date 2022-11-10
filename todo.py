"""A basic ToDo list application written in Python 3.10"""
import re

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


def main():
    repeat = True
    while repeat:
        uAction = input(
            '"Add", "See", "Edit", "Complete"? (Type "exit" to quit) ').strip().lower()
        # Checking exit here instead of in match case to provide an earlier 'out' TODO: remove this and reorder case block w/ exit at top
        if uAction.lower() == "exit" or uAction.lower() == "quit":
            repeat = False
            break
        else:
            match uAction:
                case "add":
                    nTask = input("Please enter your new task now: ")
                    # refactor validation to something less obnoxious
                    taskList.append(nTask.title())
                case "see" | "show":
                    for i, t in enumerate(taskList, 1):
                        print(f"{i}: {t}")
                case "edit":  # Using first input to find element, second input to update list
                    eTask = input(
                        "Enter number of the task you want to edit: ")
                    for item in enumerate(taskList, 1):
                        if item[0] == int(eTask):
                            ntask = input(
                                F"What would you like to change {item[1]} to? ").title()
                            taskList[item[0]-1] = ntask
                        else:
                            pass  # Todo: Don't do this for production code
                case "complete":
                    cTask = int(input(
                        "Enter the number of the task you want to complete: "))
                    completed = taskList.pop(cTask-1)
                    print(F"{completed} is done.")
                case _:
                    print("Please type, either, 'Add', 'See' or 'Exit")




if __name__ == '__main__':
    main()
