#pgm to ck the relation bt 2 int
'''
a=int(input('Enter a:'))
b=int(input('Enter b:'))
if a>b:
    print(f'{a} is greater')
elif a<b:
    print(f'{b} is greater')
elif a==b:
    print(f'{a} and {b} are equal')
else:
    print('There is no relation')
'''
#pgm to ck gn char is uc ,lc,no
'''
a=input('Enter the char:')
if 'a'<=a<='z':
    print('Lowercase')
elif 'A'<=a<='Z':
    print('Uppercase')
elif '0'<=a<='9':
    print(ord(a))
else:
    print('Special character')
'''
#pgm 56
'''
a=input('Enter the character:')
list=[]
if a in 'aeiouAEIOU':
    list.append(a)
    print(list)
elif a not in 'aeiouAEIOU':
    print(ord(a))
'''
#pgm 57
'''
a=input('Enter the character:')
if a.islower():
    print('Lowercase')
elif a.isupper():
    print('lowercase=',a.lower())
'''
#pgm58
'''
a=input('Enter the character:')
if '0'<=a<='9':
    print(ord(a))
elif 'a'<=a<='z':
    print('Lowercase')
elif 'A'<=a<='Z':
    print('Uppercase')
'''
#pgm 59
'''
a=input('Enter the character:')
if 'A'<=a<='Z':
    print(a.lower())
elif 'a'<=a<='z':
    print(a.upper())
elif not('A'<=a<='Z' or 'a'<=a<='z' or '0'<=a<='9'):
    print(ord(a)+8)
'''
#pgm to ck whtr the last char of gn str is a sp char
'''
a=input('Enter the string:')
l_d=a[-1]
if not ('A'<=l_d<='Z' or 'a'<=l_d<='z' or '0'<=l_d<='9'):
    print('Special character')
'''
#pgm to ck whtr the mv of the heyero tup is int or not
'''
t=eval(input('Enter the tuple:'))
m_v_i=len(t)//2
m_v=t[m_v_i]
if type(m_v)==int:
    print('integer')
elif type(m_v)==float:
    print('float')
elif type(m_v)==complex:
    print('complex')
elif type(m_v)==bool:
    print('bool')
'''
#pgm to ck whtr the gn dt is ind dt
''''
a=eval(input('Enter the data:'))
if type(a)==int:
    print('Individual datatype')
elif type(a)==float:
    print('Individual datatype')
elif type(a)==complex:
    print('Individual datatype')
elif type(a)==bool:
    print('Individual datatype')
else:
    print('Not an individual datatype')
'''
#pgm to ck whtr the entered int is sd or td ot thd
'''
a=int(input('Enter the integer:'))
if 0<=a<=9 or -1>=a>=-9:
    print('Single digit')
elif 10<=a<=99 or -10>=a>=-99:
    print('Two digit')
elif 100<=a<=999 or -100>=a>=-999:
    print('Three digit')
else:
    print('Greater than three digit')
'''
#pgm 64
'''
a=int(input('Enter the number:'))
if a%3==0 and a%5==0:
    print('fizzbuzz')
elif a%3==0:
    print('Fizz')
elif a%5==0:
    print('Buzz')
'''
#pgm to prt the grade based on result
'''
r=eval(input('Enter the result:'))
if 301<=r<=400:
    print('c grade')
elif 401<=r<=500:
    print('B grade')
elif 501<=r<=600:
    print('A grade')
else:
    print('D grade')
'''
#pgm to fd the greatest among 2 no
'''
a=int(input('Enter a:'))
b=int(input('Enter b:'))
if a>b:
    print('a is greater')
elif a<b:
    print('b is greater')
else:
    print('Both are equal')
'''
#pgm to fd the greatest among 4 no
'''
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
d=int(input('Enter d:'))
if a>b and a>c and a>d:
    print('a is greater')
elif b>c and b>d:
    print('b is greater')
elif c>d:
    print('c is greater')
else:
    print('d is greater')
'''
#pgm to fd the smallest among 4 no
'''
a=int(input('Enter a:'))
b=int(input('Enter b:'))
c=int(input('Enter c:'))
d=int(input('Enter d:'))
if a<b and a<c and a<d:
    print('a is smaller')
elif b<c and b<d:
    print('b is smaller')
elif c<d:
    print('c is smaller')
else:
    print('d is smaller')
'''
#pgm 71
'''
nou=eval(input('Enter the number of units:'))
if 1<=nou<=100:
    print(f'There is no electricty bill for {nou} units ')
elif 101<=nou<=200:
    print(f'The electricity bill bill for {nou} is',nou*5)
elif 201<=nou<=349:
    print(f'The electricity bill for {nou} units is',nou*10)
elif nou==350:
    print(f'The electricity bill for {nou} is 2000 rs')
'''
#pgm 72
'''
m=eval(input('Enter the mark:'))
p=float(m)
if p>90:
    print('A grade')
elif 80<=p<=90:
    print('B grade')
elif 60<=p<=80:
    print('C grade')
else:
    print('D grade')
'''
#pgm 73
'''
price=eval(input('Enter the price:'))
if price>100000:
    print(f'The road tax to be paid for {price} is ',price*50/100)
elif 50000<=price<=100000:
    print(f'The road tax to be paid for {price} is ',price*10/100)
elif price<=50000:
    print(f'The road tax to be paid for {price} is ',price*5/100)
'''
#pgm to prt the days according to the entered number
'''
n=int(input('Enter he number from 1 to 7:'))
if n==1:
    print('Sunday')
elif n==2:
    print('Monday')
elif n==3:
    print('Tuesday')
elif n==4:
    print('Wednesday')
elif n==5:
    print('Thursday')
elif n==6:
    print('Friday')
elif n==7:
    print('Saturday')
'''
#pgm 75
'''
a=int(input('Enter the number from 1 to 12:'))
if a==1:
    print('January and no of days is 31')
elif a==2:
    print('Febraury and no of days is 30')
elif a==3:
    print('March and no of days is 31')
elif a==4:
    print('April and no of days is 30')
elif a==5:
    print('May and no of days is 30')
elif a==6:
    print('June and no of days is 31')
elif a==7:
    print('July and no of days is 31')
elif a==8:
    print('August and no of days is 31')
elif a==9:
    print('September and no of days is 30')
elif a==10:
    print('October and no of days is 31')
elif a==11:
    print('November and no of days is 31')
elif a==12:
    print('December and no of days is 30')
'''
#pgm 76 
'''
cty=input('Enter the any of the city Delhi,Agra,Jaipur:')
if cty.lower()=='delhi':
    print(f'The monuments of {cty} is Red Fort')
elif cty.lower()=='agra':
    print(f'The monuments of {cty} is Taj-Mahal')
elif cty.lower()=='jaipur':
    print(f'The monuments of {cty} is Jal-Mahal')
'''
#pgm 77
'''
sd1=eval(input('Enter the side 1:'))
sd2=eval(input('Enter the side 2:'))
sd3=eval(input('Enter the side 3:'))
if sd1==sd2==sd3:
    print('Equilateral triangle')
elif sd1==sd2 or sd2==sd3 or sd1==sd3:
    print('Isosceles triangle')
else:
    print('Scalene triangle')
'''
#pgm 78
'''
nod=int(input('Enter the number of days:'))
if nod<=5:
    print(f'The charge for {nod} is ',nod*2)
elif 6<=nod<=10:
    print(f'The charge for {nod} is ',nod*3)
elif 11<=nod<=15:
    print(f'The charge for {nod} is ',nod*4)
else:
    print(f'The charge for {nod} is ',nod*5)
'''
#pgm 79
'''
km=int(input('Enter the kilometers:'))
if km<=10:
    print(f'Bill for {km} is {km*11}')
elif 11<=km<=100:
    print(f'Bill for {km} is {km*10}')
elif km>=101:
    print(f'Bill for {km} is {km*9}')
'''
#pgm convert temp from celsius to kelvin and kelvin to celsius
temp=int(input('Enter the temperature:'))
if temp <0:
    print('celsius')
    print(f'The kelvin of the temperature is {temp+273.15}')
elif 0<=temp<=373:
    print('Kelvin')
    print(f'The celsius of the temperature is {temp-273.15} ')