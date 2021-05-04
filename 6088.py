# 6088 : 수 나열하기1

a, d, n = input().split()
a = int(a)
d = int(d)
n = int(n)

sequence = a + (n-1)*d
print(sequence)
