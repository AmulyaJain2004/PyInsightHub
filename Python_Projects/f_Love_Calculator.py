Person_1 = input("Enter the name of Person 1: ").lower()
Person_2 = input("Enter the name of Person 2: ").lower()

list1 = list(Person_1)
list2 = list(Person_2)
list_concat =  list1 + list2

t=0
r=0
u=0
e=0
l=0
o=0
v=0
e=0

for i in list_concat:
    t=list_concat.count("t")
    r=list_concat.count("r")
    u=list_concat.count("u")
    e=list_concat.count("e")
    l=list_concat.count("l")
    o=list_concat.count("o")
    v=list_concat.count("v")
    e=list_concat.count("e")

number = ((t+r+u+e+l+o+v+e)/len(list_concat))*100

if round(number,1) <40:
    print(f"Love percentage is: {round(number,1)}% Change your name and Hope for Best, May Python be with you both next time!!")
elif round(number,1) >=40 and round(number,1) <=60:
    print(f"Love percentage is: {round(number,1)}% Good to go and proceed to next step, Python supports you!!")
else:
    print(f"Love percentage is: {round(number,1)}% Congratulations, both of you, Even Python can't separate you!!")
