# 6061 : 비트단위로 OR 하여 출력하기

# ~(bitwise not), &(bitwise and), |(bitwise or), ^(bitwise xor),
# <<(bitwise left shift), >>(bitwise right shift)

a, b = input().split()
c = int(a)
d = int(b)

print(c | d)
