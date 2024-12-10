import sqlite3

conn_obj=sqlite3.connect('A16.db')
cur_obj=conn_obj.cursor()
cur_obj.execute('''CREATE TABLE IF NOT EXISTS A16(
                ID NUMBER(5) PRIMARY KEY,
                NAME VARCHAR(15) NOT NULL,
                PHNO NUMBER(10) UNIQUE CHECK(LENGTH(PHNO)=10) NOT NULL,
                GENDER VARCHAR(10) NOT NULL,
                DEGREE VARCHAR(15) NOT NULL)''')

class Students:
    def __init__(self,id,name,phno,gender,degree):
        cur_obj.execute('INSERT OR IGNORE INTO A16 VALUES(?,?,?,?,?)',(id,name,phno,gender,degree))
        conn_obj.commit()

    def display(self):
        name=input('Enter name:')
        var0=cur_obj.execute('SELECT * FROM A16 WHERE NAME = ?',(name,))
        var1=var0.fetchall()
        if len(var1)==0:
            print('The value is not available')
        elif len(var1)==1:
            print(var1)
        elif len(var1)>1:
            print('The name has duplicate values enter phno:')
            phno=int(input('Enter phno:'))
            var2=cur_obj.execute('''SELECT * FROM A16
                            WHERE PHNO = ?''',(phno,))
            print(var2.fetchone())
    
    def update(self):
        pass

o1=Students(1,'pranesh',7685945678,'male','Msc')
o1=Students(2,'gokul',9475978345,'male','Bca')
o1=Students(4,'gokul',9475978345,'male','Bca')
o1=Students(5,'gokul',8675849599,'male','Bca')
o1=Students(3,'santhosh',8795867789,'male','Bsc')
# o1.display()
var=cur_obj.execute('SELECT * FROM A16')
print(var.fetchall())
# o1.display()

