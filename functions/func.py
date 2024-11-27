#pgm to get the op='nohtyp lqs hectbew'
'''
def rev(ip):
    op=''  
    b=ip.split()
    for i in range(0,len(b)):
        op+=b[i][::-1]+' '
    return op
print(rev('python sql webtech'))
'''
#pgm to print the op if user enters a string and if the individual value is lowercase chage it to uppercase or if it is uppercase change it to lowercase or if it is space print -
'''
n='No CLasS oN SaTurDaY'
def conv(ip):
    op=''
    for i in ip:
        if 'A'<=i<='Z':
            # op+=i.lower() op+=chr(ord(i)+32)
        elif 'a'<=i<='z':
            # op+=i.upper() op+=chr(ord(i)-32)
        elif i==' ':
            op+='-'
    return op
print(conv(n))
'''
#pgm to get following op [[200,300],[300,700],[500,500],[1000]]
'''
l=[200,300,500,1000,800,700]
val=1000
def comb(l,val):
    op=[]
    for i in l:
        if i==val and [i] not in op:
            op.append([i])
        else:
            for j in l :
                if i+j==val and [i,j] not in op and [j,i] not in op:
                        op.append([i,j])
    return op
print(comb(l,val))
'''
#pgm to write implementation of is lower function
'''
s='hAi'
def lower(s):
    for i in s:
        if 'A'<=i<='Z':
            return False
    return True
print(lower(s))
'''
#pgm to write implementation of reverse function
'''
l=[1,2,3,4,5]
def Reverse(l):
    for i in range(len(l)):
        a=l.pop()
        l.insert(i,a)
Reverse(l)
print(l)
 '''
#func to print the repeated chair present in each string in the given list
'''
l=['chair','air','hai','chain','hair']
def comb(l):
    op=''
    for i in range(len(l[0])):
        for j in range(len(l[0])):
            a=l[0][i:j+1]
            for k in l:
                if a not in k:
                    break
            else:
                if len(a)>len(op):
                    op=a
    return op
print(comb(l))
'''
#func to perform operations based on user requirements
'''
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def values():
    a=int(input('a:'))
    b=int(input('b:'))
    return a,b 
def calculator():
    while True:
            print('Enter 1 for addition,Enter 2 for subtraction,Enter 3 for multiplication,Enter 4 for division,Enter 0 to end')
            code=int(input('Enter code:'))
            if code==1:
                a,b=values()
                print(add(a,b))
            elif code==2:
                a,b=values()
                print(sub(a,b))
            elif code==3:
                a,b=values()
                print(mul(a,b))
            elif code==4:
                a,b=values()
                print(div(a,b))
            elif code==0:
                print('End ')
                break
            else:
                print('Invalid code')

calculator()
'''
#func to  perform addition for min two values and max 5 values
'''
def add(a,b,c=0,d=0,e=0):
    return a+b+c+d+e
print(add(3,9))
print(add(3,9,1))
print(add(3,9,3,4))
print(add(3,5,1,6,7))
'''

#func to implementation of slicing
'''
def slicing(s,si=0,ei=8,up=2):
    for i in s:
        if type(s) in [str,list,tuple]:
            return s[si:ei:up]
print(slicing('python'))
'''

#func to extract even no from list
'''
def even(l):
    op=[]
    for i in l:
        if type(i)==int and i%2==0:
            op.append(i)
    return op
print(even([1,2,'3',4,5]))
'''