#pgm to get hte following op {'python':6,'class':5}
'''
ip='python class'.split()
op={}
for i in ip:
    count=0
    for j in i:
        count+=1
    op[i]=count
print(op)
'''
#pgm to get the following op no of consonants {'python':5,'class':4}
'''
ip='python class'.split()
op={}
for i in ip:
    count=0
    for j in i:
        if j not in 'aeiouAEIOU':
            count+=1
    op[i]=count
print(op)
'''
#pgm to get the following op {0:('python',6),1:('is',2),2:('easy',4)}
'''
ip='python is easy'.split()
op={}
for i in range(len(ip)):
    count=0
    for j in ip[i]:
        count+=1
    op[i]=(ip[i],count)
print(op)
'''
#pgm to get the following op 'b2i1g2 1o1s2'
'''
ip='bigg boss'
op=''
for i in ip:
    count=0
    for j in ip:
        if i==j:
            count+=1
    if i not in op:
        op+=i+str(count)
print(op)
'''



#pattern programming
#pgm to print square
'''
n=int(input('Enter the number:'))
for i in range(n):
    for j in range(n):
        print('*',end='')
    print()
'''
#pgm to print lower triangle
'''
n=int(input('Enter no:'))
for i in range(n):
    for j in range(n):
        if i>j or i==j:
            print('*',end='')
    print()
'''
#pgm to print higher triangle 
'''
n=int(input('Enter no:'))
for i in range(n):
    for j in range(n):
        if i>j:
            print(' ',end='')
        elif i<j or i==j:
            print('*',end='')
    print()
'''
#pgm to print primary diagonal
'''
n=int(input('Enter no:'))
for i in range(n):
    for j in range(n):
        if i==j:
            print('*',end='')
        elif i>j:
            print(' ',end='')
    print()
'''
#pgm to print secondary diagonal
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i+j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print() 
'''
#pgm 
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i+j<n:
            print('*',end='')
    print()
'''
#pgm 
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i+j>=n or i+j==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''
#pgm to print hollow square
'''
***
* *
***
n=int(input('Enter n:'))
for i in range(n):
    for j in range (n):
        if j==0 or i==0 or j==n-1 or i==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''

# pgm to print hollow triangle
'''
n=int(input('Enter n:'))
m=n*2-1
for i in range(n):
    for j in range(m):
        if i+j==n-1 or i==n-1 or j-i==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''
#pgm to print triangle
'''
n=int(input('Enter n:'))
m=n*2-1
for i in range(n):
    for j in range(m):
        if i+j<n-1 or j-i>n-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()
'''
#pgm to print inverted hollow triangle
'''
n=int(input('Enter n:'))
m=n*2-1
for i in range(n):
    for j in range(m):
        if i==0 or i==j or i+j==m-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''
#pgm to print inverted triangle
'''
n=int(input('Enter n:'))
m=n*2-1
for i in range(n):
    for j in range(m):
        if i>j or i+j>m-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()
'''
#pgm to print rhombus
'''
n=int(input('Enter n:'))
m=n*2-1
for i in range(n):
    for j in range(m):
        if i+j<n-1 or j-i>n-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()
for i in range(n):
    if i==0:
        continue
    for j in range(m):
        if i>j or i+j>m-1:
            print(' ',end='')
        else:
            print('*',end='')
    print()
'''
#pgm to print hollow rhombus
'''
n=int(input('Enter n:'))
m=n*2-1
for i in range(n):
    for j in range(m):
        if i+j==n-1 or j-i==n-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(n):
    if i==0:
        continue
    for j in range(m):
        if i==j or i+j==m-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
'''
#pgm to print a
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print b
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if (i==0 and j<n-1) or (i==n-1 and j<n-1) or j==0 or (j==n-1 and i>0 and i<n-1) or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print() 
'''
#pgm to print c
'''
n=int(input('Enter n:'))
for i in range (n):
    for j in range(n):
        if (i==0 and j!=0) or (j==0 and i>0 and i<n-1) or (i==n-1 and j>0 ) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print d
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if (i==0 and j<n-1) or j==0 or (i==n-1 and j<n-1) or (j==n-1 and i>0 and i<n-1):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print e
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print f
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print g
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or i==n-1 or (i==n//2 and j>=n//2) or (j==n-1 and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print h
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if  j==0  or i==n//2 or j==n-1:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print i
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==n//2:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print k
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if j==0 or (i==n//2 and j<=n//2) or (i+j==n-1 and j>=n//2) or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print m
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or (i==j and j<=n//2) or (i+j==n-1 and i<=n//2) :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print q
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0 or j==n-1 or i==n-1 or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print r
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i==0 or j==0  or i==n//2 or (j==n-1 and i<=n//2) or (i==j and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print s 
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or i==n//2 or (j==0 and i<=n//2) or (j==n-1 and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print w
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if  j==0 or j==n-1 or (i==j and i>=n//2) or (i+j==n-1 and j<=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm to print y
'''
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if  (i==j and i<=n//2) or (i+j==n-1 and j>=n//2) or (j==n//2 and i>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()
'''
#pgm 
'''
1
22
333
4444
55555
n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i>=j:
            print(i+1,end=' ')
    print()
'''

#pgm 
'''
1
23
345
4567
56789
n=int(input('Enter n:'))
for i in range(n):
    for j in range (n):
        if i>=j:
            print(i+1+j,end='')
    print()
'''   
#pgm
'''
A
AB 
ABC
ABCD
n=int(input('Enter n:'))
for i in range(65,65+n):
    for j in range (65,i+1):
        print(chr(j),end=' ')
    print()
'''

#pgm
'''
54321
 5432
  543
   54
    5

n=int(input('Enter n:'))
for i in range(n):
    k=n
    for j in range(n):
        if i<=j :
            print (k,end='')
            k-=1
        else:
            print(' ',end='')
    print()
'''
#pgm 
'''
12345
 1234        
  123
   12
    1
n=int(input('Enter n:'))
for i in range (n):
    k=0
    for j in range(n):
        if j>=i:
            print(k+1,end='')
            k+=1
        else:
            print(' ',end='')
    print()
'''
# pgm
'''
12345
1234
123
12
1

n=int(input('Enter n:'))
for i in range(n):
    for j in range(n):
        if i+j<n:
            print(j+1,end='')
        else:
            print(' ',end='')
    print()
'''
#pgm
'''
54321
4321
321
21
1
not working
n=int(input('Enter n:'))
for i in range(n):
    k=n
    for j in range(n):
        if i+j<n:
            print(k,end='')
            k-=1
        else:
            print(' ',end='')
    k-=1
    print()
'''
#pgm 
'''
n=int(input('Enter n:'))
m=n*2-1
for i in range(n):
    k=0
    for j in range(m):
        if i+j<n-1 or j-i>n-1:
            print(' ',end='')
        else:
            print(k+1,end='')
            k+=1
    print()
'''