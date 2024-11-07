n=int(input("Enter the size of the tuple : "))
temp_list=[]
org_tup=()

for i in range(n):
    value=int(input(f"Enter {i+1} element : "))
    temp_list.append(value)

org_tup = tuple(temp_list)
print(f"Original Tuple is {org_tup}.")

# Item to be removed
item_to_remove = int(input("Enter the element to be removed from the tuple : "))

# Create a new tuple without the specified item
new_tup = tuple(item for item in org_tup if item != item_to_remove)

print(f"New Tuple is {new_tup}.")