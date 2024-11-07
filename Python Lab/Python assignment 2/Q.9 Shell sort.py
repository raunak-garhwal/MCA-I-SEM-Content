def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i

            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap

            arr[j] = temp

        gap //= 2


num = int(input("Enter the number of elements in the list: "))
arr = []

for i in range(num):
    value = int(input(f"Enter element {i + 1} : "))
    arr.append(value)

print("Before Sorting :", arr)

shell_sort(arr)

print("After Sorting :", arr)
