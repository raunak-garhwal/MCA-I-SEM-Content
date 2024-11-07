n=int(input("Enter the size of the tuple : "))
list=[]
tup=()
replist=[]

for i in range(n):
    value=int(input(f"Enter {i+1} value : "))
    list.append(value)

tup = tuple(list)

for i in tup:
    if (tup.count(i))>1:
        if i not in replist:
            replist.append(i)   
                  
print("The repeated items are",replist)