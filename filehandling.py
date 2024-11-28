'''This is text filehandling'''
# f=open('txt1.txt','x')
# f.close()


# f1=open('txt2.txt','w')
# f1.write('This is deepakrajan')
# f1.close()

# f1=open('txt2.txt','w')
# f1.writelines(['Hii \n','This is deepakrajan \n'])
# print(f1.readable())
# print(f1.writable())
# f1.close()

# f1=open('txt2.txt','a')
# f1.writelines(['This is file handling \n','We are practicing text file handling \n'])
# f1.close()

# f1=open('txt2.txt')
# # print(f1.read())
# # print(f1.readline())
# print(f1.readlines())
# data=f1.readlines()
# f1.close()

# f2=open('txt3.txt','w+')
# f2.writelines(['This is filehandling \n','We are practicing filehandling \n'])
# f2.seek(0)
# print(f2.read())
# f2.close()


# f3=open('txt3.txt','r+')
# print(f3.read())
# f3.write('This is read + mode ')
# print(f3.read())
# f3.close()


f4=open('txt3.txt','a+')
f4.write('Bye')
f4.seek(0)
print(f4.read())
f4.close()