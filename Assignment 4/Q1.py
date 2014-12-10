__author__ = 'user'
# -*- coding: "UTF-8" -*-

f = file('s.txt')
f = open('s.txt', 'r')
s = f.readlines()
#sorted(s, key=lambda s: s[]) '
print s
f2 = open('s1.txt', 'w')
lines = sorted(s, key=lambda lin: lin[0])
f2.write('\n'.join(lines))
f2.close()

print s
f2 = open('s2.txt', 'w')
lines = sorted(s, key=lambda lin: lin[1])
f2.write('\n'.join(lines))
f2.close()

#f2 = open('s3.txt', 'w')
#lines = sorted(s, key=lambda lin: lin[0])
f3 = file('s.txt')
lines = f3.read()
lines = lines.split();
i = 0
result = '';
while i < len(lines):
    if (i != 0 and (i%3)==0):
        result = result +'\n'
    result = result +' '+ lines[i]
    i = i +1

print result






#f2.write('\n'.join(lines))
f2.close()