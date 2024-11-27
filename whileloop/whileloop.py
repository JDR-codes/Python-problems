#pgm to rev the given integer
'''
n=int(input('Enter the number:'))
temp=n
rev=0
while temp>0:
    lastdigit=temp%10 #to get the last digit of the number
    rev=(rev*10)+lastdigit
    temp=temp//10 #to remove the last digit of the number
print(rev)
'''
#pgm to find the sum of gn integer
''''
n=int(input('Enter the number:'))
sum=0
temp=n
while temp!=0:
    ld=temp%10
    sum+=ld
    temp=temp//10
print(sum)
'''
#pgm to pd of individual no of the given integer
'''
n=int(input('Enter the number:'))
pd=1
temp=n
while temp!=0:
    ld=temp%10
    pd*=ld
    temp=temp//10
print(pd)
'''
#pgm to print the characters present in the string
'''
s=input('Enter the string:')
l=len(s)
ind=0 # positive index of the string
while ind<l:
    print(s[ind],end='')
    ind+=1 #increasing the index to terminate the loop when the index value greater the len of the string
'''
#pgm to extract the uppercase characters from the string
'''
s=input('Enter the string:')
l=len(s)
i=0
up=''
while i<l:
    if 65<=ord(s[i])<=90:
        up+=s[i]
    i+=1
print(up)     
'''
#pgm to extract the special characters from the entered string
'''
s=input('Enter the string:')
l=len(s)
sc=''
i=0
while i<l:
    if not('0'<=s[i]<='9' or 'a'<=s[i]<='z' or 'A'<=s[i]<='Z'):
        sc+=s[i]
    i+=1
print(sc)
'''
#pgm to extract he numbers from the given string only if the asc key value of the number is even no
'''
s=input('Enter the string:')
no=''
l=len(s)
i=0
while i<l:
    if '0'<=s[i]<='9' and ord(s[i])%2==0:
        no+=s[i]
    i+=1
print(no)
'''
#pgm to print multiplication table
'''
n=int(input('Enter the number:'))
i=1
while i<=10:
    print(f'{n}*{i}={n*i}')
    i+=1
'''
#pgm to revrese the given string without slicing
'''
s=input('Enter the string:')
i=-1
op=''
while i>=-len(s):
    op+=s[i]
    i-=1
print(op)
'''
'''
s=input('Enter the string:')
i=len(s)-1
op=''
while i>=0:
    op+=s[i]
    i-=1
print(op)
'''
'''
s=input('Enter the string:')
i=0
op=''
while i<=len(s)-1:
    op=s[i]+op
    i+=1
print(op)
'''
#pgm to int from gn list
'''
l=eval(input('Enter the list:'))
op=[]
i=0
while i<=len(l)-1:
    if type(l[i])==int:
        # op+=[l[i]]
        op.append(l[i])
    i+=1
print(op)
'''
#pgm to print uc,lc,sc,no from the given string
'''
s=input('Enter the string:')
i=0
uc,lc,sc,no='','','',''
while i<len(s):
    if 'a'<=s[i]<='z':
        lc+=s[i]
    elif 'A'<=s[i]<='z':
        uc+=s[i]
    elif '0'<=s[i]<='9':
        no+=s[i]
    else:
        sc+=s[i]
    i+=1
print(uc,lc,sc,no,sep="\n")
'''
#pgm to extract from the given tuple
'''
t=eval(input('Enter the tuple:'))
i=0
op=()
while i<len(t):
    if type(t[i])==str:
        op+=(t[i],)
    i+=1
print(op)
'''
#pgm to get the following op 'hai_hello_good_morning'
'''
s='hai hello good morning'
i=0
op=''
while i<len(s):
    if 'a'<=s[i]<='z':
        op+=s[i]
    elif s[i]==' ':
        op+='_'
    i+=1
print(op)
'''
#pgm to get the following op {'a':97,'b':98,'c':99,'d':100}
'''
s='abcd'
i=0
op={}
while i<len(s):
    op[s[i]]=ord(s[i])
    i+=1
print(op)
'''
#pgm to get the following op {'true':4,'false':5}
'''
l=[10,7.1,'true','false',7+9j]
i=0
op={}
while i<len(l):
    if type(l[i])==str:
        op[l[i]]=len(l[i])
    i+=1
print(op)
'''
#pgm to get the following op {'python':'pn','sql':'sl','web tech':'wh'}
'''
t=('python',58,'sql',7.7,'web tech',3+5j)
i=0
op={}
while i<len(t):
    if type(t[i])==str:
        op[t[i]]=t[i][0]+t[i][-1]
    i+=1
print(op)
'''
#pgm to get the alphabet letters of the entered number
'''
s=input('Enter the number:')
i=0
op=''
while i<len(s):
    if s[i]=='1':
        op+='one'
    elif s[i]=='0':
        op+='zero'
    elif s[i]=='2':
        op+='two'
    elif s[i]=='3':
        op+='three'
    elif s[i]=='4':
        op+='four'
    elif s[i]=='5':
        op+='five'
    elif s[i]=='6':
        op+='six'
    elif s[i]=='7':
        op+='seven'
    elif s[i]=='8':
        op+='eight'
    elif s[i]=='9':
        op+='nine'
    i+=1
print(op)
'''
'''
n=int(input('Enter the number:'))
d={0:'zero',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
op=''
while n>0:
    ld=n%10
    op=d[ld]+op
    n//=10
print(op)
'''
#pgm to get the following op {0:'p',1:'y',2:'t',3:'h',4:'o',5:'n'}
'''
s='python'
op={}
i=0
while i<len(s):
    op[i]=s[i]
    i+=1
print(op)
'''
#pgm to convert binary to integer
'''
n=1101
op=0
count=0
while n>0:
    ld=n%10
    op=2**count*ld
    count+=1
    n//=10
print(op)
'''
#pgm to convert integer to binary
'''
n=int(input('Enter the integer:'))
i=0
op=0
while n>0:
    bt=n%2
    op=bt*10**i+op
    n//=2
    i+=1
print(op)
'''
#pgm 1 a.first 10 even numbers
'''
i=2
count=1
while count<=10:
    print(i)
    i+=2
    count+=1
'''
#b.first 10 odd numbers
'''
i=1
count=1
while count<=10:
    print(i)
    i+=2
    count+=1
'''
#c.first 10 natural numbers
'''
i=1
count=1
while i<=10:
    print(i)
    i+=1
    count+=1
'''
#d.first 10 whole numbers

'''i=0
count=1
while i<10:
    print(i)
    i+=1
    count+=1
'''
#pgm 2 to print first 10 int and their square 
'''
i=1
count=1
while i<=10:
    print(i,i*2)
    i+=1
    count+=1
''' 
#pgm 3 to print the follwing series
'''
i=10
while i<=300:
    print(i)
    i+=10
'''
#pgm 4 to print the following series
'''
i=105
while i>0:
    print(i,end=",")
    i-=7
'''
#pgm 5 to print first 10 natural no in reverse
'''
i=10
count=1
while count<=10:
    print(i)
    i-=1
    count+=1
'''
#pgm 6 to print sum of first 10 natural no
'''
i=1
sum=0
count=1
while count<=10:
    sum+=i
    i+=1
    count+=1
print(sum)
'''
#pgm 7 to print sum of first 10 even no
'''
i=2
count=1
sum=0
while count<=10:
    sum+=i
    i+=2
    count+=1
print(sum)
'''
#pgm 8 to print table if the no user entered
'''
n=int(input('Enter the number:'))
i=1
while i<=10:
    print(f'{i}X{n}={i*n}')
    i+=1
'''
#pgm 9 to print the even no bt the ennterd two numbers
'''
n1=int(input('Enter the no 1:'))
n2=int(input('Enter the no 2:'))
while n1<=n2:
    if n1%2==0:
        print(n1)
    elif n1%2==1:
        print(n1+1)
    n1+=2
'''

#pgm 11 to print sum of the digits entered by the user
'''
n=int(input('Enter the number:'))
sum=0
while n>0:
    ld=n%10
    sum=sum+ld
    n//=10
print(sum)
'''
#pgm 12 to print product of the digits entered by the user
'''
n=int(input('Enter the number:'))
pd=1
while n>0:
    ld=n%10
    pd=pd*ld
    n//=10
print(pd)
'''
#pgm 13 reverse the user entered number
'''
n=int(input('Enter the number:'))
rv=0
while n>0:
    ld=n%10
    rv=rv*10+ld
    n//=10
print(rv)
'''
#pgm 14 to print the entered number in words
'''
n=int(input('Enter the number:'))
d={0:'one',1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine'}
op=''
while n>0:
    ld=n%10
    op=d[ld]+' '+op
    n//=10
print(op)
'''
#pgm 15 to print fibonacci series
'''
n=int(input('Enter the number:'))
if n==1:
    print(0)
elif n==2:
    print(0)
    print(1)
if n>2:
    fn=0
    print(fn)
    sn=1
    print(sn)
count=2
while count<n:
    tn=fn+sn
    print(tn)
    fn=sn
    sn=tn
    count+=1
'''
#pgm 16 to print factorial of the number
'''
n=int(input('Enter the number:'))
fc=1
count=n
while count>0:
    fc*=count
    count-=1
print(fc)
'''
#pgm 17 to check whether the entered number is armstrong
'''
n=int(input('Enter the no:'))
temp=n
lg=len(str(n))
op=0
while temp>0:
    ld=temp%10
    op+=ld**lg
    temp//=10
if n==op:
    print('Armstrong')
else:
    print('Not armstrong')
'''

# pgm 29 to print all the numbers divisible by 13 and not by 3 between the given numbers
'''
n1=100
n2=500
while n1<=n2:
    if n1%13==0 and n1%3!=0:
        print(n1)
    n1+=1
'''
#pgm 28 to display sum of odd and even numbers between the numbers user enters
'''
n1=int(input('Enter the n1:'))
n2=int(input('Enter the n2:'))
odd=0
even=0
while n1<=n2:
    if n1%2==0:
        even+=n1
    else:
        odd+=n1
    n1+=1
print(odd,even)
'''
#pgm 27 to accept 10 numbers from the users and display the smallest and largest number
'''
count=0
largest=0
smallest=0
while count<10:
    n=int(input('Enter the number:'))
    if largest==0 and smallest==0:
        largest=smallest=n
    else:
        if n<smallest:
            smallest=n
        elif n>largest:
            largest=n
    count+=1
print(largest)
print(smallest)
'''
#pgm 26 accept 10 numbers from the users and display the average
'''
count=0
sum=0
total=0
while count<10:
    n=int(input('Enter the number:'))
    sum+=n
    total+=1
    count+=1
print(sum/total)
'''
#pgm 24 to check the entered integer is palindrome
'''
n=int(input('Enter the number:'))
temp=n
rv=0
while temp<0:
    ld=temp%10
    rv=rv*10+ld
    temp//=10
if temp==n:
    print('palindrome')
else:
    print('Not palindrome')
'''
#pgm 20 to allow user to enter the number untill he enters 0 and display the positive and negative count
'''
pos=0
neg=0
count=1
while count!=0:
    n=int(input('Enter the number:'))
    if n<0:
        neg+=1
    elif n>0:
        pos+=1
    else:
        count=0
print(pos)
print(neg)
'''
#pgm 19
'''
sum=0
count=1
while count!=0:
    n=int(input('Enter the number to add or enter 0 if you want to end and print sum:'))
    if n>0 or n<0:
        sum+=n
    else:
        count=0
print(sum)
'''
#pgm to check whether the entered no is prime or not
'''
n=int(input('Enter the number:'))
if n>1:
    isprime=True
    i=2
    while i<n:
        if n%i==0:
            isprime=False
            break
        i+=1
if isprime==True:
    print('Prime number')
else:
    print('Not a prime number')
'''

#pgm to ck the last two values of the collection is float if it is float add those two values
'''
l=[3,23,65,34,5.3]
i=0
op=0
while i<len(l):
    if i==0 or i==len(l)-1:
        if type(l[i])==float:
            op+=l[i]
        else:
            print('The values are not float')
            break   
    i+=1
else:
    print(op)
'''

#18.pgm to add the first n terms of sereis 1/1!+1/2!....1/n!
'''
n=int(input('Enter n:'))
op=f'1/1!'
i=2
while i<=n:
    op+=f'+ 1/{i}!'
    i+=1
print(op)
'''
#25.pgm to find sum of the following series 1+1/1!+1/2!....1/n!
'''
n=int(input('Enter n:'))
sum=1
i=0
while i<=n:
    fact=1
    while fact<=n:
        fact*=n
        n-=1
    sum+=1/fact
    i+=1
print(sum)
'''
#30.pgm to print the following series till n terms 2,22,222,2222...n 
'''
n=int(input('Enter n:'))
op=''
for i in range(n):
    opp=''
    for j in range(i+1):
        opp+='2'
    print(opp,end=',')
print(op)
'''
#38
'''
ip=[23,45,32,25,46,33,71,90]
for i in ip:
    if i%2!=0:
        print(i)
'''
#39
'''
n=int(input('Enter n:'))
op=[]
for i in range(1,n+1):
    if n%i==0:
        op.append(i)
print(op)
'''
#40
n1=1
n2=49
for i in range(1,n2+1):
    for j in range(n2,n1):
        print(f'{i}___{j}')
