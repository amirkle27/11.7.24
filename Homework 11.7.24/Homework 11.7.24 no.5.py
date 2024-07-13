IQ=0
totalIQ: int = 0
students: int = 0

while True:
    IQ: int = int (input ("Please state your IQ"));
    totalIQ: int = totalIQ+IQ
    students: int = students+1
    if IQ<30 or IQ>300:
        break
avg: float = totalIQ / students
print (f"we had {students} students in total")
print (f"The total IQ is {totalIQ}");
print (f"Well, the average IQ in our class BEFORE THE COURSE is {avg}");
print("");
print("After 1 year of schooling, we wanted to see our new level of IQ!");
print("");
print("")
OldStudents = 0
NewIQ = 0
TotalNewIQ: int = 0
while True:
    NewIQ: int = int(input("Please enter your new IQ"));
    TotalNewIQ: int = TotalNewIQ + NewIQ;
    OldStudents = OldStudents + 1
    if NewIQ<30 or NewIQ>300:
        break;
NewAvg: float = TotalNewIQ/OldStudents
dif: float = NewAvg-avg;
print(f"The new average IQ in our class is {TotalNewIQ}");
print(f"In comparison with last year, we've had a jump of {dif} \
points in our average IQ! WOW!"
          if avg<NewAvg else f"We dropped {dif} points AFTER 1 YEAR OF SCOOLING!!!\
WHAT A DISGRACE! WHAT A HUMILIATION!!!");



