# 6084 : 소리 파일 저장용량 계산하기

h, b, c, s = input().split()
h = int(h)
b = int(b)
c = int(c)
s = int(s)

mb = (h*b*c*s)/8/1024/1024
print(format(mb, ".1f"), "MB")
