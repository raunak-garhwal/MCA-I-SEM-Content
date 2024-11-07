user_input = input('Enter a sentence : ')

lowercase_count=0
uppercase_count=0
digit_count=0
whitespace_count=0
word_count=1

for i in user_input:
    if (i>='a'and i<='z'):
        lowercase_count+=1               
    elif (i>='A'and i<='Z'):
        uppercase_count+=1
    elif (i==' '):
        whitespace_count+=1
        word_count+=1
    elif (i>='0'and i<='9'):
        digit_count+=1
         
print('Number of Lower case letters in the string : ',lowercase_count)
print('Number of Upper case letters in the string : ',uppercase_count)
print('Number of Digits in the string : ',digit_count)
print('Number of Whitespace Characters in the string : ',whitespace_count)
print('Number of words in the string : ',word_count)