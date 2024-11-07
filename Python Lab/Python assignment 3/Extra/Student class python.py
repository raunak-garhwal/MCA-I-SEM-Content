class Student:
    total_students = 0

    def __init__(self):
        name=input("\nEnter the name of the student : ")
        age=int(input("Enter the age of the student : "))
        course=input("Enter the course of the student : ")
        self.name=name
        self.age=age
        self.course=course
        Student.total_students += 1
        print(f"\nCONGRATULATIONS {self.name}! YOU HAVE REGISTERED SUCCESSFULLY.")

    def display_student_info(self):
        print("\n\'''STUDENT INFORMATION\'''")
        print(f"\nName : {self.name}")
        print(f"Age : {self.age}")
        print(f"Course : {self.course}")

print("\n\'''WELCOME TO THE STUDENT REGISTRATION PORTAL\'''")

while(True):

    print("\nPress 1 for New Student Registration.\nPress 2 to get Student Information.\nPress 3 to discover the total count of enrolled students.\nPress 4 to exit.")

    try:
        choice = int(input("\nEnter your choice : "))
    except:
        print("\nWARNING :- Please enter a valid numeric value. Thank you.")
    else:    
        if choice == 1:
            new_student = Student()

        elif choice == 2:
            try:
                new_student.display_student_info()
            except:
                print("\nWARNING :- Please register yourself first. Thank you.")

        elif choice == 3:
            print(f"\nNumber of Students Enrolled : {Student.total_students}")

        elif choice == 4:
            print("\nTHANKS FOR USING THIS PORTAL.PLEASE COME BACK LATER.\n")
            break

        else:
            print("\nInvalid input : Please enter a valid choice.")
