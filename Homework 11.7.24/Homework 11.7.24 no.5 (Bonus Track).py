IQ=0
totalIQ: int = 0
students: int = 0
max: int = IQ
while True:
    IQ: int = int (input ("Please state your IQ"));
    if IQ>max:
        max=IQ
    totalIQ: int = totalIQ+IQ
    students: int = students+1
    if IQ<30 or IQ>300:
        break
avg: float = totalIQ / students
print (f"we had {students} students in total")
print (f"The total IQ is {totalIQ}");
print (f"The highest IQ score was {max}")
print (f"Well, the average IQ in our class BEFORE THE COURSE is {avg}");
print("");
print("After 1 year of schooling, we wanted to see our new level of IQ!");
print("");
print("")
OldStudents = 0
NewIQ = 0
maxNew=IQ
TotalNewIQ: int = 0
while True:
    NewIQ: int = int(input("Please enter your new IQ"));
    if NewIQ>maxNew:
        maxNew=NewIQ
    TotalNewIQ: int = TotalNewIQ + NewIQ;
    OldStudents = OldStudents + 1
    if NewIQ<30 or NewIQ>300:
        break;
NewAvg: float = TotalNewIQ/OldStudents
dif: float = NewAvg-avg;
print (f"we had {OldStudents} students in total this time")
print (f"The total IQ is {TotalNewIQ}");
print (f"The highest IQ score was {maxNew} after the course")
print(f"The new average IQ in our class is {TotalNewIQ}");
print(f"In comparison with last year, we've had a jump of {dif} \
points in our average IQ! WOW!"
          if avg<NewAvg else f"We dropped {dif} points AFTER 1 YEAR OF SCOOLING!!!\
WHAT A DISGRACE! WHAT A HUMILIATION!!!");
print(f"In summery, the highest IQ score a year ago was {max}, and {maxNew} this time");
print (f"Good Job!" if maxNew>max else (f"Shame on you!"));



