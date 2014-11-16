# -*- coding: utf-8 -*-
#임시 7번문제

import urllib
s = urllib.urlopen('http://www.python.org/').read()

a = s.splitlines()
#빈칸 모두 ''로 만들기
for x in range(0, len(a)):
    a[x] = a[x].strip()

count = 0
final_count = len(a)
while count <= final_count:
    if(a[count] == '</html>'):
        break
    if(a[count] == ''):
        a.pop(count)
        final_count = final_count -1
    count = count +1
    
    print count
 

#</li>
#</a>
#</span>
#</h1>
#</label>
#</script>
#</div>
#</ul>



count = 0   
while True:
    if(a[count] == ''):
        a.pop(count)
    count = count+1
    print count,
    if(('/html' in a[count])==True):
        break

i = len(a)         
while count < i:
    if(a[count] == '</html>'):
        break
    a.pop(count)
    count = count+1

for x in range(0, len(a)):    
    start = a[x].find('<')
    last = a[x].find('>')
    a[x] = a[x].split(a[x][start:last+1])
    a[x] = ' '.join(a[x])
    for y in range(0, len(a[x])):
        a[x][y] = a[x][y].strip()
        






#빈칸제거 함수
