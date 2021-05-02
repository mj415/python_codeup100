# 6074  문자 1개 입력받아 알파벳 출력하기

char = ord(input())  # ord() 유니코드 값을 돌려줌
a = ord('a')  # a의 유니코드 값 97 저장

while a <= char:  # a의 유니코드 값이 입력받은 값보다 작으면
    print(chr(a), end=' ')  # chr() 유니코드 값을 문자로, end=' ' 마지막 공백출력
    a += 1  # a = a+1
