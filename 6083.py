# 6083 : 빛 섞어 색 만들기

r, g, b = input().split()

r = int(r)
g = int(g)
b = int(b)

num = 0

for i in range(r):  # range(0,r)보단 range(r)
    for j in range(g):
        for p in range(b):
            print(i, j, p)
            num += 1
print(num)
