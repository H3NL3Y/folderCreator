# folderCreator 

A simple program which creates folder in the format needed for exams. Uses student exam numbers and details.
The program will create sub folders dependent on class  name provided in CSV file.

---
### Format for CSV: 
>| First Name | Surname  | Exam Number | Class Code    |


---
### Instructions

1. Add student details into a CSV (name: student_details.csv) matching the format above.
2. Add it to the same location as the .py file.
3. Run

The folders should then appear in the same place as the .py.

---

#### Current Features
- Able to upload CSV with student details.
- Reads CSV and creates folders based on the class name.
- Creates a sub-folder with the following format:
>[Exam Number]-[First Name]_[Surname]


#### Features to add / TODO

- Allow users to choose folder path if needed. 
- Deal with errors and other anomalies 
