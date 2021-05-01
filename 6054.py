# 6054 : 둘 다 참일 경우만 참 출력하기

a, b = input().split()
c = bool(int(a))
d = bool(int(b))

print(c and d)  # 두 값 모두 참 값이여야 참
