#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Eunseok'
'''
[3번 문제] 다음 각 요구사항 모두를 만족시키는 Counter 클래스를 코딩하시오 (정답을 각 요구사항별로 입력할 필요 없이 3번 문제에 대해 1개의 클래스 정의 코드를 제시하면 된다.)

요구사항 1. 생성자에 count 값과 step 값을 인자로 받을 수 있다.

count: Counter 인스턴스가 지니는 초기 정수 값
step: Counter 인스턴스의 count가 증가되는 증분 (defalt 값: 1)
>>> c = Counter(10)
>>> d = Counter(10, 2)
요구사항 2. 다음과 같이 Counter의 인스턴스를 출력을 해주는 __str__() 메소드를 구현하시오.

>>> print c
[Count (step: 1)] 10
>>> print d
[Count (step: 2)] 10
요구사항 3. 다음과 같이 step에 주어진 증분만큼 count를 증가시키는 incr() 메소드를 구현하시오.

>>> c.incr()
>>> d.incr()
>>> print c
[Count (step: 1)] 11
>>> print d
[Count (step: 2)] 12
요구사항 4. __call__() 메소드를 추가하여 인스턴스 객체를 직접 호출할 수 있도록 하시오. 인스턴스 객체를 직접 호출했을 때의 동작방식은 incr() 메소드를 호출하였을 때와 동일하다.

>>> c()
>>> d()
>>> print c
[Count (step: 1)] 12
>>> print d
[Count (step: 2)] 14
요구사항 5. 다음과 같은 두 개의 산술 연산 (+, -)이 수행될 수 있도록 관련 메소드를 추가하시오.

>>> c = c + 5
>>> d = d - 5
>>> print c
[Count (step: 1)] 17
>>> print d
[Count (step: 2)] 9
요구사항 6. 다음과 같은 관계연산 (+, -)이 수행될 수 있도록 __cmp__() 메소드를 추가하시오.

>>> print c > 10
True
>>> print d > 10
False
>>> print c < 10
False
>>> print d < 10
True
>>> print c == 17
True
>>> print d != 9
False
'''

class Counter:
    step = 1
    #start = 0
    def __init__(self, *args):
        if(len(args)==1):
            self.start = args[0]
        if(len(args)==2):
            self.start = args[0]
            self.step = args[1]
    def __str__(self):
        return "[Count (step: "+str(self.step)+") "+str(self.start)

        #return temp
    def __call__(self):
        self.start = self.start + self.step
    def __cmp__(self, other):
        if(self.start > other.start):
            return True
        if(self.start < other.start):
            return False
        if(self.start == other.start):
            return True
        if(self.start != other.start):
            return False
    def incr(self):
        self.start = self.start + self.step
    def __add__(self, other):
        return self.start + other
    def __sub__(self, other):
        return self.start - other

#요구사항 1. 생성자에 count 값과 step 값을 인자로 받을 수 있다.

print "요구사항 1 확인"
c = Counter(10)
d = Counter(10, 2)
print "요구사항 2 확인"
print c
print d
print
print "요구사항 3 확인"
c.incr()
d.incr()
print c
print d
print

print "요구사항 4 확인"
c()
d()
print c
print d
print

print "요구사항 5 확인"
c = c + 5
d = d - 5
print c
print d
print

print "요구사항 6 확인"
print c > 10
print d > 10
print c < 10
print d < 10
print c == 17
print d != 9



