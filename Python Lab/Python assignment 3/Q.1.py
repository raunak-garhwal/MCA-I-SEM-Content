def student_biodata():
    global stud_name,stud_class,stud_section
    stud_name=input("Enter the Name of the student : ")
    stud_class=input("Enter the Class of the student : ")
    stud_section=input("Enter the Section of the student : ")
    student_mark()

def student_mark():
    global e,h,m,sc,sst,stud_percent,stud_remark
    try:
        e=float(input("Enter marks in English : "))
        h=float(input("Enter marks in Hindi : "))
        m=float(input("Enter marks in Maths : "))
        sc=float(input("Enter marks in Science : "))
        sst=float(input("Enter marks in Social-Science : "))
    except:
        print("\nWARNING :- PLEASE ENTER NUMERIC MARKS.\n")
    else:
        if(e>100 or h>100 or m>100 or sc>100 or sst>100):
            print("\nERROR :- CHECK THE MARKS ENTRY!\nPLEASE ENTER THE MARKS IN VALID RANGE(BETWEEN 0 AND 100)\n")
        elif (e>40 and h>40 and m>40 and sc>40 and sst>40):
            student_remark()
        else:
            stud_percent = "NA"
            stud_remark = "FAIL(Note :- Individual Subject Marks below 40)"
            student_result()

def student_remark():
    global stud_percent,stud_remark
    stud_percent=(e+h+m+sc+sst)/5
    if(0<stud_percent<45):
        stud_remark = "FAIL(Note :- Overall Percentage below 45%)"
        student_result()
    else:
        stud_remark = "PASS"
        student_result()

def student_result():
    print("\n--- STUDENT DETAILS ---")
    print("Name :",stud_name)
    print("Class :",stud_class)
    print("Section :",stud_section)
    print("Percentage :",stud_percent)
    print("Remark :",stud_remark,"\n")

if __name__ == "__main__":
    print("\n--- WELCOME TO THE STUDENT RESULT DECLARATION PORTAL ---\n")
    student_biodata()