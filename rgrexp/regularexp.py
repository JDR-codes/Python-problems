import re
'''Findall() inbuilt'''
# string='hi pranesh is also called as praneshh,praneshhh,pranes'
# var=re.findall('pranesh',string)
# print(var)

'''Finditer() inbuilt'''
# string='hi pranesh is also called as praneshh,praneshhh,pranes'
# var=re.finditer('pranesh',string)
# print(var)

'''search() inbuilt'''
# string='hi pranesh is also called as praneshh,praneshhh,pranes'
# var=re.search('pranesh',string)
# print(var)

'''sub() substring'''
# string='hi pranesh is also called as praneshh,praneshhh,pranes'
# var=re.sub('pranesh','santhosh',string)
# print(var)

'''Qantifier . '''
# string='hi pranesh is also called as pranashh,pranrshhh,pranes'
# var=re.findall('pran.sh',string)
# print(var)

'''Qantifier ? '''
# string='hi pranesh is also called as praneshh,praneshhh,pranes'
# var=re.findall('pranesh?',string)
# print(var)

'''Qantifier * '''
# string='hi pranesh is also called as praneshh,praneshhh,pranes'
# var=re.findall('pranesh*',string)
# print(var)

'''Char class []'''
# string='hi pranesh is also called as pranashh,pranrshhh,prangshhhhh'
# var=re.findall('[ae]',string)
# print(var)

'''Startswith  ^char'''
# string='hi pranesh is also called as praneshh,praneshhh,pranes'
# var=re.findall('^hi',string)
# print(var)

'''Endswith 'chr$' '''
# string='hi pranesh is also called as praneshh,praneshhh,pranes'
# var=re.findall('es$',string)
# print(var)

'''Negation [^ ]'''
string='hi pranesh is also called as praneshh,praneshhh,pranes'
var=re.findall('[^ae]',string)
print(var)