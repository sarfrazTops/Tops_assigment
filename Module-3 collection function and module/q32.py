#Q.32 write a python script to sort (ascending and descending) a dictionary by value.

dict={"sarfraz":3,
      "sanjay":5,
      "rahul":2,
      "riyaz":1,
      "manoj":4
}

print(sorted(dict.values()))
print(sorted(dict.values(), reverse=True))