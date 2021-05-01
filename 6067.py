# 6067 : 정수 1개 입력받아 분류하기

a = int(input())

if a % 2 == 0:
    if a > 0:
        print("C")
    else:
        print("A")
else:
    if a > 0:
        print("D")
    else:
        print("B")
