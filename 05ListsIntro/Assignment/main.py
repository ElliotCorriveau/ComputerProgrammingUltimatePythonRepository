def make_abc():
    return ["a, b, c"]
print("Demonstrate make_abc =>", make_abc())

def equal_edges(integers):
    first = integers[0]
    last = integers[-1]
    if int(first) == int(last):
        return True
    else:
        return False
    
print("Demonstrate equal_edges [1, 2, 1] =>", equal_edges("1, 2, 1"))
print("Demonstrate equal_edges [1, 2, 3] =>", equal_edges("1, 2, 3"))

def common_edge(list1, list2):
    first1 = list1[0]
    first2 = list2[0]
    last1 = list1[-1]
    last2 = list2[-1]

    if first1 == first2 or first1 == last2:
        return True
    else:
        return False
print("Demonstrate common_edge [1, 2, 3], [1, 2, 3] =>", common_edge([1, 2, 3], [1, 2, 3]))
print("Demonstrate common_edge [1, 2, 3], [4, 5, 6] =>", common_edge([1, 2, 3], [4, 5, 6]))

def all_the_same(list):
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first == middle and first == last:
        return True
    else:
        return False
print("Demonstrate all_the_same [5, 5, 5] =>", all_the_same([5, 5, 5]))
print("Demonstrate all_the_same [5, 4, 5] =>", all_the_same([5, 4, 5]))

def all_unique(list):
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first != middle and first != last:
        return True
    else:
        return False
print("Demonstrate all_unique [1, 2, 3] = >", all_unique([1, 2, 3]))
print("Demonstrate all_unique [1, 1, 1] = >", all_unique([1, 1, 1]))

def increasing(list):
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first < middle and first < last and middle < last and middle < last:
        return True
    else:
        return False
print("Demonstrate increasing [1, 2, 3] =>", increasing([1, 2, 3]))
print("Demonstrate increasing [1, 4, 3] =>", increasing([1, 4, 3]))

def all_true(list):
    first = list[0]
    middle = list[1]
    last = list[-1]
    if first == True and middle == True and last == True:
        return True
    if first == False and middle == False and last == False:
        return True
    else:
        return False
print("Demonstrate all_true [True, True, True] =>", all_true([True, True, True]))
print("Demonstrate all_true [True, False, True] =>", all_true([True, False, True]))
print("Demonstrate all_true [False, False, False] =>", all_true([False, False, False]))


def mostly_true(list):
    first = list[0]
    middle = list[1]
    last = list[-1]
    if (first == True and middle == True) or (first == True and last == True) or (middle == True and last == True):
        return True
    
    if first == False and middle == False or first == False and last == False or middle == False and last == False:
        return False
    else:
        return False
print("Demonstrate mostly_true [False, True, False] =>", mostly_true([False, True, False]))
print("Demonstrate mostly_true [True, True, False] =>", mostly_true([True, True, False]))
print("Demonstrate mostly_true [False, False, False] =>", mostly_true([False, False, False]))
    

    