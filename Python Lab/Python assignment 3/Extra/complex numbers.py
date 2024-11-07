class Complex:
    def __init__(self,real,imag):
        self.real=real
        self.imag=imag
    
    def display(self):
        return(f"{self.real} + {self.imag}i")

    def add(self,other):
        print(f"\nComplex Number after Addition :- {self.real+other.real} + {self.imag+other.imag}i")

    def sub(self,other):
        print(f"\nComplex Number after Subtraction :- {self.real-other.real} + {self.imag-other.imag}i")

    def mul(self,other):
        print(f"\nComplex Number after Multiplication :- {(self.real*other.real)-(self.imag*other.imag)} + {(self.imag*other.real)+(self.real*other.imag)}i")


real_value1=int(input("\nEnter the real value of the 1st complex number : "))
imag_value1=int(input("Enter the imaginary value of the 1st complex number : "))
c1=Complex(real_value1,imag_value1)
print("\nFirst Complex Number :",c1.display())

real_value2=int(input("\nEnter the real value of the 2nd complex number : "))
imag_value2=int(input("Enter the imaginary value of the 2nd complex number : "))
c2=Complex(real_value2,imag_value2)
print("\nSecond Complex Number :",c2.display())

print("\nWHAT OPERATION WOULD YOU LIKE YOU PERFORM")


while(True):

    print("\nPress 1 to add the two complex numbers.\nPress 2 to subtract the two complex numbers.\nPress 3 to multiply the two complex numbers.\npress 4 to exit.")

    try:
        choice = int(input("\nEnter your choice : "))
    except:
        print("\nWARNING :- Please enter a valid numeric value. Thank you.")
    else:    
        if choice == 1:
            c1.add(c2)

        elif choice == 2:
            c1.sub(c2)

        elif choice == 3:
            c1.mul(c2)

        elif choice == 4:
            print("\nTHANKS FOR USING THIS PROGRAM.PLEASE COME BACK LATER.\n")
            break

        else:
            print("\nInvalid input : Please enter a valid choice.")
