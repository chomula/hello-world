#this is a simple program written in python
print("hello world")
print("Wellcome to the simple grading system")
print("please enter the mode you want to use the program as:")
userinput = input("Teacher or Student: > ")
loweruserinput = userinput.lower()
length = len(userinput)
if loweruserinput == "student":
    print("Welcome dear student")
elif loweruserinput == "teacher":
    print("Welcome dear instructor")
else:
    print("You entered the wrong input")
