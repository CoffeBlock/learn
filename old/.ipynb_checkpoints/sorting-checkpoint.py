numlist = [1, 3, 2, 4, 9, 6, 10, 5]

def sortList(l):
    length = len(numlist)
    terms = 0
    while not terms == length:
        if numlist[terms] > numlist[terms - 1]:
            l.insert(terms - 1, numlist[terms])
        terms =+ 1

sortList(numlist)
print(numlist)