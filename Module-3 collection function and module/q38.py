
#Q.38 write a python program to check multiple keys exits in a dictionary.

dict={
         'a':1,
         'b':2,
         'c':3,
         'd':4 
    
}
check=['a','b','c','d']
for key in check:
    if  key in dict :
        print("The keys is present in dictionary")
    else:
        print("The keys are missing in the dictionary.")
