#!/usr/bin/python
# -*- coding: UTF-8 -*-
__author__ = 'Eunseok'
#[2번 문제] 다형성에 대해 설명하고 다형성을 보여주는 자신만의 파이썬 코드 예제를 제시하시오.
'''
다형성(Polymorphism)
상속 관계 내의 다른 클래스들의 인스턴스들이 같은 멤버 함수 호출에 대해 각각 다르게 반응하도록 하는 기능
연산자 오버로딩도 다형성을 지원하는 중요한 기술
하나의 이름 (적은 코딩)으로 다양한 객체들에게 유사한 작업을 수행시킬 수 있음
프로그램 작성 코드 량이 줄어든다.
코드의 가독성을 높혀준다.
형 선언이 없다는 점에서 파이썬에서는 다형성의 장점이 더욱 부각된다.
실시간으로 객체의 형이 결정되므로 단 하나의 메소드에 의해 처리될 수 있는 객체의 수는 더욱 많아진다.
즉, 다른 언어보다 코드의 양이 더욱 줄어든다.
파이썬에서 모든 함수는 기본적으로 다형성의 특징을 포함한다.
'''

class Vehicle:
    def move(self):
        print '이동수단이 이동한다'

class Plane(Vehicle):
    def move(self):
        print "비행기가 이동한다"

class Car(Vehicle):
    def move(self):
        print "차가 이동한다"

class Taxi(Car):
    def move(self):
        print "택시가 이동한다"

class Bus(Car):
    def move(self):
        print "버스가 이동한다"

for each in (Vehicle(), Plane(), Car(), Taxi(), Bus()):
    each.move()
