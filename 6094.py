# 6094 : 이상한 출석 번호 부르기3

n = int(input())  # 부른 횟수
a = input().split()

for i in range(n):
    a[i] = int(a[i])

first = a[0]
for i in range(n):
    if first > a[i]:
        first = a[i]
print(first)
