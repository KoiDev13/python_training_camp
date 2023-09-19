import os

def create_file(fileName: str):
    try:
        with open(file_name, "w") as f:
            f.write("Hello World!\nThe file is initially created.")
        print("-- SYSTEM: File " + fileName + " has been created successfully. --")
    except IOError:
        print('Error: Cannot create file ' + file_name)

def read_file(fileName: str):
    try:
        print("-- SYSTEM: Reading content of file " + fileName + ". --")
        with open(fileName, 'r') as f: 
            data  = f.readlines()
            for line in data:
                print(line)
        print("-- SYSTEM: File " + fileName + " is read successfully. --")
    except IOError:
        print("Error: Cannot read file " + fileName + ".")

def append_file(fileName: str):
    try:
        with open(fileName, 'a') as f:
            f.write("\nThis is the append line.")
        print("-- SYSTEM: File " + fileName + " is read successfully. --")
    except IOError:
        print("Error: Cannot append file " + fileName + ".")

def rename_file(fileName: str, newFileName):
    try:
        os.rename(fileName, newFileName)
        print("-- SYSTEM: File " + fileName + " is rename to " + newFileName + " successfully. --")
    except IOError:
        print("Error: Cannot rename file " + fileName + ".")

def remove_file(fileName: str):
    try:
        os.remove(fileName)
    except IOError:
        print("Error: Cannot remove file " + fileName + ".")

if __name__ == '__main__':
    print("SYSTEM:File handlers starts!")
    # file_name = input("Enter file name: ")
    file_name = 'khoimap.txt'
    new_file_name = 'khoimap-new.txt'
    create_file(file_name)
    read_file(file_name)
    rename_file(file_name, new_file_name)
    append_file(new_file_name)
    read_file(new_file_name)
    remove_file(new_file_name)