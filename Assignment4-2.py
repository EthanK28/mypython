# -*- coding: utf-8 -*-

func = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
import sha

#메뉴를 표시하고 메뉴를 입력받는다(0-4).
def menu():
    print "1. Sign Up"
    print "2. Sign In"
    print "3. quit"
 
    return input('Select menu:')
    f = open('acesss.txt', 'w+')

#메뉴를 표시하고 선택된 메뉴를 실행한다.
while 1:
    sel = menu()                     # 메뉴 표시하고 키 입력 받음
    if sel == 1:   # 범위를 벗어나면 다시 메뉴 표시
        print "Sign up selected"
        id = raw_input('ID: ')
        password = raw_input('Password: ')
        name = raw_input('Name: ')
        school = raw_input('School: ')
        # "id: password, name, school" 
        file_input = id+": "+password+", "+name+", "+school
        print file_input
        f.write(file_input)
    if sel == 2:
        print "Sign in selected"
        break
    if sel == 3:             
        break



