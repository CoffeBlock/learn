x = [1, 2, 5, 7]
y = [3, 6, 9, 20, 34, 95]

def merge(x, y):
    xt = 0
    yt = 0
    mergelist = []

    while not xt == len(x) and not yt == len(y):
        if x[xt] < y[yt]:
            mergelist.append(x[xt])
            xt += 1
        else:
            mergelist.append(y[yt])
            yt += 1
    if not xt == len(x):
        while not xt == len(x):
            mergelist.append(x[xt])
            xt += 1
    else:
        while not yt == len(y):
            mergelist.append(y[yt])
            yt += 1
    

    return mergelist

print(merge(x, y))