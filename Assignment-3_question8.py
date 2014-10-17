# -*- coding: utf-8 -*-

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
print nonRepeatedWords.count("컴퓨터공학부")
list = []
for x in nonRepeatedWords:
    list.append((x, words.count(x)))

list_dict = dict(list)
for key in list_dict:
    print key+':',list_dict[key],"|",

     
                  
           