# 1. 변수 만들기
a = "456" # 문자열 만들기
b = 789 # 정수 만들기

print(type(a))
print(type(b))

# 2. 연산해 보기 
# 결과 : 1,245

# 정답 1
# 변수 재할당
a = int(a) 
print(a + b)

# 정답 2
# 변수를 바꾸는 것이 아닌 계산만 수행하고 싶다면?
print(int(a) + b)

# 3. 식별자와 리터럴
number_1 = 1.0  # 여기에서 에러 발생
print(number_1) 
# 식별자의 이름은 숫자로 시작하면 안된다.
# 숫자로 시작하면 숫자로 인식하려 하기 때문에

print_ex = "출력을 위한 함수" 
print(print_ex) # 여기에서 에러 발생
# 기존에 파이썬에서 쓰고 있는 내장 함수를 덮어써서
# 더이상 print 함수의 기능을 하지 못함

# 4. 비교 연산자 / 논리 연산자
c = " " # 공백이 있는 문자열 " " (str)
d = a // b # a에서 b를 나눈 몫 0 (int)

print(type(c)) # str
print(type(d)) # int

# 비교 연산자
# ==, != : 단순 비교 -> 값이 일치하는지 판단
# >, <, >=, <= : 대소 비교 (자료형 일치)
print(c != d) # True (1)

# 논리 연산자
print(not c == d) # True (2)
print(not d) # True (3)
print(bool(c) or bool(d)) # True (4)
