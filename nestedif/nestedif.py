#pgm to crt an instagram login page
'''
user_name=eval(input('Enter the username:'))
password=eval(input('Enter the password:'))
u_n='deepakrajan'
pwd='password'
if user_name==u_n:
    if password==pwd:
        print('Loged in')
    else:
        print('Wrong password')
else:
    print('Invalid username')
'''
#pgm 82
'''
t=eval(input('Enter the heterogeneous tuple:'))
m_i=len(t)//2
m_v=t[m_i]
if type(m_v)==str:
    if len(m_v)>3:
        print(f'{m_v} is the middle value')
    else:
        print('The length of the middle value is not greater then three')
else:
    print('The middle value is not a string')
'''
#pgm to print greatest amomg 4 no
'''
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
d=int(input('Enter d:'))
if a>b:
    if a>c:
        if a>d:
            print('a is greater')
        else:
            print('d is greatest')
    else:
        if c>d:
            print('c is greater')
        else:
            print('d is greater')
else:
    if b>c:
        if b>d:
             print('b is greater')
        else:
            print('d is greatest')
    else:
        if c>d:
            print('c is greater')
        else:
            print('d is greater')
'''

#pgm to ck the type of the char
'''
a=input('Enter the character:')
if len(a)==1:
    if 'A'<=a<='Z' or 'a'<=a<='z':
        print('Alaphabets')
    else:
        if '0'<=a<='9':
            print('Numbers')

        else:
            print('Special characters')
'''
#pgm 86
'''
a=int(input('Enter the integer:'))
if a%2==0:
    print('Happy')
else:
    if a%5==0 and a%7==0:
        print('Sad')
        print(a**2)
    else:
        print(a)
'''
#pgm 88
'''
a=input('Enter the string:')
rv=a[::-1]
if a==rv:
    print(a)
else:
    if len(a)%2==0:
        print(rv)
    else:
        if len(a)%2!=0:
            print(a[1::2])
'''
#pgm 89
'''
a=input('Enter the string:')
m_i=len(a)//2
m_c=a[m_i]
if len(a)%2!=0:
    if a.isupper():
        print(m_c)
    else:
        print('Lowercase')
else:
    print('Does not contain middle character')
'''
#pgm 90
'''
a=input('Enter the character:')
if 'a'<=a<='z' or 'A'<=a<='Z':
    if a in 'aeiouAEIOU':
        print('Vowels')
    else:
        print('Consonants')
else:
    print('Not alphabets')
'''

#PGM to second greatest among 4 numbers
'''
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
d=int(input('Enter d:'))
if a>b and a>c and a>d:
    if b>c and b>d:
        print('b is greater')
    elif c>d:
        print('c is greater')
    else:
        print('d is greater')
elif b>c and b>d:
    if a>c and a>d:
        print('a is greater')
    elif c>d:
        print('c is greater')
    else:
        print('d is greater')
elif c>d:
    if b>a and b>d:
        print('b is greater')
    elif a>d:
        print('a is greater')
    else:
        print('d is greater')
else:
    if a>c and a>b:
        print('a is greater')
    elif c>b:
        print('c is greater')
    else:
        print('b is greater')
'''
#pgm 94
'''
age=int(input('Enter the age:'))
day=input('Enter the day:')
if 18<=age<=65:
    if day.lower()!='tuesday':
        print('Movie ticket price is 10$')
    else:
        print('Movie ticket price is 12$')
elif age<18:
    if day.lower()!='tuesday':
        print('Movie ticket price is 6$')
    else:
        print('Movie ticket price is 8$')
else:
    print('Movie ticket price is 8$')
'''
#pgm leap year checker 95
'''
year=int(input('Enter the year to check:'))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print(f'{year} is a leap year')
        else:
            print(f'{year} is not a leap year')
    else:
        print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
'''
#pgm 96
# p_c=int(input('Enter the code:'))
# a_p=float(input('Enter the amount paid:'))
# d={768495:250.0,576945:350.0}
# if p_c==d.keys():
#     if a_p==d[768495]:
#         print(d[768495])

#pgm  97
'''
d_o_w=input('Enter the day:')
p_s=int(input('Enter the party size:'))
if d_o_w not in ['saturday','sunday']:
    if p_s<4:
        print('No discount')
    else:
        if p_s>=4:
            print('10 percentage discount')
else:
    print('15 percentage discount')
'''
#pgm 98
'''
l1=int(input('Enter the length 1:'))
l2=int(input('Enter the length 2:'))
if l1==l2:
    print('Square')
else:
    if l1==l2+l2 or l2==l1+l1:
        print('Rectangle')
    else:
        print('Not a rectangle and square')
'''
#pgm 99
'''
sd1=int(input('Enter the side 1:'))
sd2=int(input('Enter the side 2:'))
sd3=int(input('Enter the side 3:'))
if sd1==sd2==sd3:
    print('Equilateral')
else:
    if sd1==sd2 or sd2==sd3 or sd3==sd1:
        print('Isoseles')
    else:
        print('Scalene')
'''
#pgm 100

