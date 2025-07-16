import os
import csv
import shutil


def student():
    with open('student_details.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            folderName = row[2] +"-"+ row[1] +"_"+ row[0]#Concantenates the required details in the correct order.
            className = row[3]
            print(className)
            #Will request location if Class Code is null
            if className == '':
                className = input(f"{folderName} has no class code assigned! Enter path for folder, leave blank for current location: ")
            create_folder(folderName,className)



def create_folder(name,className):

    fName = name
    location = className


    if not location:
        location = os.getcwd() #This returns the current location of the file.

    full_path = os.path.join(location, fName)

    try:
        if not os.path.exists(full_path):
            os.makedirs(full_path)
            print(f"Folder {fName} created at {location}.")
        else:
            print(f"Folder {fName} already exists at {location}.")
    except Exception as e:
        print(f"Error creating folder: {e}")
    if addFile == 'Y':
        addnewfile(full_path)

def addnewfile(folder_path):

    destination = os.path.join(folder_path, source_file)

    # Copy the file
    if os.path.exists(destination):
        print(f"⚠️ File already exists at: {destination}")
    else:
        shutil.copy(source_file, destination)
        print(f"✅ File copied to: {destination}")




if __name__ == "__main__":
    addFile = input("When the folders have successfully been created, do you want to add a file/s to each of them? [Y/N]: ")
    if addFile == 'Y':
        source_file = input("What is the name of the file you want to add to the folders? (This should be in the same folder as the folderCreator.py): ")
    student()



