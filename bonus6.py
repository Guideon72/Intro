"""TODO: Make this work with pathlib"""
from pathlib import Path

filepath = Path(Path.cwd() / "data" / "b6")
filepath.mkdir(parents=True, exist_ok=True)
filenames = [Path("file1.txt"),
             Path("file2.txt"), Path("file3.txt")]
files = []
for filename in filenames:
    file = filepath/filename
    file.touch(exist_ok=True)
    files.append(file)
# print(files)

contents = ["This is the content for file1.txt",
            "This is the content for file2.txt", "This is the content for file3.txt"]

for content, file in zip(contents, files):
    file.write_text(content)
