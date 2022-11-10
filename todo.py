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
            '"Add" a task, "See" your todo list or Edit a task? (Type "exit" to quit) ').strip().lower()
        # Checking exit here instead of in match case to provide an earlier 'out' TODO: remove this and reorder case block w/ exit at top
        if uAction == "exit":
            repeat = False
            break
        else:
            match uAction:
                case "add":
                    nTask = input("Please enter your new task now: ")
                    # refactor validation to something less obnoxious
                    taskList.append(nTask.title())
                case "see":
                    for t in taskList:
                        print(t)
                case "edit":  # Using first input to find element, second input to update list
                    option = input("Enter the task you want to edit: ")
                    for i in range(len(taskList)):
                        if taskList[i].lower() == option.lower():
                            nt = input(
                                F"What would you like to replace {taskList[i]} with? ")
                            taskList[i] = nt.title()
                case _:
                    print("Please type, either, 'Add', 'See' or 'Exit")




if __name__ == '__main__':
    main()
