#Q.27 write a python program to find the repeated items of a tuple.

Ans:-

tup=(1,2,3,4,5,5,5,6,7,7,8,9)
for x in tup:
    if tup.count(x) > 1:
        print(x)
