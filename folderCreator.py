import os
import csv

#TODO: Allow different class names as a sub group. This may be another column in the CSV.



def student():
    with open('student_details.csv', mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            folderName = row[2] +"-"+ row[1] +"_"+ row[0] #Concantenates the required details in the correct order.
            create_folder(folderName)



def create_folder(name):
    # TODO: Improve this to function without global variable.
    global location
    fName = name


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

if __name__ == "__main__":

    location = input("Enter path, leave blank for current locations: ")
    student()


