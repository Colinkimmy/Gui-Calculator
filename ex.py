#덧셈 계산기
print("start!")

num1 = input("첫 번째 숫자를 입력하세요.: ")
num2 = input("두 번째 숫자를 입력하세요.: ")

num1 = float(num1)
num2 = float(num2)

result = num1 + num2

print("결과:", result)

#사칙연산
print("Start!")

num1 = float(input("첫 번째 숫자 입력: "))
operator = input("연산자 입력(+,-,*,/): ")
num2 = float(input("두 번째 숫자 입력: "))

if operator == "+" :
    result = num1 + num2
elif operator == "-" :
    result = num1 - num2
elif operator == "*" :
    result = num1 * num2
elif operator == "/" :
    result = num1 / num2
    if num2 != 0 :
        result = num1 / num2
    else:
        result = "0으로 나눌 수 없습니다."
else:
    result = "지원하지 않는 연산자입니다."
print("결과: ", result)