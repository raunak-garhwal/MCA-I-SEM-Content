a=int(input("Enter first number : "))
b=int(input("Enter second number : "))
c=int(input("Enter third number : "))
if(a>b and a>c):
    print("From the above entered numbers,",a,"is the highest.")
elif(b>a and b>c):
    print("From the above entered numbers,",b,"is the highest.")
else:
    print("From the above entered numbers,",c,"is the highest.")