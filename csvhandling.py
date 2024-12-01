import csv
# with open('python.csv','w',newline='') as f1:
#     wo=csv.writer(f1)
#     wo.writerow(['Name','Age','Id'])
#     wo.writerows([['Pranesh','24','1'],['Gokul','22','2']])

# with open('python.csv','a',newline='') as f1:
#     wo=csv.DictWriter(f1,['Name','Age','Id'])
#     wo.writerow({'Name':'Santhosh','Age':21,'Id':3})
#     wo.writerows([{'Name':'Sridhar','Age':22,'Id':4},{'Name':'Salai','Age':23,'Id':5}])
#     # wo=csv.DictReader(f1)
    # print(list(wo))

with open('stuinfo.csv','w',newline='') as f1:
    wo=csv.writer(f1)
    wo.writerow(['Name','Id','Phno','Class'])


class Student_info:
    def __init__(self,name,id,phno,Class):
        self.name=name
        self.id=id
        self.phno=phno
        self.Class=Class
        with open('stuinfo.csv','a',newline='') as f1:
            ro=csv.writer(f1)
            ro.writerow([name,id,phno,Class])
    def display(self,cls):
        with open('stuinfo.csv') as f1:
            ro=csv.reader(f1)
            for i in ro:
                if cls in i:
                    print(i)

s1=Student_info('pranesh',1,345,12)
s2=Student_info('gokul',2,643,12)
# s1.display(12)

# with open('stuinfo.csv') as f1,open('infocopy.csv','w') as f2:
#     ro=csv.DictReader(f1)
#     wo=csv.DictWriter(f2,['Name','Phno'])
#     wo.writeheader()
#     for i in ro:
#         i.pop('Id')
#         i.pop('Class')
#         wo.writerow(i)