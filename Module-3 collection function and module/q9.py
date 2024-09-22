#(9)Write a Python function that takes two lists and returns true if they have
 #at least one common member.

#ans:-
 
def check_num(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False

print(check_num([1, 2, 3, 4], [4, 5, 6, 7]))
print(check_num([1, 2, 3, 4], [5, 6, 7, 8]))s