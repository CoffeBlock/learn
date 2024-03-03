steps = 0

def move(plates, origin, target):
    global steps
    
    def empty(originE, targetE):
        posts = {1, 2, 3}
        posts.remove(originE)
        posts.remove(targetE)
        return posts.pop()
    
    if plates == 1:
        print(f'Move from {origin} to {target}')
        steps += 1
        return
    emptyposts = empty(origin, target)
    move(plates - 1, origin, emptyposts)
    move(1, origin, target)
    move(plates - 1, emptyposts, target)
    


# 1 -> 3
platesToMove = 3

move(platesToMove,1,3)
fastest = 2 ** platesToMove
fastest -= 1
print(steps)
print(fastest)
