#pgm to get the following op 'a4b2c2d1'
#a
ip='aabcbadca'
'''
op=''
for i in range(0,len(ip)):
    if ip[i] not in op:
        op=op+ip[i]+str(ip.count(ip[i]))
print(op)
'''
#b
'''
op=''
count=1
for i in range(0,len(ip)-1):
    if ip[i]==ip[i+1]:
        count+=1
    else:
        op+=ip[i]+str(count)
    count=1
op+=ip[i+1]+str(count)
print(op)
'''
#pgm to extract string dsta item from the tuple
'''
t=eval(input('Enter the tuple:'))
op=()
for i in t:
    if type(i)==str:
        op+=(i,)
print(op)
'''
#pgm to extract integer from the list if the int is a palindrome
'''
l=eval(input('Enter the list:'))
op=[]
for i in l:
    if type(i)==int:
        if str(i)==str(i)[::-1]:
            op.append(i)
print(op)
'''
#pgm to extract values from dict if type of both key and value are same
'''
d=eval(input('Enter the dictionary:'))
op={}
for i in d:
    if type(i)==type(d[i]):
        op[i]=d[i]
print(op)
'''
#pgm to find the length of the collection without using len function
'''
c=eval(input('Enter the collection:'))
count=0
for i in c:
    count+=1
print(count)
'''
#pgm to extract complex data from the given tuple
'''
t=eval(input('Enter the tuple:'))
op=()
for i in t:
    if type(i)==complex:
        op+=(i,)
print(op)
'''
#pgm to generate uppercase alphabets from A-Z
'''
op=''
for i in range(65,91):
    op+=chr(i)
print(op)
'''
#pgm to get the following op {'python':6,'is':2,'easy':4}
'''
ip='python is easy'
op={}
b=ip.split()
for i in b:
    op[i]=len(i)
print(op)
'''
#pgm to find the longest substring from the given string
'''
s=input('Enter the string:')
b=s.split()
largest=b[0]
for i in b:
    if len(i)>len(largest):
        largest=i
print(largest)
'''
#pgm to get the following op ['py',db','html']
'''
ip=['python.py','sql.db','program.html']
op=[]
for i in ip:
    b=i.split('.')
    op.append(b[-1])
print(op)
'''
#pgm to get the following op {'py':'python','db':database','html':'program'}
'''
ip=['python.py','sql.db','program.html']
op={}
for i in ip:
    b=i.split('.')
    op[b[-1]]=b[0]
print(op)
'''
#pgm  to get the following op {'py':['python','file'],'com':['instagram','facebook']}
'''
ip=['python.py','file.py','instagram.com','facebook.com']
op={}
for i in ip:
    b=i.split('.')
    if b[-1] not in op:
        op[b[-1]]=[b[0]]
    else:
        op[b[-1]].append(b[0])    
print(op)   
'''
#pgm to get the following op {'a':2,'b':3,'c':1,'d':2}
'''
ip='abbcadbd'
op={}
for i in ip:
    if i not in op:
        op[i]=ip.count(i)
print(op)
'''
#pgm to extract key and value pair from a dictionary if it is a string
'''
d=eval(input('Enter the dictionary:'))
op={}
for i in d:
    if type(i)==str:
        op[i]=d[i]
print(op)
'''
#pgm to get the following op {'a':0,'b':1,'c':2,'d':3}
'''
ip='abcd'
op={}
for i in range(0,len(ip)):
    op[ip[i]]=i
print(op)
'''
#pgm to guess the number
#break statement example---
'''
n=99
while True:
    no=int(input('Enter the number to guess:'))
    if no>n:
        print('Enter a smaller number')
    elif no<n:
        print('Enter a higher number')
    else:
        print('Correct number')
        break
'''
#pgm to chect prime number
'''
n=int(input('Enter the number:'))
for i in range(2,n):
    if n%i==0:
        print('Not a prime number')
        break
else:
    print('Prime number')
'''
