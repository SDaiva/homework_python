from datetime import date
import os
from pathlib import Path
def audit_system():
    print()

while True:
    #here is programed user input: name, surname, ID
    add_name = input("Name: ")
    add_surname = input("Surname: ")
    add_id = input("Personal ID: ")

    #here all user input is added into 1 line
    lines = [add_name, " ", add_surname, " ", add_id + '\n']

    #here is programed path where new folder must be saved and defined that folder must named by today date
    path = "/home/sgtuser/Devops/sgt2/homework/" + str(date.today())

    #here new folder is created or if Folder exist it is ok to continue. Otherwise the error is printed
    try:
        os.makedirs(path, exist_ok=True)
    except OSError as error:
        print("New folder cannot be created : ", str(NameError))

    #here is defined file name. It will contain ID added by user and will be saved as txt file
    file_name = add_id + '.txt'.format(path)

    #here is defined that new file must be created in new folder named with today date
    new_file = os.path.join(path, file_name)

    #here is opened new file and written user input
    with open(new_file, 'a') as f:
        for line in lines:
            f.write(line)
    #here is defined information in latest file
    with open(new_file, 'r') as f:
        content = f.read()

    #print user input and file, path where input is saved and all content
    print(
        "***********************************" + '\n'
        "Your latest input:"
        "Name: " + " " + add_name + '\n'
        "Surname: " + " " + add_surname + '\n'
        "Personal ID number: " + add_id + '\n'
        "Input is saved in the file: " + file_name + '\n'
        "location / folder" + path + '\n'
        "All content in the file: " + '\n' +
        content + '\n'
        "***********************************")

    #to continue or to go out of program
    check = input("Run the program again? Y/N ")
    if check.upper() == "Y":
        continue
    print("See you next time")
    break