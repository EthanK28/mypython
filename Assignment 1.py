# -*- coding: utf-8 -*-
#1번
"""
a = "Hello Python"
a = a[6:] +' '+ a[0:6]
print a
"""

#2번
"""
b = "Hello Python"
b = b[5:] +' '+ b[0:6]
b = 'World'+b
print b
"""

#3번
"""
c
"""

#4번
"""
s="python"
print s[0]
print s[0][0]
print s[0][0][0]
print s[-100]
print s[100]
s[1:-1]
s[3:-3]
"""
#5번
'''
for x in range(1,101):
    if(x%2 == 1):
        print x,
    else:
        continue

#6번
sum = 0
a = 2
while a<=100:
    sum += a
    a += 2
print sum
'''
#7번
#정수 입력
print '정수입력?: ' 
num = int(raw_input())

x = 2
isPrime = True
if num == 2:
    print 2

for n in range(2, num):
    isPrime=True
    for a in range(2, n):
        if n % a == 0:
            isPrime=False            
        else:
            continue        
    if isPrime is True:s
        print n,

        
        



    
    
        

#1은 소수가 아니므로 2부터 시작


