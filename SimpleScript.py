#this is a simple program written in python
import MySQLdb
import math
import random

#function to authenticate the student
def studentAuthe():
    studID = input("Please enter student ID: > ")
    studPassword = input("Now enter your password: > ")
    classRegister = {"user1":12345,"user2":6789, "user3":101112}
    if studID and studPassword in classRegister:
        print("welcome " + str(classRegister[studPassword]))
        studentV = classRegister[studPassword]
        studentAction(studentV)
    else:
        print("the username and password you enter is incorrect")
        
#Function to authenticate the teacher
def teacherAuthe():
    teacherID = input("Please enter teacher ID: > ")
    teachPasswd = input("Now enter your password: > ")
    teacherDB = { 1234:'Pass1', 5678:'Pass2', 91011:'Pass3', 121314:'Pass4'}
    if teacherID and teachPasswd in teacherDB:
        print('Ilimo password iyi {}'.format(teacherDB[teacherID]))
        trueTeachID = teacherDB[teachPasswd]
        teacherAction(trueTeachID)
    else:
        print("The credentials you used are incorrect")
        teacherAuthe()
        
#student view function
def studentAction(studentID):
    print("hello ".format(studentID))
    print("Would you like to view grades for one course or all courses")
    ViewInput = input(" Enter One or All: > ")
    lowerInput = ViewInput.lower()
    if lowerInput == "one":
        print("you choose to view on course")
    elif lowerInput == "all":
        print("you chose to view all you courses")
    else:
        print("You entered the wrong input")
        
#teacherAction funtion that shows what the system allows the teacher to do      
def teacherAction(teacherID):
    print('hello '.format(teacherID))
    print("Would you like to view or edit student grades")
    ViewInput = input(" Enter View or Edit: > ")
    lowerInput = ViewInput.lower()
    if lowerInput == "view":
        print("You choose to view student grades")
        print("Would you like to view grades for one student or all students")
        ViewInput = input(" Enter One or All: > ")
        lowerInput1 = ViewInput.lower()
        if lowerInput1 == "one":
            print("Enter the ID of student you want to view")
            stud2teach = input()
        elif lowerInput1 == "all":
            print ("enter grade or class")
            grade2teach = input()
        else:
            print ("You gave the wrong input")
                      
            
    elif lowerInput == "edit":
        print("You choose to edit student grades")
        print("Would you like to edit grades for one student or all students")
        ViewInput = input(" Enter One or All: > ")
        lowerInput1 = ViewInput.lower()
        if lowerInput1 == "one":
            print ("You choose to edit grades for one student")
            stud2teach = input("Enter the ID of student whose grades you wish to edit: > ")
            print("okay")
        elif lowerInput1 == "all":
            print ("you choose to edit grades for all students")
            editInput = input("Enter the grade of the class of the students: > ")
            print ("okay")
            
              


def prompt():
    pass
    print("hello world")
    print("Wellcome to the simple grading system")
    print("please enter the mode you want to use the program as:")
    userinput = input("Teacher or Student: > ")
    while (1==1):
        pass
        loweruserinput = userinput.lower()
        lengthOfInput = len(userinput)
        if loweruserinput == "student":
            print("Welcome dear student")
            studentAuthe()
        elif loweruserinput == "teacher":
            print("Welcome dear instructor")
            teacherAuthe()
        else:
            print("You entered the wrong input")
            prompt()
            

#testing functions
prompt()



