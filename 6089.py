# 6089 : 수 나열하기2

a, r, n = input().split()
a = int(a)
r = int(r)
n = int(n)

sequence = a*r**(n-1)
print(sequence)
