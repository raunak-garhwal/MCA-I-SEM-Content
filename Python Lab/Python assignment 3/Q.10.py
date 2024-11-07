class Student:
    def __init__(self,name,age,roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def display_student_info(self):
        print("\n---Student Info---")
        print("\nName :-", self.name)
        print("Age :-", self.age)
        print("Roll no. :-", self.roll_no)

class MCA(Student):
    def __init__(self,name,age,roll_no,course,sem,duration):
        super().__init__(name,age,roll_no)
        self.course = course
        self.sem = sem
        self.duration = duration

    def display_mca_info(self):
        super().display_student_info()
        print("Course :-", self.course)
        print("Semester :-", self.sem)
        print("Duration :-", self.duration)

class Result(MCA):
    def __init__(self,name,age,roll_no,course,sem,duration,marks,per):
        super().__init__(name,age,roll_no,course,sem,duration)
        self.marks = marks
        self.per = per
        
    def display_result(self):
        super().display_mca_info()
        print("Marks :-", self.marks)
        print("Percentage :-", self.per)
        
if __name__ == "__main__":
    n = input("\nEnter Student's Name : ")
    a = int(input("Enter Student's Age : "))
    r = int(input("Enter Student's Roll no. : "))
    c = input("Enter Student's Course Name : ")
    s = input("Enter Student's semester : ")
    d = int(input("Enter Course Duration : "))
    m = int(input("Enter Student's total marks : "))
    p = m/5
    s1=Result(n,a,r,c,s,d,m,p)

    s1.display_result()
    print("\n")
    
    