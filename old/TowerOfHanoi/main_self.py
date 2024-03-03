def move(plates, origin, target):
    def mid(oe, te):
        post = {1, 2, 3}
        post.remove(oe)
        post.remove(te)
        return post.pop()
    if plates == 1:
        print(f"From {origin} to {target}")
        return
    empty = mid(origin, target)
    move(plates - 1, origin, empty)
    move(1, origin, target)
    move(plates - 1, empty, target)

move(3, 1, 3)

