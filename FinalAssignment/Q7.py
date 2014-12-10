#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Eunseok'
'''

[7번 문제] 이전 Assignment 3 (Assignment 4가 아님)의 마지막 문제는 웹 URL로 지정된 웹페이지를 문자열로 가져와 모든 HTML 태그 및 CSS와 Javascript를 제외한 순수 텍스트를 얻어내고 그 안에 존재하는 단어를 추출하여 각 단어들에 대해
출현빈도를 사전형태({'world': 2, 'hello': 1, 'python': 1})로 저장하여 출력하는 것이었다. 이번에는 Assignment 3과 Assignment 4를 확장/변형하여 다음과 같은 조건을 만족하도록 구현하시오.

1) 새로운 클래스 WebWordsFrequency를 정의하시오.
2) 생성자에 URL을 0개에서 임의의 개수를 넣을 수 있도록 생성자 인수를 가변인수로 정의하여 각각의 URL을 리스트 자료형에 유지하시오.
>>> w1 = WebWordsFrequency('http://www.daum.net', 'http://www.naver.com', 'http://www.google.co.kr')
>>> w2 = WebWordsFrequency('http://www.daum.net', 'http://www.naver.com')
>>> w3 = WebWordsFrequency()
3) addUrl() 메소드를 구현하여 인스턴스를 생성한 이후에도 URL을 추가할 수 있도록 한다.

반드시 1개의 URL을 추가하도록 구현 (즉, 동시에 여러 개의 URL을 추가하는 것은 배제)
>>> w1.addUrl('http://cse.koreatech.ac.kr')
>>> w3.addUrl('http://www.koreatech.ac.kr')
4) removeUrl() 메소드를 구현하여 URL을 삭제할 수 있도록 한다.

반드시 1개의 URL을 삭제하도록 구현 (즉, 동시에 여러 개의 URL을 삭제하는 것은 배제)
>>> w1.removeUrl('http://www.daum.net')
>>> w2.removeUrl('http://www.naver.com')
5) listUrls() 메소드를 구현하여 현재 등록된 모든 URL을 출력하는 기능을 추가
>>> w1.listUrls()
http://www.naver.com
http://www.google.co.kr
http://cse/koreatech.ac.kr
6) getWordsFrequency() 메소드를 구현하여 각 URL의 웹페이지들을 종합적으로 분석한 단어 출현 빈도 사전을 반환하시오.

만약 등록된 URL이 없다면 공백 사전을 반환
>>> w1.getWordsFrequency()
{'다음': 8, '안녕': 12, 'world': 2, '우리': 11, 'hello': 1, 'python': 1}
7) getMaxFreqencyWords() 메소드를 구현하여 각 URL의 웹페이지들을 종합적으로 분석한 단어 출현 빈도 사전에서 가장 많이 출현한 단어 리스트를 반환하시오.

최다 출현 단어의 빈도수가 동일한 경우 모두 출력해주어야 함
만약 등록된 URL이 없다면 None을 반환
>>> w1.getMaxFreqencyWords()
우리
>>> w2.getMaxFreqencyWords()
다음에
안녕
8) Assignment 4에서 요구했던 파일로 저장하는 코드는 모두 삭제하시오.
'''
import urllib
import string


class WebWordsFrequency:
    urlList = []
    def __init__(self, *args):
        if (len(args) == 0):
            self.urlList = []
        else:
            for url in args:
                self.urlList.append(url)
    def webScroll(self, input_url):
        source = urllib.urlopen("http://" + input_url).read()
        len_source = len(source)

        source_new = None
        i = 0
        while (i < len_source):
            found = False
            if (found != True and source[i] == "<" and source[i + 1: i + 7].lower() == "script"):
                found = True;
                j = i + 7;
                while (True):
                    if (source[j] == "<" and source[j + 1] == "/" and source[j + 2: j + 8].lower() == "script"):
                        #print "found - script"
                        source = source[:i] + ' ' + source[j + 9:]
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
            if (found != True and source[i] == "<" and source[i + 1: i + 6].lower() == "style"):
                found = True;
                j = i + 6;
                while (True):
                    if (source[j] == "<" and source[j + 1] == "/" and source[j + 2: j + 7].lower() == "style"):
                        #print "found - style"
                        source = source[:i] + ' ' + source[j + 8:]
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
                        source = source[:i] + ' ' + source[j + 1:]

                        break
                    j = j + 1
                    if (j > len_source):
                        break
                len_source = len(source)
            i = i + 1

        Filter = string.punctuation
        found = False

        i = 0
        while (i < len_source):
            found = False
            if (found != True and source[i] in Filter):
                found = True;
                j = i + 1;
                source = source[:i] + ' ' + source[i + 1:]
                if (j > len_source):
                    break
                len_source = len(source)
            i = i + 1

        source = source.split('·')
        source = ''.join(source)
        words = source.split()

        def checkedForRepetition(source):
            list = []
            len_source = len(source)
            i = 0
            while True:
                if (i > len_source - 1):
                    break
                checkedWord = source[i]
                if (list.count(checkedWord) == 0):
                    list.append(checkedWord)
                else:
                    i = i + 1
                    continue

            return list

        nonRepeatedWords = checkedForRepetition(words)
        list = []
        for x in nonRepeatedWords:
            list.append((x, words.count(x)))

        self.list_dict = dict(list)

        return self.list_dict

    def addUrl(self, url):
        self.urlList.append(url)

    def removeUrl(self, url):
        for x in self.urlList:
            if (url == x):
                self.urlList.remove(x)

    def listUrls(self):
        for x in self.urlList:
            print x


    def getWordsFrequency(self):
        WordsFrequency = []
        self.result = {}
        if(len(self.urlList) == 0):
            return self.result
        for urlFromUrlList in self.urlList:
            WordsFrequency.append(self.webScroll(urlFromUrlList))
        for url in WordsFrequency:
            for x in url.keys():
                if(x not in self.result):
                    self.result[x]= url[x]
                else:
                    self.result[x] = self.result[x]+url[x]
        return self.result

    def getMaxFreqencyWords(self):
        if(len(self.urlList)==0):
            return None

        numlist = sorted(self.result.values(),reverse=True)
        #list = sorted(self.result, key=lambda x: x[1], reverse=True)

        maxNum = numlist[0]
        if(numlist.count(maxNum)!=1):
            print "맥스넘버가 하나가 아닐경우 호출"
            count = 0
            self.result = []
            while 0 <= numlist.count(maxNum):
                for key in self.result.keys():
                    if(self.result[key]==maxNum):
                        self.result.append(key, self.result[key])
                count = count + 1
            result = dict(self.result)
            for x in self.result.key():
                print x
        else:
            print "반복횟수 중복된 값 X"
            for key in self.result.keys():
                if(self.result[key] == maxNum):
                    print key, self.result[key]
        return True


    '''
    def theHighestNum(self, url):
        list = []
        for x in url:
            list.append(showthemostfrequentword(x))

        def f(x):
            return x[1]

        list = sorted(list, key=lambda x: x[1], reverse=True)

        return list
    '''



print "1번 조건 WebWordsFrequency 정의 완료"
print "2번 조건"
w1 = WebWordsFrequency('www.daum.net', 'www.naver.com', 'www.google.co.kr')
w2 = WebWordsFrequency('www.daum.net', 'www.naver.com')
w3 = WebWordsFrequency()
print "3번 조건"
w1.addUrl('cse.koreatech.ac.kr')
w3.addUrl('www.koreatech.ac.kr')

print "4번 조건"
w1.removeUrl('www.daum.net')
w2.removeUrl('www.naver.com')
print "4번 조건 완료"

print "5번 조건"
w1.listUrls()

print "6번조건"
w1.getWordsFrequency()
w2.getWordsFrequency()

print "7번조건"
w1.getMaxFreqencyWords()
w2.getMaxFreqencyWords()

print "8번조건 파일 저장 코드 삭제 완료"

print "-------------"

#8번문제

class OrderedWebWordsFrequency(WebWordsFrequency):
    OrderedList = []

    def getWordsFrequency(self):
        WordsFrequency = []
        self.result = {}
        if(len(self.urlList) == 0):
            return self.result
        for urlFromUrlList in self.urlList:
            WordsFrequency.append(self.webScroll(urlFromUrlList))
        for url in WordsFrequency:
            for x in url.keys():
                if(x not in self.result):
                    self.result[x]= url[x]
                else:
                    self.result[x] = self.result[x]+url[x]
        #print self.result
        numlist = sorted(self.result.values(),reverse=True)
        print numlist

        for x in numlist:
            for y in self.result.keys():
                if(self.result[y] == x):
                    self.OrderedList.append((y, x));
        print self.OrderedList[:4]



        #self.OrderedList = sorted(self.result, key=lambda x: x[1], reverse=True)


        '''
        for x in self.result.keys():
            self.OrderedList.append((x, self.result[x]))
        return self.OrderedList
        '''

w4 = OrderedWebWordsFrequency('www.daum.net', 'www.naver.com', 'www.google.co.kr')
w4.getWordsFrequency()


