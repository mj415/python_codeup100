# 6055 : 하나라도 참이면 참 출력하기

a, b = input().split()
c = bool(int(a))
d = bool(int(b))

print(c or d)   # 둘 중에 하나라도 참 값이면 참
