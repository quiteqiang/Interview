houses = ["Eric's house", "Kenny's house", "Kyle's house", "Stan's house"]


def rec (Alist):
    if len(Alist) == 1:
        print(Alist[0])

    else:
        mid = len(Alist)  // 2
        left = Alist[:mid]
        right = Alist[mid:]
        rec(left)
        rec(right)


rec(houses)
