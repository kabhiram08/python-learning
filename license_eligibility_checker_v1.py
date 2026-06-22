#Importing date and time to work on License eligibility         

#User name input

username = input("Enter your name: ")         

from datetime import datetime

#Get user's DoB data

dob = input ("Enter your date of brith in dd/mm/yyyy format:")  

print ("Hello", username,"\nLets check if you are eligible for a driving license. Please wait a moment...")

#Convert the string input to a date which python can understand

dob = datetime.strptime(dob, "%d/%m/%Y")

#Comparing with today's date to find out the remaing number of days

today = datetime.now()

#Calculating when the user turns 18 years old

eigtheenth_birthday = datetime(dob.year + 18, dob.month, dob.day)

if dob > today:
    print (" Be honest dudee!😑😒")
    quit()


# INVALID DATES TO BE LEARNT YET
    

#Eligibility check along with declaration

if eigtheenth_birthday > today:
     remaining_days = eigtheenth_birthday - today
     print ("You will be eligible for a driving license in ", remaining_days.days, "days")

else:
    print ("Congratulations! You are eligible for a license. Please apply for it as soon as possible.")

# Asking for area to determine the nearest RTO office

    area = input("Enter your area name to find the nearest RTO office: ") 

    if area.lower() == "miyapur":
        print ("The nearest RTO office is located at Patancheru, Hyderabad.")

    elif area.lower() == "kukatpally":
        print ("The nearest RTO office is located at Kukatpally, Hyderabad.")

    elif area.lower() == "Hafeezpet":
     print ("The nearest RTO office is located at Kondapur, Hyderabad.")

    else: 
     print ("Sorry, we do not have information about the nearest RTO office in your area. Please check with local authorities for more information.")



     #DONE