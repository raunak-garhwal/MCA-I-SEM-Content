n=int(input("Enter the total number of element in the list : "))

if(n>0):
    input_list=[]
    for i in range(n):
        value=input(f"Enter {i+1} element : ")
        input_list.append(value)
    frequency_count={}
    for i in input_list:
        if i in frequency_count:
            frequency_count[i]+=1
        else:
            frequency_count[i]=1

    print("\n")
    print("The frequency of elements in the list :- ")
    for key,value in frequency_count.items():
        print(f"{key} -> {value}")

else:
    print("The list is empty, Please enter a valid number greater than 0")