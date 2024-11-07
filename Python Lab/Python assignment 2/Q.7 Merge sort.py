def merge_sort(my_list):
    if len(my_list) > 1:
        # Divide the my_list into two halves
        mid = len(my_list) // 2
        left_half = my_list[:mid]
        right_half = my_list[mid:]

        # Recursively sort each half
        merge_sort(left_half)
        merge_sort(right_half)

        # Merge the sorted halves
        merge(my_list, left_half, right_half)

def merge(my_list, left, right):
    i = j = k = 0

    # Compare elements from both halves and merge them
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            my_list[k] = left[i]
            i += 1
        else:
            my_list[k] = right[j]
            j += 1
        k += 1

    # Copy the remaining elements, if any, from the left half
    while i < len(left):
        my_list[k] = left[i]
        i += 1
        k += 1

    # Copy the remaining elements, if any, from the right half
    while j < len(right):
        my_list[k] = right[j]
        j += 1
        k += 1

num=int(input("Enter the number of elements in the list : "))
my_list=[]

for i in range(num):
    value=int(input(f"Enter {i+1} element : "))
    my_list.append(value)


print(f"Before Sorting : {my_list}")

merge_sort(my_list)

print(f"After Sorting : {my_list}")