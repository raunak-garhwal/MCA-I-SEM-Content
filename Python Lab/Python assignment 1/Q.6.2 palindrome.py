def do_reverse(num):
    rev_num=0
    while(num>0):
        digit=num%10
        rev_num=(rev_num*10)+digit
        num=num//10
    return rev_num

def is_palindrome(num):
    if(num==do_reverse(num)):
        return True
    else:
        return False

num=int(input("Enter a number : "))

if(is_palindrome(num)):
    print("The number is a palindrome.")
else:       
    print("The number is not a palindrome.")