num=int(input("Enter a number : "))
temp=num
sum=0
while(num>0):
    digit=num%10
    sum+=digit
    num//=10

print("The sum of digits of",temp,"is",sum)