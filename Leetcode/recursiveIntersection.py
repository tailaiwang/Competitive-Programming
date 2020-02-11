#recursiveIntersection
#Recursively determines the size of the intersection of two lists

def search(L, item, count):
    if item == L[count]:
        return 1
    elif count + 1 == len(L):
        return 0
    else:
        return search(L, item, count + 1)
    

def helper(a, b, count, total):
    if count == len(a) - 1:
        return total
    else:
        return helper(a, b, count + 1, total + search(b, a[count + 1], 0))

def inter (a, b):
    if (len(a) == 0 or len(b) == 0):
        return 0
    else:
        return helper(a ,b , 0, search(b, a[0], 0))



# -- Test Cases -- #
a = [1,2,3,4,5]
b = [3,4,5,6,7]
print(inter(a,b))


