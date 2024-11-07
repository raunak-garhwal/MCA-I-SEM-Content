num=int(input("Enter the total number of elements in the list : "))
input_list=[]
for i in range(num):
    value=int(input(f"Enter {i+1} Element : "))
    input_list.append(value)

count_zero=0
count_pos=0
count_neg=0

for i in input_list:
    if(i==0):
        count_zero+=1
    elif(i>0):
        count_pos+=1
    else:
        count_neg+=1

print("\n")
print("The elements in the list :",input_list)
print("\n")
print("Count of zeros :",count_zero)
print("Count of positive numbers :",count_pos)
print("Count of negative numbers :",count_neg)
