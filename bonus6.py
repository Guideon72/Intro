"""TODO: Make this work with pathlib"""

contents = ["This is the content for file1.txt",
            "This is the content for file2.txt", "This is the content for file3.txt"]
filenames = ["./data/b6/file1.txt",
             "./data/b6/file2.txt", "./data/b6/file3.txt"]

for content, filename in zip(contents, filenames):
    with open(filename, 'w+')as file:
        file.write(content)
