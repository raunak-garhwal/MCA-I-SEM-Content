n=int(input("Enter the total number of elements to be added : "))
sum=0
for i in range(n):
    value=int(input(f"Enter {i+1} number : "))
    sum+=value
print("The Sum is",sum)