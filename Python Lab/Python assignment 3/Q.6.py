class Operation:
    def __init__(self,f_num,s_num):
        self.f_num=f_num
        self.s_num=s_num

    def add(self):
        print("\nResult after Addition(+) :",self.f_num+self.s_num)

    def sub(self):
        print("\nResult after Subtraction(-) :",self.f_num-self.s_num)

    def mul(self):
        print("\nResult after Multiplication(*) :",self.f_num*self.s_num)

    def div(self):
        print("\nResult after Division(/) :",self.f_num/self.s_num)

    def mod(self):
        print("\nResult after Modulus(%) :",self.f_num%self.s_num)


print("\nWHAT OPERATION WOULD YOU LIKE TO PERFORM")

while(True):

    print("\nPress 1 to input the Numbers.\nPress 2 for addition(+).\nPress 3 for subtraction(-).\nPress 4 for multiplication(*).\nPress 5 for division(/).\nPress 6 for Modulus(%).\nPress 7 to exit.")

    try:
        choice = int(input("\nEnter your choice : "))
    except:
        print("\nWARNING :- Please enter a valid numeric value. Thank you.")
    else:    
        if choice == 1:
            a=float(input("\nEnter first number : "))
            b=float(input("\nEnter second number : "))
            obj=Operation(a,b)

        elif choice == 2:
            try:
                obj.add()
            except:
                print("\nWARNING :- Please enter the numbers first. Thank you.")
        
        elif choice == 3:
            try:
                obj.sub()
            except:
                print("\nWARNING :- Please enter the numbers first. Thank you.")

        elif choice == 4:
            try:
                obj.mul()
            except:
                print("\nWARNING :- Please enter the numbers first. Thank you.")
        
        elif choice == 5:
            try:
                obj.div()
            except:
                print("\nWARNING :- Please enter the numbers first. Thank you.")
        
        elif choice == 6:
            try:
                obj.mod()
            except:
                print("\nWARNING :- Please enter the numbers first. Thank you.")

        elif choice == 7:
            print("\nTHANKS FOR USING THIS PROGRAM.PLEASE COME BACK LATER.\n")
            break

        else:
            print("\nInvalid input : Please enter a valid choice.")