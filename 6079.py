# 6079 : 언제까지 더해야 할까?

a = int(input())
b = 0
n = 0

while b < a:
    n += 1
    b += n
print(n)  # 마지막에 더한 정수 출력
