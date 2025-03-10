operator = input("Operatoru daxil edin (+, -, *, /): ")
num1 = float(input("Birinci ədədi daxil edin: "))
num2 = float(input("İkinci ədədi daxil edin: "))


if operator == "+":
    result = num1 + num2
    print(f"Nəticə: {result}")
elif operator == "-":
    result = num1 - num2
    print(f"Nəticə: {result}")
elif operator == "*":
    result = num1 * num2
    print(f"Nəticə: {result}")
elif operator == "/":
    if num2 == 0:
        print("Xəta: 0-a bölmək olmaz!")
    else:
        result = num1 / num2
        print(f"Nəticə: {result}")
else:
    print("Xəta: Düzgün operator daxil edin!")