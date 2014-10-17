# -*- coding: utf-8 -*-
def printQNum(i):
    print i+"문제"



#L=[1, 2, 3, 4, 5]일 때 다음 각 문장을 수행한 후의 결과를 보고 납득할 만한 이유를 설명하시오.\
L=[1, 2, 3, 4, 5]
#1)

L[1:3] = [100]
print L
#2)
L[1:3] = [(100)]
print L
#3)
'''
L[1:3] = 100
print L
#4)
L[1:3] = (100)
print L
'''
#5)
L[1:3] = (100, 101, 102)
print L
#6)
L[1:3] = [100, 101, 102]
print L
#7)
L[1:3] = [(100, 101, 102)]
print L
#8)
L[1:3] = [[100, 101, 102]]
print L

# -*- coding: utf-8 -*-
#2번과제
#문자열 S = 'Hello World and Python'에 대해 다음 요구사항에 대한 Python 코드를 제시하시오.
#1) 단어의 순서가 역순으로 되어진 문자열 ('Python and World Hello')을 만들고
#2) 1)의 결과 문자열에 대해 메소드 split과 join을 이용하여 공백을 모두 없엔 문자열 'PythonandWorldHello'을 만드시오.
S = 'Hello World and Python'
print S[::-1]
S = S[16:] + S[11:16] + S[6:12] + S[:6]
print S

#3번과제 
a = [1, 2, 3]
b = a * 3
c = [a] * 3
print b
print c

a[0]=0
print b
print c

#4번 과제
#다음 문자열을 ':'을 기준으로 분리하여 리스트로 만들고 각 문자열의 좌우 공백을 제거하시오 (즉, 문자열 S에서 l을 만들어라)
s = '  first star   :   second star   :    third star  '


s = s.split(':')
print s
for x in range(0,len(s)):
    s[x] = s[x].strip()
    
print s

#5번과제
'''다음과 같이 0보다 큰 정수 리스트 변수 list를 인자로 받는 함수 addall(list)와 addallodd(list)를 for ~ in 리터널과 리스트 내포 방식으로 각각 제시하시오.
1) addall(list) 함수 (리스트 내의 모든 정수를 더하는 함수로서 해답으로는 for ~ in 리터럴과 리스트 내포 방식으로 각각 제시하시오.)
>>> addall([1])
1
>>> addall([1, 2, 3, 4, 5, 6, 7, 8, 9])
45
2) addallodd(list) 함수 (리스트내의 모든 홀수를 더하는 함수로서 해답으로는 for ~ in 리터럴과 리스트 내포 방식으로 각각 제시하시오.)
>>> addallodd([1])
1
>>> addallodd([1, 2, 3, 4, 5, 6, 7, 8, 9])
25
'''
#result = 0
def addall(list):
    #for in 리터럴 
    result = 0
    for x in range(len(list)):
        result = result + list[x]
    return result

def addall1(list):
    result = 0 
    result = sum([list[x] for x in range(len(list))])
    return result

def addallodd(list):
    result = 0
    for x in range(len(list)):
        if(list[x]%2!=0):
            result = result + list[x]
    return result
    
def addallodd1(list):
    result = 0 
    result = sum([list[x] for x in range(0, len(list)) if(list[x]%2!=0)])
    return result
 
list1 = [1,2,3,4,5,6,7,8,9]
a = addall(list1)
print a
b = addallodd(list1)
print b
c = addall1(list1)
print c
d = addallodd1(list1)
print d

#6번과제
#다음 코드를 보고 물음에 답하시오.
L1 = [1, 2, 3]
L2 = [4, 5, 6]
d = {'low':L1, 'high':L2}
e = d
f = d.copy()
print d
print e
print f
print
d['low'] = [10, 20, 30]
d['high'][1] = 500
print d
print e
print f

#7번문제 
'''
사전 d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}가 주어졌을 때 다음 요구사항에 맞는 코드를 제시하시오
[참고]: d.keys(), d.values()를 통해 리스트를 얻어낸 후 리스트가 지니고 있는 sort(cmp=None, key=None, reverse=False)함수를 활용하시오.
1) 키의 알파벳 오름차순 순서대로 튜플 (키, 값)을 차례대로 출력하시오.
2) 키의 알파벳 내림차순 순서대로 튜플 (키, 값)을 차례대로 출력하시오.
3) 값의 오름차순 순서대로 튜플 (키, 값)을 차례대로 출력하시오.
4) 값의 내림차순 순서대로 튜플 (키, 값)을 차례대로 출력하시오.
'''
d = {'one':1, 'two':2, 'three':3, 'four':4, 'five':5}
#1)

str = 'abc'
x = d.values()
y = d.keys()

def mycmp(a1, a2):
    if(a1[0]>a2[0]):
        return cmp(a1[0], a2[0])
    elif(a1[0]==a2[0]):
        if(a1[1]>a1[1]):
            return cmp(a1[1], a2[1])            
        else:
            return cmp(a2[1], a1[1])                
    else:
        return cmp(a1[0], a2[0])

b = sorted(y, mycmp)

print '문제 1)' 
for key in b:
    temp = (key, d[key])
    print temp,   


#2)
print 
print '--------------'    
print '문제 2)'
c = sorted(y, mycmp)
c.reverse()
for key in c:
    temp = key, d[key]
    print temp,
 
#3)
print
print '--------------'
print '문제 3)'
a = sorted(x)
for i in a:
    for l in d:
        if(d[l] == i):
            print (i, l),
        
#4)
print
print '--------------'
print '문제 4)'
a = sorted(x, reverse=True)
for i in a:
    for l in d:
        if(d[l] == i):
            print (i, l),
#print a

'''
이전 Assignment 2의 마지막 문제는 웹 URL로 지정된 웹페이지를 문자열로 가져와 모든 HTML 태그 및 CSS와 Javascript를 제외한 순수 텍스트를 얻어내고 그 안에 존재하는 단어를 추출하는 프로그램을 작성하는 것이었다. 
이번에는 그 마지막 숙제를 그대로 확장하여 웹 URL로 지정된 웹페이지 내 순수 텍스트 안에 존재하는 각 단어들에 대해 다음 요구사항 대로 출력하는 프로그램을 작성하시오.
요구사항 1. 순수 텍스트 안에 존재하는 단어들에 대해 string 모듈을 활용하여 모든 punctuation (구두문자)를 완벽히 제거하시오 (교재 166페이지 참고).
예: ['world!', ':', '+hello+', '~python$$$', '=', 'world'] ---> ['world', 'hello', 'python', 'world']
요구사항 2. 각 단어들의 출현빈도를 사전형태로 저장하여 출력하시오.
예: ['world', 'hello', 'python', 'world'] ---> {'world': 2, 'hello': 1, 'python': 1}
'''

import urllib
import string

source = urllib.urlopen("http://cse.kut.ac.kr/").read()

len_source = len(source)
print "Initial length of source:", len_source

source_new = None
i = 0
while (i < len_source):
	found = False
	if (found != True and source[i] == "<" and source[i+1 : i+7].lower() == "script"):
		found = True;
		j = i + 7;
		while (True):
			if (source[j] == "<" and source[j+1] == "/" and source[j+2 : j+8].lower() == "script"):
				#print "found - script"
				source = source[:i] + ' ' + source[j+9:]
				break
			j = j + 1
			if (j > len_source):
				break
		len_source = len(source)
	i = i + 1

len_source = len(source)
#print len_source

i = 0
while (i < len_source):
	found = False
	if (found != True and source[i] == "<" and source[i+1 : i+6].lower() == "style"):
		found = True;
		j = i + 6;
		while (True):
			if (source[j] == "<" and source[j+1] == "/" and source[j+2 : j+7].lower() == "style"):
				#print "found - style"
				source = source[:i] + ' ' + source[j+8:]
				break
			j = j + 1
			if (j > len_source):
				break
		len_source = len(source)
	i = i + 1

len_source = len(source)
#print len_source

i = 0
while (i < len_source):
	found = False
	if (found != True and source[i] == "<"):
		found = True;
		j = i + 1;
		while (True):
			if (source[j] == ">"):
				#print "found - HTML tag"
				source = source[:i] + ' ' + source[j+1:]
				break
			j = j + 1
			if (j > len_source):
				break
		len_source = len(source)
	i = i + 1
	




Filter = string.punctuation
print "필터출력"
print Filter
found = False


i = 0
while (i < len_source):
	found = False
	if (found != True and source[i] in Filter):
		found = True;
		j = i + 1;
		source = source[:i] + ' ' + source[i+1:]
		if (j > len_source):
			break
		len_source = len(source)
	i = i + 1

	

len_source = len(source)
print "Last length of source:", len_source

words = source.split()

#for word in words:
#	print word

print "Total num of plain words:", len(words)

    
print 
print type(words)

def checkedForRepetition(source):
    list=[]
    len_source = len(source)
    i = 0    
    while True:
        if(i>len_source-1):
            break
        checkedWord = source[i]         
        if(list.count(checkedWord)==0): 
            list.append(checkedWord)                          
        else:
            i = i + 1
            continue            
       
    return list  
  
nonRepeatedWords = checkedForRepetition(words)

list = []
for x in nonRepeatedWords:
    list.append((x, words.count(x)))

list_dict = dict(list)

     
