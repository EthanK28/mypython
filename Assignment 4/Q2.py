__author__ = 'user'
# -*- coding: "UTF-8" -*-
func = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
def menu():
    print "0. add"
    print "1. sub"
    print "2. mul"
    print "3. div"
    print "4. quit"
    return input('Select menu:')

#메뉴를 표시하고 선택된 메뉴를 실행한다.
while 1:
    sel = menu()                     # 메뉴 표시하고 키 입력 받음
    if sel < 0 or sel > len(func):   # 범위를 벗어나면 다시 메뉴 표시
        continue
    if sel == len(func):             # quit이면 종료
        break
    x = input('First operand:')      # 첫번째 인수
    y = input('Second operand:')     # 두번째 인수
    print 'Result =', func[sel](x,y) # 해당함수 호출