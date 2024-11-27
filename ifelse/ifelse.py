#pgm to ck whtr the gn no is even or odd
'''
num=int(input('Enter the number:'))
if num%2==0:
    print(f'{num} is even')
else:
    print(f'{num} is odd')
'''
#pgm to ck whtr the gn data is mutable or immutable
'''
a=eval(input('Enter the data:'))
if type(a) in [list,set,dict]:
    print('Mutable')
else:
    print('Immutable')
'''
#pgm to ck whtr the gn dt is svd or mvd
'''
a=eval(input('Enter the data:'))
if type(a) in [int,float,complex,bool]:
    print('Single value data')
else:
    print('Multi value data')
'''
#pgm to  ck whtr the entered char is special char or not
'''
a=input('Enter the char:')
if not('a'<=a<='z' or 'A'<=a<='Z' or '0'<=a<='9'):
    print('Special character')
else:
    print('Not a special character')
'''
#pgm to ck whtr the gn str having middle value or not
'''
a=input('Enter the string:')
if len(a)%2==0:
    print('Not having middle char')
else:
    print('Having middle character')
'''
#pgm to ck whtr the gn two variables are pointing to the same memory location
'''
a=eval(input('Enter the value 1:'))
b=eval(input('Enter the value 2:'))
if a is b:
    print('Pointing to same memory location')
else:
    print('Pointing to different memory location')
'''
#pgm to ck the first value present inside the gn list is complex or not
'''
list=eval(input('Enter the list:'))
if type(list[0])==complex:
    print('The first value is complex')
else:
    print('The the first value is not complex')
'''
#pgm 41
'''
t=eval(input('Enter the tuple: '))
if type(t[0])==type(t[1]):
    print('The entered tuple is a homogeneous collection')
else:
    print('The entered tuple is a heterogeneous collection')
'''
#pgm to ck whtr the gn int is multiple of 10 or not
'''
a=int(input('Enter the integer:'))
if a%10==0:
    print(f'{a} is multiple of 10')
else:
    print(f'{a} is not a multiple of 10')
'''
#pgm43
'''
a=int(input('Enter the integer:'))
if a%2==0:
    print(a**2)
else:
    print(a**3)
'''
#pgm to ck whtr the gn string is palindrone or not
s=input('Enter the string:')
if s[::-1]==s:
    print('Palindrome')
else:
    print('Not a palindrome')

#pgm 45
'''
s=input('Enter the string:')
if len(s)>3:
    print(len(s))
else:
    print(s)
'''
#pgm to ck whtr the user is eligible to vote or not
'''
age=int(input('Enter the age:'))
if age>=18:
    print('Eligible to vote')
else:
    print('Not eligible to vote')
'''
#pgm to ck whtr the entered no is divisible by 7 or not
'''
n=int(input('Enter the number:'))
if n%7==0:
    print(f'{n} is divisible by 7')
else:
    print(f'{n} is not divisible by 7')
'''
#pgm to ck whtr the last digit of the number is divisible by three or not
'''
n=int(input('Enter the number:'))
last_digit=n%10
if last_digit%3==0:
    print('The last digit of the entered number is divisible by 3')
else:
     print('The last digit of the entered number is not divisible by 3')
'''
#pgm to ck whtr the entered year is a leap year
'''
year=int(input('Enter the year:'))
if year%4==0:
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
'''
#pgm to find largest of two numbers
'''
a=int(input('Enter a:'))
b=int(input('Enter b:'))
if a>b:
    print(f'{a} is greater')
else:
    print(f'{b} is greater')
'''
#pgm to ck whtr the entered no is positive or negative
'''
a=int(input('Enter the number:'))
if a>0:
    print(f'{a} is positive number')
else:
    print(f'{a} is negative number')
'''
#pgm to ck whtr the user ip is divisible by both 2 and 3
'''
a=int(input('Enter the number:'))
if a%2==0 and a%3==0:
    print(f'{a} is divisible by both 2 and 3')
else:
    print(f'{a} is not divisible by both 2 and 3')
'''