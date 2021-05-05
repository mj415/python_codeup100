# 6090 : 수 나열하기3

a, m, d, n = input().split()

a = int(a)
m = int(m)
d = int(d)
n = int(n)

sequence = a

for i in range(0, n-1):
    sequence = sequence*m+d
print(sequence)
