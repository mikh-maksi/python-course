operators = ("+", "-", "*", "/")
result = None
operand = None
operator = None
wait_for_number = True

while True:
    user_input = input(">>> ")
    if user_input == "=":
        break
    if wait_for_number:
        try:
            operand = float(user_input)
        except ValueError:
            print(f"{user_input} is not a number. Try again.")
            continue
        wait_for_number = False
        if result is None:
            result = operand
        else:
            if operator == "+":
                result += operand
            elif operator == "-":
                result -= operand
            elif operator == "*":
                result *= operand
            elif operator == "/":
                result /= operand
    else:
        operator = None
        for valid_operator in operators:
            if user_input == valid_operator:
                operator = user_input
        if operator is None:
            print(f"{user_input} is not in {operators}. Try again")
        else:
            wait_for_number = True

print(f"Result: {result}")
