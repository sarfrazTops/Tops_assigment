#Q.37 write a python script to print a dictionary where the keys are numbers between 1 and 15.

dict = {}

for i in range(1, 16):
    dict[i] = i ** 2  

print(dict)
