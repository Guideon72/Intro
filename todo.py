"""A basic ToDo list application written in Python 3.10"""
import re

task = input('Please enter your new task here: ')
pattern = "^[A-Za-z0-9', ]*$"
taskList = []


def getTask(task):
    if re.match(pattern, task):
        global taskList
        taskList.append(task)
        # return taskList
    else:
        return str("Sorry, I don't recognize that task. Please try again")


def main():
    nt = getTask(task)
    print(nt)
    print(taskList)


if __name__ == '__main__':
    main()
