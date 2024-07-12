statements = [
    "4 < 2",
    "(4 + 2) * (6 - 6) == 0",
    "not 3"
]

for statement in statements:
    # Evaluate the statement
    result = eval(statement)

    # Print the original statement and the result
    print(f"{statement} -> {result}")

    # Check if the statement is a mathematical equation and print the evaluated result
    try:
        # Replace comparison operators to get the mathematical expression
        math_statement = statement.replace("==", "=").replace("<", "=").replace(">", "=").replace("not", "not ")
        math_result = eval(math_statement.split("=")[0])
        print(f"Mathematical Result: {math_result}")
    except:
        pass


ToF = [
"4 > 9",
"(2 * 3 + 4) * (7 + 7)",
"18 - 9, 10 == 10",
"10 == 10 and 20 == 30",
"10 == 10 or 20 == 30",
"20 == 30 or 10 == 10",
"not 3",
]
a =
b = (2 * 3 + 4) * (7 + 7)

questions =   ,  , ,,  ,  3,  (33 > 20) and (2 < 12) and 10, True and True,  True and False,  True or False

for range in questions:
    if range :
        print(f"{a} is True")
    else:
        print (f"{a} is False")


