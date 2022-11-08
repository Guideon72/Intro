"""A basic ToDo list application written in Python 3.10"""
import re

task = input('Please enter your new task here: ')
pattern = "^[A-Za-z0-9', ]*$"
taskList = ()


def getTask(task):
    retry = True
    try:
        while retry:
            if re.match(pattern, task):
                retry = False
                return task
            else:
                print("Sorry, that is not valid")
                break
    except Exception as e:
        return e


def main():
    nt = getTask(task)
    print(nt)


if __name__ == '__main__':
    main()
