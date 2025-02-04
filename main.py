import os

directories = input("enter correct file paths: ").split()

for directory in directories:
    try:
        list_directory = os.listdir(directory)
    except FileNotFoundError:
        print(f"Kindly enter a valid directory, as {directory} is invalid")
        break

    print("\n")

    print(f"List directories for {directory}")
    for file in list_directory:
        print (file)
    