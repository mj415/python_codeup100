# 문제 1. Hello 출력
print("Hello")
print('Hello')  # 문자열을 출력할 때 '', "" 상관 없음


# 문제 2. Hello World 출력
print("Hello World")
print("Hello", "World")  # ,로 나열할 때는 띄어쓰기 포함
print("Hello"+" World")  # +로 연결할 때는 띄어쓰기 포함되어 있지 않음

"""
문제 3. Hello
        World   출력
"""
print("Hello")
print("World")  # print()에 줄바꿈이 포함돼 있음

print("Hello\nWorld")  # \n은 줄바꿈 문자이므로 따옴표 안에 표시

# 문제 4. 'Hello' 출력
print("'Hello'")  # ""(큰 따옴표) 안에 ''(작은 따옴표)를 표시

print("\'Hello\'")
print('\'Hello\'')  # \'을 사용하면 '을 출력할 수 있음

# 문제 5. "Hllo World" 출력
print('"Hello World"')  # ''(작은 따옴표) 안에 ""(큰 따옴표) 사용 가능

print('\"Hello\"')
print("\"Hello\"")  # \"을 사용하면 "을 출력할 수 있음
