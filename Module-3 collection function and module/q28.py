#Q.28 write a python program to remove an empty tuple(s) from a list of a tuple.

#Ans:-

lis=[(1,2,3),(),(4,5,6),()]
for x in lis:
    if len(x)==0:
        lis.remove(x)
print(lis)        
        