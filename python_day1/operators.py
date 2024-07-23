# 연산자
# "처리"

a = 5
b = 2

# 1. 산술 연산자
# print(a + b) # 6 / int
# print(a - b) # 2 / int
# print(a * b) # 8 / int
# print(a / b) # 2.0 / float # 산술연산자에서 헷갈리는 부분

# # 몫 / 나머지 / 제곱
# print(a // b) # 2 / int
# print(a % b)  # 0 / int
# print(a ** b) # 16 / int

# 복합 연산자
# 산술연산자와 할당연산자를 함께 쓰는 것
# +=, -=, *=
# print(a)
# print(b)

# a = a + b
# a += b
# print(a)

# 3. 비교 연산자 (값과 값을 비교한다!)
# <, >, <=, >=, ==, !=
# 비교 연산의 결과는 True 혹은 False -> bool 자료형
# a = 'aa'
# b = 'ab'

# print(a > b)

# 논리연산자 (and, or, not)
# True 혹은 False 라는 bool 타입을 반환!

# a and b: a와 b, 둘다 True 여야만 True
a = 20 > 10             # 비교연산자 -> True
b = 'hello' == 'Hello'  # 비교연산자 -> False

print(a and b) # False
print(a or b)  # True
print(not a)