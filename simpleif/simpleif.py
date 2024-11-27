#pgm1
'''
location=input('Enter the location:')
if location.lower()=="bangalore":
    print('The company is registered')
'''
#program to check whether the given number is even
'''
num=int(input('Enter the number:'))
if num%2==0:
    print(f'{num} is even')
'''
#program to check whether the given number is odd
'''
num=int(input('Enter the number:'))
if num%2!=0:
    print('even')
'''
#pgm4
'''
num=int(input('Enter the number:'))
if 5<=num<=10:
    print(f'{num} lies between 5 and 10')
'''
#program to the num of char is greater than three
'''
string=input('Enter the sting:')
if len(string)>3:
    print(f'{string} has more than three characters')
'''
#program to check the given number is having 4 digits
'''
num=int(input('Enter the number:'))
if 1000<=num<=9999:
    print(f'The {num} has four digits')
'''
#program to check whether the given charcter is vowel or not
'''
a=input('Enter the character:')
if a in 'aeiouAEIOU':
    print(f'{a} is a vowel')
'''
#pgm to ck whtr the gn integer is even and multiple of 5
'''
num=int(input('Enter the integer:'))
if num%2==0 and num%5==0:
    print(f'{num} is an even number and divisible by 5')
'''
#pgm to ck whtr the given sting is char 
'''
string=input('Enter the string:')
if len(string)==1:
    print(f'{string} is a character')
'''
#pgm to ck whtr the given string is uppercase
'''
string=input('Enter the string:')
if string.isupper():
    print(f'{string} is a uppercase')
'''
#pgm to ck whtr the given string is lowercase
'''
string=input('Enter the string:')
if string.islower():
    print(f'{string} is a lowercase')
'''
#pgm to ck whtr the given string is a digit
'''
string=input('Enter the char:')
if '0'<=string<='9':
    print(f'{string} is a digit')
'''
#pgm to ck whtr the given char is alphabet
'''
a=input('Enter the character:')
if 'a'<=a<='z' or 'A'<=a<='Z':
    print(f'{a} is a alphabet')
'''
#pgm to ck whtr the given char is a special character
'''
a=input('Enter the character:')
if not('a'<=a<='z' or 'A'<=a<='Z'):
    print(f'{a} is a special character')
'''
#pgm to ck whtr the gn coll is a list
'''
coll=eval(input('Enter the collection:'))
if type(coll)==list:
    print('The given coll is a list')
'''
#pgm to ck whtr the entered value is default
'''
a=eval(input('Enter the value:'))
if bool(a)==False:
    print(f'{a} is a default value')
'''
#pgm to  ck whtr the list consists of the even no of values
'''
a=eval(input('Enter the list:'))
if len(a)%2==0:
    print(f'{a} consist of even number of values')
'''
#pgm  to ck whtr the gn sting consits of middle value
'''
list=eval(input('Enter the list:'))
if len(list)%2!=0:
    print('The list consist of a middle value')
'''
#pgm to ck whtr the entered input is immutable
'''
a=eval(input('Enter the value:'))
if type(a) not in [list,set,dict]:
    print('The entered value is immutable')
'''
#pgm to ck whtr the entered input is mutable
'''
a=eval(input('Enter the value:'))
if type(a) in [list,set,dict]:
    print('The entered value is mutable')
'''
#pgm to ck whtr the entered ip is svdt
'''
a=eval(input('Enter the input:'))
if type(a) in [int,float,complex,bool]:
    print('The entered input is a single value data type')
'''
#pgm to ck whtr the entered ip is mvdt
'''
a=eval(input('Enter the input:'))
if type(a) not in [int,float,complex,bool]:
    print('The entered input is a multi value data type')
'''
#pgm to ck whtr the entered no exactly having one digit

num=int(input('Enter the number:'))
if 0<=num<=9:
    print('Single digit')