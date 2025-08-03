print("Start Calculator")
print("종료하려면 연산자에 'q'를 입력하세요.\n")

while True :
    num1 = float(input("첫 번째 숫자: "))
    operator = input("연산자 입력(+,-,*,/,q): ")

    if operator == "q" :
        print("Quit Calculator")
        break
    
    num2 = float(input("두 번째 숫자: "))

    if operator == "+" :
        result = num1 + num2
    elif operator == "-" :
        result = num1 - num2
    elif operator == "*" :
        result = num1 * num2
    elif operator == "/" :
        if num2 != 0 :
            result = num1 / num2
        else :
            result = "❌ 0으로 나눌 수 없습니다."
        
    else :
        result = "❗️ 지원하지 않는 연산자입니다."
    print("결과: ", result)
    print("-" * 30)

