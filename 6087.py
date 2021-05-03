# 6087 : 3의 배수는 통과

a = int(input())

for i in range(a+1):
    if i % 3 != 0:
        print(i, end=" ")
