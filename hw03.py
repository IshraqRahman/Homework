"""
Step 1: Create a file name hw03.py inside the HW folder

Step 2: Define value for some variables like stName, stId, stGrade, fullTimeStudent etc

Step 3: Now create an User defined function name st_info. Use only one formatting Text inside this function and call all variables. Expected outcome below like line by line when you call this function.
Student Name: <your name here from stName but in upper case and inside double quotation>
Student Id: <your Id here from stId>
Student Grade: <your grade here from stGrade but containiing floating value with 3 decimel>
Full Time Student: <Your status here from fullTimeStudent>
Step 4: Copy the code and paste it below
"""

stName = "Ishraq Rahman"
stId = 2465749
stGrade = 5.92
fulltimeStudent = "True"

def st_info():
    x = f"Student Name: \"{stName.upper()}\" \nStudent Id: {stId} \nStudent Grade: {stGrade:.3f} \nFull Time Student: {fulltimeStudent}"
    print(x)

st_info()












