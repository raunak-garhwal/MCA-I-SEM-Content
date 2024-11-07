def selection_sort(list,n):
    for i in range(n-1):
        min_idx=i
        for j in range(i+1,n):
            if list[j] < list[min_idx]:
                min_idx=j

        list[i],list[min_idx] = list[min_idx],list[i]


num=int(input("Enter the number of elements in the list : "))
my_list=[]

for i in range(num):
    value=int(input(f"Enter {i+1} element : "))
    my_list.append(value)


print(f"Before Sorting : {my_list}")

selection_sort(my_list,num)

print(f"After Sorting : {my_list}")