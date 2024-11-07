def linear_search(my_list,target_value):
    n=len(my_list)
    for j in range(n):
        if my_list[j] == target_value:
            return j
    return -1

n=int(input("Enter the number of elements in the list : "))

my_list=[]

for i in range(n):
    value=int(input(f"Enter {i+1} element : "))
    my_list.append(value)

print(f"\nElements in the list are {my_list}")
         
target_value = int(input("\nEnter the element to search in the list : "))

result = linear_search(my_list,target_value)

if result == -1:
    print(f"\nElement {target_value} not found in the list.\n")
else:
    print(f"\nElement {target_value} found at index {result}.\n")
