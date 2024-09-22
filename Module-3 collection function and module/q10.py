#Q.10 write a python program to generate  and print a list of first and last 5 elements where the values are square of numbers
#between 1 and 30.

#ans:-
l = []

for i in range(1, 30):
    l.append(i ** 2)
    first_five=l[:5]
    last_five=l[-5:]
print(l)
print("first 5 elements:",first_five)
print("last 5 elements:",last_five)

