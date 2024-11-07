def binary_search(my_list, target_value):

    start = 0
    end = len(my_list) - 1

    while start <= end:
        mid = (start + end) // 2
        mid_value = my_list[mid]

        if mid_value == target_value:
            return mid  # Element found, return its index
        elif mid_value < target_value:
            start = mid + 1  # Discard the left half
        else:
            end = mid - 1  # Discard the right half

    return -1  # Element not found in the list

n=int(input("Enter the number of elements in a list : "))

my_list=[]

for i in range(n):
    value=int(input(f"Enter {i+1} element : "))
    my_list.append(value)

target_value = int(input("Enter the element to search in the list : "))

print(f"Original list : {my_list}")

# sorting the list:
my_list.sort()

print(f"Sorted list : {my_list}")

result = binary_search(my_list, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print(f"Element {target_value} not found in the list.")