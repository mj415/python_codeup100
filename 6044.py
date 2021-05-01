# 6044 : 정수 2개 입력받아 자동 계산하기

a, b = input().split()
c = int(a)
d = int(b)

print(c+d)  # 합
print(c-d)  # 차
print(c*d)  # 곱
print(c//d)  # 나눈 몫
print(c % d)  # 나머지
print(format(c/d, ".2f"))  # 나눈 값을 소숫점 둘째자리까지
