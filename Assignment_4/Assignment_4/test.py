lines = ['first line\n', 'second line\n', 'third line\n']
f = open('t1.txt', 'w')
f.write(''.join(lines))

f = open('t1.txt') #�б�
print f.read()
print f.read()
f.close()