# 6043 : 실수 2개 입력받아 나눈 결과 계산하기
# 나눈 값의 소숫점 넷째 자리에서 반올림하기

a, b = input().split()
c = float(a)/float(b)

print(format(c, ".3f"))
