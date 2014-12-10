# -*- coding: utf-8 -*-
s = """
Its power: Python developers typically report 
they are able to develop applications in a half
to a tenth the amount of time it takes them to do
the same work in such languages as C.
"""
#"id: password, name, school"
test = ["kang: dsdokrer, kes, rer", "koaerko", "12312312#@!"]
f = open('e.txt', 'w+')
'''
if f.read()== None:
    f.write("첫번쨰\n")
    f.write("두번쨰\n")
    f.write("세번째")
else:
    f.write("빈곳처리")


f2 = open('e.txt', 'r')
print len(f2.readline())
print test[0].find(':')+2
print test[0][test[0].find(' ')+1:test[0].find(',')]
'''
'''

password_plain = "my password"
password_encrypted = sha.new(password_plain).hexdigest()
print password_encrypted
f2 = open('e.txt', 'w+')
f2.write(password_encrypted)
f2.write(password_plain)
'''
test = ["kang: dsdokrer, kes, rer", "korea: dsdokrer, kes, rer", "kans: dsdokrer, kes, rer"]
i = 0
for x in test:
    x = x+" added"
    print x

for x in range(len(test)):
    print x

def subStringId(info):
    return info[:info.find(':')]

def checkForId(id, database):
    i = 0
    for x in database:
        x = subStringId(x)
        database[i] = x
        i = i + 1
    #print database
    #id 존재 True 반환, 비존재 False 반환
    if (id not in database):
        return False
    else:
        return id

#print checkForId("kng", test)
import sha
password_plain = "my password"
password_encrypted = sha.new(password_plain).hexdigest()
#print password_encrypted
#f2 = open('e.txt', 'w+')
#f2.write(password_encrypted)
#f2.write(password_plain)
s = "kang: dsdokrer, kes, rer"
print s.find(', ')
print s.rfind(',')
print s.find('kes')
print s.rfind('kes')
print s[s.find(',')+2: s.rfind(',')]
