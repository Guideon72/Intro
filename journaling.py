from datetime import datetime
from pathlib import Path

"""Building out variables"""
today = datetime.today().date()
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


"""Doing things with all of the above"""
with open(fileName, "w") as todayFile:
    todayFile.write(F"My mood rating today is: {mood} \n")
    todayFile.write(F"My thoughts about today are: {feels}")

def main():
    pass


if __name__ == '__main__':
    main()
