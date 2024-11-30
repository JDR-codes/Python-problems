import csv
# with open('python.csv','w',newline='') as f1:
#     wo=csv.writer(f1)
#     wo.writerow(['Name','Age','Id'])
#     wo.writerows([['Pranesh','24','1'],['Gokul','22','2']])

with open('python.csv','a',newline='') as f1:
    wo=csv.DictWriter(f1,['Name','Age','Id'])
    wo.writerow({'Name':'Santhosh','Age':21,'Id':3})
    wo.writerows([{'Name':'Sridhar','Age':22,'Id':4},{'Name':'Salai','Age':23,'Id':5}])
    # wo=csv.DictReader(f1)
    # print(list(wo))


