import os


def create_folder():
    fName = input("Enter folder name: ")
    location = input("Enter path, leave blank for current locations: ")

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
    create_folder()

