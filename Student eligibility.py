name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
print("")
def recieve_age_marks(age , marks):
    if age >= 16 and marks >= 75:
        return "eligible"
    else:
        return "not eligible"
    
result = recieve_age_marks(age, marks)
if result == "Eligible":
    print("Heyy " + name + "!!!")
    print("You are " + result)
else:
    print("Sorry you are " + result)
    






    