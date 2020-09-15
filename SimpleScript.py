#this is a simple program written in python
def studentAuthe():
    studID = input("Please enter student ID: > ")
    studPassword = input("Now enter your password: > ")
    classRegister = {"user1":12345,"user2":6789, "user3":101112}
    if studID and studPassword in classRegister:
        print("welcome " + str(classRegister[studPassword]))
        studentV = classRegister[studPassword]
        studentView(studentV)
    else:
        print("the username and password you enter is incorrect")

def teacherAuthe():
    pass
    print('hello ba teacher')
    teacherID = input("Please enter teacher ID: > ")
    teachPasswd = input("Now enter your password: > ")

def studentView(studentID):
    print("hello")

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



