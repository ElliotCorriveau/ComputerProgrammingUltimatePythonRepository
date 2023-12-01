def count_failing_grades(grades):
    for grade in grades:
        count = 0
        if grade < 60:
            count = count + 1 
            return count
print("count_failing_grades --------------------------------------")
print(count_failing_grades([70, 59, 60]))


def count_act_scores(scores):
    count = 0
    for score in scores:
        if score > 0 and score < 37:
            count = count + 1
    return count
print("count_act_scores --------------------------------------")
print(count_act_scores([1, 36, 37, 0, 5]))


def number_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
print("number_sum --------------------------------------")
print(number_sum([1, 2, 3, 4]))


def average_act_score(scores):
    count = 0
    total = 0
    for score in scores:
        if score > 0 and score < 37:
            count = count + 1
            total = score + total
    mean = total / count
    return mean
print("average_act_score --------------------------------------")
print(average_act_score([1, 17, 37]))


def all_true(booleans):
    count  = 0
    for boolean in booleans:
        if boolean == True:
            count = count + 1
    if count == len(booleans):
        return True
    else:
        return False
print("all_true --------------------------------------")   
print(all_true([True, False, False]))
print(all_true([True, True, True]))

def any_true(booleans):
    for boolean in booleans:
        if boolean == True:
            return True
    else:
        return False
print("any_true --------------------------------------")
print(any_true([True, False, True]))
print(any_true([False, False, False]))


def has_vowel(vowels):
    for vowel in vowels:
        if vowel in ["a", "e", "i", "o", "u"]:
            return True
        else:
            return False
print("has_vowel --------------------------------------")
print(has_vowel(["a", "e", "i", "o", "u"]))
print(has_vowel(["a,", "e", "i", "o", "r"]))

def mostly_true(booleans):
    count = 0
    for boolean in booleans:
        if boolean == True:
            count = count + 1
    if count > len(booleans) / 2: 
        return True
    else:
        return False
print("mostly_true --------------------------------------")
print(mostly_true([True, False, True]))
print(mostly_true([False, False, True]))
