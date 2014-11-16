__author__ = 'ES'
# -*- coding: utf-8 -*-
import sha

# 메뉴를 표시하고 메뉴를 입력받는다(0-4).
def menu():
    print "1. Sign Up"
    print "2. Sign In"
    print "3. quit"
    return input('Select menu: ')

f = open('access.txt', 'r+')
if(f.read() == ''):
    f.close()
    f = open('access.txt','w+')

def checkId(Id, file):
    print "아이디 중복검사 함수 시작"
    temp_f = file
    temp_f.seek(0)
    lines_file = temp_f.readlines()
    i = 0
    while i < len(lines_file):
        #subStringId = lines_file[i][:lines_file[i].find(':')]
        print "아이디만 자르기"
        #print subStringId
        #print subStringId(lines_file[i])
        if (Id in subStringId(lines_file[i])):
            if subStringId(lines_file[i]) == Id:
                return True
        i = i + 1
    return False


#ID 부분만 추출하는 함수
def subStringId(info):
    return info[:info.find(':')]

#Password 부분만 추출하는 함수
def subStringPassword(info):
    return info[info.find(' ') + 1:info.find(',')]

# Name 부분만 추출하는 함수
def subStringName(info):
    return info[info.find(',')+2: info.rfind(',')]

#ID 존재 검사 함수
def checkForId(id, database):
    i = 0
    for x in database:
        x = subStringId(x)
        database[i] = x
        i = i + 1
    for x in database:
        print x
    #id 존재 True 반환, 비존재 False 반환
    if (id not in database):
        return False
    else:
        return id


#Pass 일치 검사 함수
def checkForPass(id, password, database):
    password = sha.new(password).hexdigest()
    for x in range(len(database)):
        if (id in database[x]):
            if (password in database[x]):
                return True
    return False

#ID로 이름찾기 함수
def findNameById(id, database):
    for i in range(len(database)):
        if(id in database[i]):
            if(id == subStringId(database[i])):
                return subStringName(database[i])
            else:
                continue
    return "Id not found"

#메뉴를 표시하고 선택된 메뉴를 실행한다.
while 1:
    sel = menu()  # 메뉴 표시하고 키 입력 받음
    if sel == 1:  # 범위를 벗어나면 다시 메뉴 표시
        print "Sign up selected"
        id = raw_input('ID: ')

        if checkId(id, f) == True:
            print "Sorry, the entered ID is already used."
            continue

        password = raw_input('Password: ')
        name = raw_input('Name: ')
        school = raw_input('School: ')
        # "id: password, name, school"

        password = sha.new(password).hexdigest()
        file_input = id + ": " + password + ", " + name + ", " + school + "\n"
        print file_input

        #password_plain = "my password"
        #password_encrypted = sha.new(password_plain).hexdigest()


        if f.read() != '':
            f = open('access.txt', 'a+')
            f.write(file_input)
        else:
            f.write(file_input)

    if sel == 2:
        print "Sign in selected"
        id = raw_input('ID: ')
        password = raw_input('Password: ')
        if f == None:
            f = open('access.txt', 'r')
        f.seek(0)
        userInfo = f.readlines()
        idFlag = checkForId(id, userInfo)
        #print "id Flag 중간검사: ", idFlag
        #print idFlag
        #print "id Flag 중간검사: "+idFlag
        if not idFlag:
            print "Sorry, you are not a registered member."
        else:
            if not checkForPass(idFlag, password, userInfo):
                print "Sorry, the entered password is not correct."
            else:
                print "Hello ["+idFlag+"]!"



    if sel == 3:
        break




