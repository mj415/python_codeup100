# 6045 : 정수 3개 입력받아 합과 평균 출력하기

a, b, c = input().split()

d = int(a)
e = int(b)
f = int(c)

add = d+e+f

print(add, format(add/3, ".2f"))
