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


def main():
    repeat = True
    while repeat:
        nTask = input(
            'Please enter your new task here: (Type "quit" to exit) ')
        if nTask == "quit":
            repeat = False
            break
        else:
            taskList.append(nTask)
            print(taskList)




if __name__ == '__main__':
    main()
