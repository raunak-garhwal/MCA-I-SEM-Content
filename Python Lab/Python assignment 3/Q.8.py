class Time:
    def __init__(self,hour,minute=0):
        self.hour=hour
        self.minute=minute

    def add_time(self,other):
        if(self.minute+other.minute)>=60:
            print(f"\nTotal time after adding two time :- {(self.hour+other.hour+1)} hr : {(self.minute+other.minute)%60} min")
        else:
            print(f"\nTotal time after adding two time :- {(self.hour+other.hour)} hr : {(self.minute+other.minute)} min")

    def display_time(self):
        print(f"\nTime :- {self.hour} hr : {self.minute} min")

    def display_minute(self):
        print(f"\nTotal minutes :- {(self.hour*60)+self.minute} minutes")


if __name__ == "__main__":
    print("\n--- Welcome to the Python Time Program ---")

    while(True):
        print("\nPress 1 to add two times.\nPress 2 to display time.\nPress 3 to convert time in minutes.\nPress 4 to exit.")

        try:
            choice = int(input("\nEnter your choice : "))
        except:
            print("\nWARNING :- Please enter a valid numeric value. Thank you.")
        else:    
            if choice == 1:
                print("\n- ADDING TWO TIME -")
                h1 = int(input("\nEnter the hour part of the First Time : "))
                m1 = int(input("Enter the minute part of the First Time : "))
                h2 = int(input("\nEnter the hour part of the Second Time : "))
                m2 = int(input("Enter the minute part of the Second Time : "))
                c1=Time(h1,m1)
                c2=Time(h2,m2)
                c1.add_time(c2)

            elif choice == 2:
                print("\n- DISPLAY TIME -")
                h = int(input("\nEnter the hour part of the Time : "))
                m = int(input("Enter the minute part of the Time : "))
                c=Time(h,m)
                c.display_time()

            elif choice == 3:
                print("\n- CONVERTING TIME IN MINUTES -")
                h = int(input("\nEnter the hour part of the Time : "))
                m = int(input("Enter the minute part of the Time : "))
                c=Time(h,m)
                c.display_minute()

            elif choice == 4:
                print("\nTHANKS FOR USING THIS PROGRAM.PLEASE COME BACK LATER.\n")
                break

            else:
                print("\nInvalid input : Please enter a valid choice.")