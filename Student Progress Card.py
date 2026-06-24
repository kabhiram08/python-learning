name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

def analyse_marks(marks):
    if marks >= 90:
        return "Grade A"
    elif marks >= 75 and marks < 90:
        return "Grade B"
    elif marks >= 60:
        return "Grade C"
    elif marks >= 50:
        return "Grade D"
    else:
        return "Grade F"
    
grade_determination = analyse_marks(marks)
print(grade_determination)

if marks >= 50:
    print("Pass")
else:
    print("Fail")

if grade_determination == "Grade A":
    print("Excellent performance")
elif grade_determination == "Grade B":
    print("Very good")
elif grade_determination == "Grade C":
    print("Needs improvement")
elif grade_determination == "Grade D":
    print("Get out of my class!")
else:
    print("Meet me in my cabin!!")

    
    