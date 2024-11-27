#pgm to check whether the entered number is a perfect number or not
'''
a=int(input('Enter the number:'))
count=1
sum=0
while count<a:
    if a%count==0:
        sum+=count
    count+=1
if a==sum:
    print('Perfect number')
else:
    print('Not a perfect number')
'''
#pgm to get the following op 4
'''
ip1='11001010'
ip2='01110010'
i=0
count=0
while i<len(ip1):
    if ip1[i]==ip2[i]:
        count+=1
    i+=1
print(count)
'''
#pgm to check whether the given number is xylem number or not
'''
n=int(input('Enter the number:'))
n1=str(n)
op1=0
op2=0
i=0
while i<len(n1):
    if i==0 or i==len(n1)-1:
        op1+=int(n1[i])
    else:
        op2+=int(n1[i])
    i+=1
if op1==op2:
    print('Xylem number')
else:
    print('Not a xylem number')
'''
#pgm to remove duplicate value from list without converting to set
'''
l=eval(input('Enter the list:'))
i=0
op=[]
while i<len(l):
    if l[i] not in op:
        op.append(l[i])
    i+=1
print(op)
'''
#pgm to find the longest substring without repeating characters in a given string using while loop

#1
'''

n=int(input('Enter n:'))
m=n*2-1
for i in range(n):
    for j in range(m):
        if j==0 or i==j or i+j==m-1 or i==n-1 or j==m-1 or i>=j or i+j>=m-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
for i in range(n):
    if i==0:
        continue
    for j in range(m):
        if i+j<n-1 or j-i>n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

#6
'''
ip=[12,35,1,10,34,1]
fg=ip[0]
sg=ip[0]
for i in ip:
    if i>fg:
        fg=i
    elif i>sg and i!=fg:
        sg=i
print(sg)
''' 

#2
'''
ip='just looking like wow'
si=int(input('Enter starting index:'))
ei=int(input('Enter ending index:'))
op=''
for i in range(len(ip)):
    if si<=i<=ei:
        op+=ip[i].upper()

    else:
        op+=ip[i]
print(op)
'''
#3
'''
ip=[1,2,3,[2,65,4],[9,6],'gi']
op=[]
for i in range(len(ip)):
    if type(ip[i])==list and len(ip[i])%2!=0:
        mv=len(ip[i])//2
        if type(ip[i][mv])==int and ip[i][0]%2==0:
            op.append(ip[i])
print(op)
'''
#7
'''
s=input('Enter the string:')
op=''
for i in range(len(s)):
    for j in range(i+1,len(s)):
        if s[i]==s[j] and s[i] not in op:
            op+=s[i]
print(op)
'''

#8
'''
st='The cat sat on the mat. The cat meowed'
def cnt(st):
    s=st.split()
    op={}
    for i in range(len(s)):
        count=0
        for j in range(len(s)):
            if s[i]==s[j]:
                count+=1
        op[s[i]]=count  
    return op
print(cnt(st))
'''
#4
'''
n=int(input('Enter n:'))
m=n*2-1
k=0
for i in range(n):
    for j in range(m):
        if i+j<n-1 or j-i>n-1:
            print(' ',end=' ')
        else:
            print(k+1,end=' ')
            k+=1
    print()
'''

# #5
# var=lambda a:a**3
# n=int(input('Enter number:'))
# var1=map(var,range(1,n+1))
# var2=filter(lambda b: True if b<n else False,var1)
# print(list(var2))




def ExceptionHandler(func):
    def wrapper(count=0,*a,**b):
        try:
            func(*a,**b)
        except Exception as error:
            print(f'Error Found:{error}')
            add(count+1)
        else:
            print(count)
    return wrapper
@ExceptionHandler
def add():
    a=int(input('Enter a:'))
    b=int(input('Enter b:'))
    print(a+b)

add()