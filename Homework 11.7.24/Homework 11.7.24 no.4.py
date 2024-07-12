for i in range (10,21):
    print (i, end=" ")

for i in range (10, 21, 2):
    print (i)

jump: int = int (input("What's the jump you wish to perform?"));
for i in range (10, 21, jump):
    print (i)

start: int = int (input ("please enter the start point"));
end: int = int (input( "please enter the end point?"));
jump: int = int (input("Please enter the jumps"));
for i in range (start, end, jump):
    print (i)