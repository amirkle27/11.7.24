a = "amir"
b = "amir"
if a == b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")



a = 1
b = 0
c = 2
d = 0
if a + b and c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



a = 12
b = 2
c = 0
d = 0
if a >= b or c > d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



a = 0
b = 0
c = 0
d = 0.00000000000001
if a >= b or c < d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



a = 1
b = 1
c = 8
d = 8
if a == b and c <= d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



a = 0
b = 0
c = 900
d = 0
if True and a + b + c + d:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")



a = 90
b = 0
if a != b:
    print(f"was True for {a} {b}")
else:
    print(f"was False for {a} {b}")



a = 0
b = 90
c = 9
if a != b and a <= c or a <= b or True:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")



a = 2
b = 3
c = 4
if a != b and a <= c or a <= b or False:
    print(f"was True for {a} {b} {c}")
else:
    print(f"was False for {a} {b} {c}")


a = 20
b = 5
c = 15
d = 7
if a % b == 0 and c % d == 1:
    print(f"was True for {a} {b} {c} {d}")
else:
    print(f"was False for {a} {b} {c} {d}")