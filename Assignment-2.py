# -*- coding: utf-8 -*-
#다음 6 개의 Expression에 대해 Evaluation 결과 값을 출력하고, 해당 결과가 나온 이유에 대해 설명하시오
print eval('1 and 2 and 3 and 4')
print eval('1 or 2 or 3 or 4')
print eval('1 and 2 or 3 and 4')
print eval('(1 and 2) or (3 and 4)')
print eval('1 or 2 and 3 or 4')
print eval('(1 or 2) and (3 or 4)')


#7/5, -7/5, -(7/5)의 결과를 확인하고 각각의 결과가 왜 그렇게 나오는 지 설명하시오
#[참고] 몫은 항상 음의 무한대 방향으로 round up (반올림) 된다는 점을 기억해야 함
print 7/5, -7/5, -(7/5)


#키보드로 정수값을 입력 받고 그 값이 양수인지 음수인지를 비트 연산자를 이용하여 판단하는 프로그램을 작성하시오.
#[참고] 가장 왼쪽에 있는 비트가 0이면 양수이며, 1이면 음수이다.
def discriminator(num):
    if(num > 0 ):
        result = (num >> len(bin(int(num))[2:])-1)
        return result
    elif (num < 0):
        return (num >> len(bin(int(num))[3:]))
    else:
        return 0
        
switch_case = {
        1 : "양수",
        2 : "음수",
        0 : "영"
        }

while True:
    input_nu = input(u"숫자 입력: ")        
    input_num = discriminator(input_nu)
    print input_nu,"판별: ", switch_case[input_num]
    print
    if input == 0:
        break;
        




#키보드로 정수값을 입력 받고 그 값이 양수인지 음수인지를 비트 연산자를 이용하여 판단하는 프로그램을 작성하시오.
#[참고] 가장 왼쪽에 있는 비트가 0이면 양수이며, 1이면 음수이다.


'''
두 개의 리스트를 인자로 받아서 그 두 개의 리스트에 대한 '합집합'을 반환하는 함수 list_union(lista, listb)를 작성하시오.
인자로 전달하는 리스트 2 개에는 정수값만 들어간다고 가정하자.
함수 내에서 새로운 리스트를 만들어 그 리스트 내에 인자로 받은 두 리스트의 모든 원소를 넣어 반환한다.
반환하는 리스트에는 절대로 중복된 원소가 들어 있으면 안된다 (집합의 조건).
반환하는 리스트는 정렬이 되어 있어야 한다.
다음과 같은 실행 및 출력 결과가 도출되어야 한다.
list_union([1, 2, 3], [1, 2, 4])
[1, 2, 3, 4]
list_union([-10, -5, 0, -1], [100, 9, 0, 9])
[-10, -5, -1, 0, 9, 100]
list_union([0, 1, 2], [0, 1, 2])
[0, 1, 2]
[참고] 리스트(l) 내에 새로운 정수값 (예를 들어 10)을 넣는 방법은 l.append(10) 이다.
[참고] 임의의 정수값 (x)이 리스트 (l) 내에 존재하는지 판단하는 방법은 x in l 이다.
'''
def list_union (l1, l2):
    relist=[]
    for x in l1+l2:
        if x not in relist:
            relist.append(x)
    return relist
    
print list_union ([1,2,3], [1,2,4])
    

'''
경로에 해당하는 문자열 1개를 입력 받아 그 안에 디렉토리 경로명과 파일명을 분리하여 리스트로 반환하는 함수 div_path(s)를 작성하시오.
인자로 전달하는 문자열은 경로만 들어간다고 가정한다.
각 디렉토리와 파일을 구분하는 문자는 '/'로 가정한다.
반환하는 리스트의 첫번째 원소는 디렉토리이고 두번째 원소는 파일명이다.
다음과 같은 실행 및 출력 결과가 도출되어야 한다.
div_path('/usr/local/bin/python')
['/usr/local/bin', 'python']
div_path('/home/chulsoo/test.txt')
['/home/chulsoo', 'test.txt']
'''
def div_path(s):
    result = s.rsplit('/', 1)
    return result
    
    



    