# 6056 : 참/거짓이 서로 다를 때에만 참 출력하기

a, b = input().split()
c = bool(int(a))
d = bool(int(b))

print((c and (not d)) or ((not c) and d))  # 둘의 bool 값이 다를 때 참 값
print(c != d)
