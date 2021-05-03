# 6086 : 거기까지! 이제 그만~

a = int(input())
sum = 0
c = 0

while True:
    sum = sum+c
    c = c + 1
    if sum >= a:
        break
print(sum)
