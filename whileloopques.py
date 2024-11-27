'''def ext(n,sum=0,i=1):
    if i>n:
        return sum
    sum+=i
    return ext(n,sum,i=i+1)
print(ext(10))

def pd_of_nat_no(n,pd=1,i=1):
    if i>n:
        return pd
    pd*=i
    return pd_of_nat_no(n,pd,i=i+1)
print(pd_of_nat_no(10))

'''
def rev_int(n,op=0):
    if n<=0:
        return op
    ld=n%10
    op=op*10+ld
    return rev_int(n//10,op)
print(rev_int(153))


