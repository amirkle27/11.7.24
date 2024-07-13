statements = [
    "4 < 9",
    "(2 * 3 + 4) * (7 + 7)",
    "18 + 18",
    "10 == 10",
    "10 == 10 and 20 == 30",
    "10 == 10 or 20 == 30",
    "20 == 30 or 10 == 10",
    "not 3",
    "3",
    "(33 > 20) and (2 < 12) and 10",
    "True and True",
    "True and False",
    "True or False",
    "False or True",
    "(not 10) and (10)",
    "(not 10) and (not 10)",
    "5 != 5 and 5 == 5",
    "2 == 2 or 3 == 3",
    "2 == 2 and 3 == 3",
    "40 == 30 and 1 >= 4",
    "13 >= 3 or 47 >= 5"
]
for statement in statements:
    result = eval(statement)
    if statement:
        print(f"{statement} ---> True");
    else:
        print(f"{statement} ---> False");





