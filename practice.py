'''class library:
    limit=5
    books={'python':10,'django':8,'sql':10,'javascript':5,'java':3,'c++':4}
    def __init__(self,name,deptname,year):
        self.Name=name
        self.Deptname=deptname
        self.Year=year
        self.book=[]
    def info(self):
        print(self.Name,self.Deptname,self.Year,self.book,sep='\n')
    def issue_book(self,*a):
        if len(self.book)<self.limit:
            for i in a:
                if i not in self.book:
                    if i in self.books and self.books[i]>0 :
                        self.book.append(i)
                        self.books[i]-=1
                        print('Book issued')
                    else:
                        print('Requested book not available')
                else:
                    print('Book already issued')
    def return_book(self,*b):
        for i in b:
            if i in self.books and i in self.book:
                self.book.remove(i)
                self.books[i]+=1
                print('Book returned')
            else:
                print('Book does not belong to the library or the book was not issued to you')


pranesh=library('pranesh','cse','4 year')
gokul=library('gokul','ece','4 year')
pranesh.info()
print('*'*10)
gokul.info()
pranesh.issue_book('python','java')
pranesh.info()
library.books
pranesh.return_book('python')
pranesh.info()
library.books
pranesh.return_book('python')'''


'''
class flipkart:
    pds={'iphone15':[70000,10],'iphone15plus':[89000,15],'iphone15pro':[95000,5],'iphone15promax':[125000,4]}
    def __init__(self,name,loc,phno):
        self.Name=name
        self.Location=loc
        self.Phoneno=phno
        self.Cart={}
    def cust_info(self):
        print(self.Name,self.Location,self.Phoneno,self.Cart,sep='\n')
    @classmethod
    def disp_pds(cls):
        print(cls.pds)
    def add_to_cart(self):
        print(self.pds)
        prod=input('Enter the product you want to add to cart:')
        quantity=int(input('Enter the no of product:'))
        if prod in self.pds and self.pds[prod][-1]>0:
            if prod not in self.Cart and quantity<=self.pds[prod][-1]:
                self.Cart[prod]=[self.pds[prod][0]*quantity,quantity]
                self.pds[prod][-1]-=quantity
                print('Product added to cart')
            elif quantity<=self.pds[prod][-1]:
                self.Cart[prod][0]+=self.pds[prod][0]*quantity
                self.Cart[prod][-1]+=quantity
                self.pds[prod][-1]-=quantity
                print('Product added to cart')
            else:
                print(f'Sorry currently we have {self.pds[prod][-1]} quantities')
        else:
            print('Requested product is not available or out of stock')
        
    def rmv_frm_cart(self):
        print(self.Cart)
        prod=input('Enter the product you want to remove from cart:')
        quantity=int(input('Enter the no of product:'))
        if prod in self.Cart:
            if quantity<=self.Cart[prod][-1]:
                self.Cart[prod][-1]-=quantity
                self.pds[prod][-1]+=quantity
                self.Cart[prod][0]-=self.pds[prod][0]*quantity
                if self.Cart[prod][-1]==0:
                    self.Cart.pop(prod)
                    print('Product removed from your cart')
            else:
                print(f'Sorry currently you have {self.Cart[prod][-1]}')
        else:
            print('The product not in your cart')
    def total_amt(self):
        print(self.Cart)
        tt_amt=0
        quantity=0
        for i in self.Cart:
            tt_amt+=self.Cart[i][0]
            quantity+=self.Cart[i][-1]
        print(f'Total quantity of products is {quantity}')
        print(f'Total amount is {tt_amt}')


        
pranesh=flipkart('pranesh','erode',9785765468)
pranesh.cust_info()

pranesh.disp_pds()
pranesh.add_to_cart()
pranesh.cust_info()'''

'''

class Instagram:
    d={'deepak':['12345',7956314789]}


    def __init__(self):
        n=int(input('Enter 1 to log in or 2 to sign up:'))
        if n==1:
            self.login()
        else:
            self.signup()


    def login(self):
        username=input('Enter username:')
        if username in self.d:
            
            while True:
                password=input('Enter password:')
                if self.d[username][0]==password:
                    print('Loged In')
                    break
                else:
                    print('--You entered wrong password--')
                    fp=int(input('Forget password,to reset password enter 1 or to re enter password enter 2:'))
                    if fp==1:
                        self.ch_pwd()
                    else:
                        password=input('Enter the correct password:')
        else:
            print('--User name is not registered--')
            no=int(input('If you want to register enter 1 or to login again enter 2:'))
            if no==1:
                self.signup()
            else:
                self.login()
    def signup(self):
        username=input('Enter username:')
        if username not in self.d:
            phone_no=int(input('Enter the mobile number:'))
            password=input('Enter the password:')
            confirm_password=input('Enter the confirm password:')
            while True:
                if password==confirm_password:
                    self.d[username]=[password,phone_no]
                    print('Signed In')
                    break
                else:
                    print('--You entered wrong confirm password--')
                    confirm_password=input('Enter the correct confirm password:')
        else:
            print('--The username is already registered--')
            num=int(input('If you want to log in enter 1 or to sign up again enter 2:'))
            if num==1:
                self.login()
            else:
                self.signup()
    def ch_pwd(self):
        username=input('Enter the username:')
        phone_no=int(input('Enter your registered phone number to verify:'))
        if self.d[username][-1]==phone_no:
            np=input('Enter the new password:')
            self.d[username]=[np,phone_no]
            print('--Password updated--')
        else:
            print('The phone number you entered does not match')
                

o1=Instagram()
o1.d
       '''     
'''
def Positive(func):
    def wrapper(*a,**b):
        var=func(*a,**b)
        if var<0:
            print(abs(var))
        else:
            print(var)
    return wrapper
@Positive
def sub(a,b):
    return a-b
sub(20,10)'''

'''
count={}
def Count(func):
    def wrapper(*a,**b):
        func(*a,**b)
        if func.__name__ not in count:
            count[func.__name__]=1
        else:
            count[func.__name__]+=1
        print(f'The no of times the function {func.__name__} executed is {count[func.__name__]}')
    return wrapper
@Count
def add(a,b):
    print(a+b)

@Count
def sub(a,b):
    print(a-b)

sub(9,3)
sub(10,2)
sub(35,21)

add(8,3)
add(5,4)
'''
'''
def ExceptionHandler(func):
    def wrapper(count=0,*a,**b):
        try:
            func(*a,**b)
        except Exception as error:
            print(f'Error Found:{error}')
            wrapper(count+1)
        else:
            
            print(f'no. of errors handled in {func.__name__} is {count}')
    return wrapper
@ExceptionHandler
def add():
    c=int(input('Enter a:'))
    d=int(input('Enter b:'))
    print(c+d)



@ExceptionHandler
def div():
        a=int(input('enter a:'))
        b=int(input('enter b:'))
        print(a/b)
add()
div()'''


b=[{'id':1,'a':'Events app under construction'},{'id':2,'a':'Authors app under construction'}]
print(b[1]['a'])



