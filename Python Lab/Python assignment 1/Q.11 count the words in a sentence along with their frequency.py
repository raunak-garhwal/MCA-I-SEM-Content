line=input("Enter a sentence : ")

list=line.split()

frequency_count={}
for i in list:
    if i in frequency_count:
        frequency_count[i]+=1
    else:
        frequency_count[i]=1

print("\n")
print(f"The sentence is :",line)

count=1
for char in line:
    if(char==" "):
        count+=1

print("\n")
print("The total number of words in the sentence are :",count)

print("\n")
print("The frequency of elements in the list :- ")
for key,value in frequency_count.items():
    print(f"{key} -> {value}")