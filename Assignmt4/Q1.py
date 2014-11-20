__author__ = 'user'
# -*- coding: UTF-8 -*-

f = file('s.txt')
f = open('s.txt', 'r')
s = f.readlines()

#sorted(s, key=lambda s: s[]) '
#1번문제

f2 = open('s1.txt', 'w')
lines = sorted(s, key=lambda lin: lin[0])
f2.write(''.join(lines))
f2.close()
f2 = open('s1.txt', 'r')
print "1-1번문제 파일에서 읽어와 출력"
print f2.read()
f2.close()

#2번문제

f2 = open('s2.txt', 'w')
lines = sorted(s, key=lambda lin: lin[1])
f2.write(''.join(lines))
f2 = open('s2.txt', 'r')
print "1-2번문제 파일에서 읽어와 출력"
print f2.read()
f2.close()


#1-3번문제
f2 = open('s.txt', 'r')
lines = f2.read()
lines = lines.split();

i = 0
result = '';
first = 1
while i < len(lines):

    if i == 0:
        result = result+lines[i]
        i += 1
        continue
    elif (i%3==0):
        result = result +'\n'
        result = result+lines[i]
        i += 1
        continue

    result = result+' '+lines[i]
    i = i +1

f2.close()
f2 = open('s3.txt', 'w')
f2.write(result)
f2 = open('s3.txt', 'r')
print "1-3번 소문제 파일에서 읽어와 출력"
print f2.read()
f2.close()
