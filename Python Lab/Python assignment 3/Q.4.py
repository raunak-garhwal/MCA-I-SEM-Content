class Shapes:
    def calculate_perimeter(self):
        pass
    def calculate_area(self):
        pass

class Rectangle(Shapes):
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)
    def calculate_area(self):
        return self.length * self.width
    
class Circle(Shapes):
    def __init__(self,radius):
        self.radius=radius
    def calculate_perimeter(self):
        return 2 * 3.141592653589793 * self.radius
    def calculate_area(self):
        return 3.141592653589793 * self.radius**2

class Square(Shapes):
    def __init__(self,side):
        self.side=side
    def calculate_perimeter(self):
        return 4 * self.side
    def calculate_area(self):
        return self.side**2 

class Triangle(Shapes):
    def __init__(self,side1,side2,side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
    def calculate_perimeter(self):
        return self.side1 + self.side2 + self.side3
    def calculate_area(self):
        s = (self.side1 + self.side2 + self.side3)/2
        return (s*(s - self.side1)*(s - self.side2)*(s - self.side3))**0.5
    
print("\n--- WELCOME TO THE PYTHON SHAPES PROGRAM ---")

while(True):

    print("\nPress 1 to calculate area and perimeter of Rectangle.\nPress 2 to calculate area and perimeter of Circle.\nPress 3 to calculate area and perimeter of Square.\nPress 4 to calculate area and perimeter of Triangle.\nPress 5 to exit.")

    try:
        choice = int(input("\nEnter your choice : "))
    except:
        print("\nWARNING :- Please enter a valid numeric value. Thank you.")
    else:    
        if choice == 1:
            a=float(input("\nEnter Length of the Rectangle : "))
            b=float(input("\nEnter Breadth of the Rectangle : "))
            r=Rectangle(a,b)
            print("\nPerimeter of Rectangle :- ",r.calculate_perimeter(),"units")
            print("Area of Rectangle :- ",r.calculate_area(),"square units")

        elif choice == 2:
            a=float(input("\nEnter Radius of the Circle : "))
            c=Circle(a)
            print("\nPerimeter of Circle :- ",c.calculate_perimeter(),"units")
            print("Area of Circle :- ",c.calculate_area(),"square units")
        
        elif choice == 3:
            a=float(input("\nEnter Side of the Square : "))
            s=Square(a)
            print("\nPerimeter of Square :- ",s.calculate_perimeter(),"units")
            print("Area of Square :- ",s.calculate_area(),"square units")

        elif choice == 4:
            a=float(input("\nEnter First Side of the Triangle : "))
            b=float(input("\nEnter Second Side of the Triangle : "))
            c=float(input("\nEnter Third Side of the Triangle : "))
            t=Triangle(a,b,c)
            print("\nPerimeter of Triangle :- ",t.calculate_perimeter(),"units")
            print("Area of Triangle :- ",t.calculate_area(),"square units")

        elif choice == 5:
            print("\nTHANKS FOR USING THIS PROGRAM.PLEASE COME BACK LATER.\n")
            break

        else:
            print("\nInvalid input : Please enter a valid choice.")