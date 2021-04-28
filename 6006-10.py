# 문제 6. "!@#$%^&*()' 출력
print("\"!@#$%^&*()\'")

# 문제 7. "C:\Download\'hello'.py" 출력
print("\"C:\Download\\'hello'.py\"")    # \ 출력하려면 \\

# 문제 8. print("Hello\nWorld") 출력
print("print(\"Hello\\nWorld\")")  # \\가 \n보다 먼저 인식돼서 \n이 출력

# 문제 9.문자 1개를 입력받아 출력
#a = input()
# print(a)    # 입력받은 값이 b라면 b 출력

# 문제 10. 정수 1개를 입력받아 출력
a = input()  # print(type(a))의 값이 str
print(int(a))

b = int(input())  # input(int())는 int형으로 변환한 값을 문자열로 입력 받는 것이므로 안됨
print(b)
