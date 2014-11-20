# -*- coding: utf-8 -*-
from webScroll import webScroll
import urllib
import pickle


url = ("koreatech.ac.kr", "cse.koreatech.ac.kr","naver.com", "daum.net", "ruliweb.com",
       "google.com", "www.naughtydog.com", "www.reddit.com", "www.microsoft.com", "khnews.kheraldm.com" )


#8번문제
print "8번 1번 문제"
def saveAsAFile(url):
    url = url+".html"

    f = open(url, 'w+')
    f.write('12312 ')
    print url+"로 저장"
    if(f):
        return True
    else:
        return False

for x in url:
    saveAsAFile(x)
print
print "8번 2, 3번 문제"
def saveFrequency(url):
    url_dict = webScroll(url)
    url = url+".words.frequency"
    f = open(url, 'w+')
    pickle.dump(url_dict, f)
    print url+"로 저장"
    f.close()

for x in url:
    saveFrequency(x)

##9번문제

def showthemostfrequentword(url):
    url = url+".words.frequency"
    f = open(url)
    x = pickle.load(f)
    list = []
    for a in x:
        list.append(x[a])
    highestNum = sorted(list, reverse=True)[0]
    for a in x:
        if(x[a] == highestNum):
            result = (a, x[a])
    return result

def thehighestnum(url):
    list = []
    for x in url:
        list.append(showthemostfrequentword(x))
    def f(x):
        return x[1]
    list = sorted(list, key=lambda x: x[1], reverse=True)

    return list[0]

themostfrequentword = thehighestnum(url)

print
print "10개 파일에서 불러온 값중 가장 빈도수 높은 값"
print "값:",themostfrequentword[0], "빈도수:",themostfrequentword[1]




        



    