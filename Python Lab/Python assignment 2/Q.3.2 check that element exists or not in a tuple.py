n = int(input("Enter the size of the tuple : "))
my_list = [] 
my_tuple = ()

# Taking input for the tuple
for i in range(n):
    value = int(input(f"Enter {i+1} value : "))
    my_list.append(value)

element = int(input("Enter the element to search in the tuple : "))

my_tuple = tuple(my_list)
element_found = False

# Searching for the element in the tuple
for j in my_tuple:
    if j == element:
        element_found = True
        break

# Checking and printing the result
if element_found:
    print(f"{element} is present in the tuple.")
else:
    print(f"{element} is not present in the tuple.")