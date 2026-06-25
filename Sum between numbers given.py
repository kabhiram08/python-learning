num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
common_difference = int(input("Enter common difference: "))

sum = 0
current_number = num1

if num1 == num2:
    print(0)
else:

    while current_number <= num2:
     sum = sum + current_number
     current_number += common_difference

    print(sum)


