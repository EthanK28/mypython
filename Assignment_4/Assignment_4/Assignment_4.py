# -*- coding: utf-8 -*-

func = [lambda x, y: x + y, lambda x, y: x - y, lambda x, y: x * y, lambda x, y: x / y]
import sha

#�޴��� ǥ���ϰ� �޴��� �Է¹޴´�(0-4).
def menu():
    print "1. Sign Up"
    print "2. Sign In"
    print "3. quit"
 
    return input('Select menu:')
    f = open('acesss.txt', 'w+')

#�޴��� ǥ���ϰ� ���õ� �޴��� �����Ѵ�.
while 1:
    sel = menu()                     # �޴� ǥ���ϰ� Ű �Է� ����
    if sel == 1:   # ������ ����� �ٽ� �޴� ǥ��
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



