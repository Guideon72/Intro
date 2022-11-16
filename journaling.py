from datetime import date, datetime
from pathlib import Path

"""Building out variables"""
today = input("Please enter today's date (yyyy:mm:dd): ")
# print(today)
mood = input("Please enter your mood rating for today (1-10): ")
# print(mood)
feels = input("Let me know your thoughts for today: ")
# print(feels)


"""Setting up directory and files"""
fileDir = Path(Path.cwd() / "journal")
fileDir.mkdir(parents=True, exist_ok=True)

fileName = Path(fileDir / F"{today}.txt")
fileName.touch(exist_ok=True)


"""Doing shit with all of the above"""


def main():
    pass


if __name__ == '__main__':
    main()
