n=int(input("Enter the total number of element in the list : "))

num_list=[]
even_list=[]
odd_list=[]

for i in range(n):
    value=int(input(f"Enter {i+1} element : "))
    num_list.append(value)    

for i in num_list:
    if(i%2==0):
        even_list.append(i)
    else:
        odd_list.append(i)

print("\n")
print("List of All Numbers :",num_list)
print("List of Even Numbers :",even_list)
print("List of Odd Numbers :",odd_list)
