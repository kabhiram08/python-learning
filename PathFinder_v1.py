#Welcome line

print("\nHey buddy! Welcome to PathFinder!")

# Ask student name and class

name = input("\nEnter your name: ")
print("Hello," + name + " Welcome to PathFinder.")
print("Let's explore some academic possibilities for you.\n")

class_studying_in = int(input("What grade are you currently in?"))
print("")
allowed_classes = (7, 8, 9, 10)
if class_studying_in in allowed_classes: 

    #creating subjects tuple to choose from
    subjects = ("mathematics", "physics", "chemistry", "biology", "history", "geography", "economics",)

else:
    print("Sorry! PathFinder is currently designed only for students in Classes 7 to 10.")   
    quit() 

    #asking for favourite subject 

favourite_subject = input("Which subject do you enjoy the most, my friend?").lower()

#creating 'if' 'elif and 'else'for a subject chosen subject

if favourite_subject in subjects:
       
        print("\nAnalysing your interests...")
        
    #Mathematics

        if favourite_subject == "mathematics":
            print("\nSuggested Intermediate Groups:")
            print("• MPC")
            print("• MEC")

            print("\nRecommended Exams:")
            print("• JEE")
            print("• EAPCET")
            print("• CUET")
            print("• ISI Admission Test")

            print("\nPopular Career Options:")
            print("• Software Engineer")
            print("• Data Scientist")

            print("\nEmerging / Lesser-Known Career Options:")
            print("• Quantitative Analyst")
            print("• Cryptographer")
            print("• Financial Risk Analyst")   

    #Physics

        elif favourite_subject == "physics":
            print("Suggested Intermediate Groups:")
            print("• MPC")
            print("• BiPC")

            print("\nRecommended Exams:")
            print("• JEE")
            print("• EAPCET")
            print("• NEST")
            print("• IISER Aptitude Test")

            print("\nPopular Career Options:")
            print("• Engineer")
            print("• Physicist")

            print("\nEmerging / Lesser-Known Career Options:")
            print("• Astrophysicist")
            print("• Nuclear Scientist")
            print("• Aerospace Researcher")

    #Chemistry

        elif favourite_subject == "chemistry":
            print("Suggested Intermediate Groups:")
            print("• MPC")
            print("• BiPC")

            print("\nRecommended Exams:")
            print("• JEE")
            print("• NEET")
            print("• EAPCET")
            print("• CUET")

            print("\nPopular Career Options:")
            print("• Chemical Engineer")
            print("• Pharmacist")

            print("\nEmerging / Lesser-Known Career Options:")
            print("• Toxicologist")
            print("• Cosmetic Scientist")
            print("• Forensic Scientist")


    #Biology

        elif favourite_subject == "biology":
            print("Suggested Intermediate Groups:")
            print("• BiPC")
            print("• MPC (Biotechnology Path)")

            print("\nRecommended Exams:")
            print("• NEET")
            print("• EAPCET")
            print("• CUET")
            print("• ICAR AIEEA")

            print("\nPopular Career Options:")
            print("• Doctor")
            print("• Dentist")

            print("\nEmerging / Lesser-Known Career Options:")
            print("• Genetic Engineer")
            print("• Bioinformatician")
            print("• Clinical Research Scientist")

    #History

        elif favourite_subject == "history":
            print("Suggested Intermediate Groups:")
            print("• CEC")
            print("• MEC")

            print("\nRecommended Exams:")
            print("• CUET")
            print("• CLAT")
            print("• UPSC")
            print("• TSPSC/APPSC")

            print("\nPopular Career Options:")
            print("• Lawyer")
            print("• Civil Servant")

            print("\nEmerging / Lesser-Known Career Options:")
            print("• Archaeologist")
            print("• Museum Curator")
            print("• Diplomat")

    #Geography

        elif favourite_subject== "geography":
            print("Suggested Intermediate Groups:")
            print("• MEC")
            print("• MPC")

            print("\nRecommended Exams:")
            print("• CUET")
            print("• UPSC")
            print("• NID")
            print("• NIFT")

            print("\nPopular Career Options:")
            print("• Urban Planner")
            print("• Environmental Consultant")

            print("\nEmerging / Lesser-Known Career Options:")
            print("• GIS Specialist")
            print("• Cartographer")
            print("• Climate Researcher")

    #Economics

        elif favourite_subject == "economics":
            print("Suggested Intermediate Groups:")
            print("• MEC")
            print("• CEC")

            print("\nRecommended Exams:")
            print("• CUET")
            print("• CA Foundation")
            print("• CMA Foundation")
            print("• IPMAT")

            print("\nPopular Career Options:")
            print("• Economist")
            print("• Investment Banker")

            print("\nEmerging / Lesser-Known Career Options:")
            print("• Policy Analyst")
            print("• Behavioral Economist")
            print("• Economic Researcher")

else:
    print("Sorry, we cannot help with the chosen subject.")

print("\nThank you for using PathFinder!!")

    # Final Learning:
# Leart how to collect user input, validate it using tuples,
# use if elif statements and provide different outputs
# based on the user's chosen subject.

