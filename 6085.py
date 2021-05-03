# 6085 : 그림 파일 저장용량 계산하기

w, h, b = input().split()

w = int(w)
h = int(h)
b = int(b)

mb = (w*h*b)/8/1024/1024

print(format(float(mb), ".2f"), "MB")
