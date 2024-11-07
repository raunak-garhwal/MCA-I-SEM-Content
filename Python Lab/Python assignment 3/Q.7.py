class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks

student_list=[]

def add_student():
    name = input("\nEnter Student's Name : ")
    mark = float(input("Enter Student's marks : "))
    student = Student(name,mark)
    student_list.append(student)

def display_student():
    if not student_list:
        print("\nNo Student present in the list.")
    else:
        print("\nList of students :- ")
        for student in student_list:
            print(f"{student.name} : {student.marks}")

if __name__ =="__main__":
    while True:
        try:
            print("\nPlease Enter your choice : ")
            print("1. Add New Student\n2. Display student info\n3. Exit")
            choice = int(input("\nEnter your choice (1-3) : "))
        except:
            print("\nERROR :- Please enter a valid numeric value.")
        else:
            if choice == 1:
                add_student()
            elif choice == 2:
                display_student()
            elif choice == 3:
                print("\nExisting the program.....\n")
                break
            else:
                print("\nInvalid choice. Please enter a valid choice.")