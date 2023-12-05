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


def all_the_same(nums):
    count = 0
    numsTrue = 0
    while count == 0:
        for num in nums:
            if num == nums[0]:
                numsTrue = numsTrue + 1
            else:
                count = count + 1
                return False
            if numsTrue == len(nums):
                return True

print("all_the_same --------------------------------------")   
print(all_the_same([1, 2, 3]))
print(all_the_same([1, 1, 1]))


def increasing(nums):
    greatest = nums[0]
    count = 1
    for num in nums:
        if greatest < num:
            greatest = num
            count = count + 1

    if count == len(nums):
        return True
    else:
        return False
        
print("increasing --------------------------------------")   
print(increasing([1, 2, 3]))
print(increasing([1, 1, 1]))


def is_incrementing(nums):
    greatest = nums[0]
    for num in nums:
        if num == greatest + 1:
            return True
    else:
        return False
print("is_incrementing --------------------------------------")   
print(is_incrementing([1, 2, 3]))
print(is_incrementing([1, 1, 1]))
print(is_incrementing([4, 5, 6]))
    
def has_adjacent_repeat(nums):
    prev = 99999999999999999999999
    for num in nums:
        if num == prev:
            prev = num
            return True
        else: 
            prev = num
    else:
        return False
print("had_adjacent_repeat --------------------------------------")   
print(has_adjacent_repeat([1, 2, 3]))
print(has_adjacent_repeat([1, 1, 1]))
print(has_adjacent_repeat([4, 4, 6]))


def sum_with_skips(nums):
    total = 0
    ignoring = False
    for num in nums:
        if num == -1 and ignoring == False:
            ignoring = True
        elif num == -1 and ignoring == True:
            ignoring = False
        elif ignoring == False:
            total = total + num
    return total

print("sum_with_skips --------------------------------------")   
print(sum_with_skips([1, 2, 3, -1, 4, 5, 6, -1, 7]))
print(sum_with_skips([1, -1, 2, -1, 3]))
print(sum_with_skips([-1, 1, 2, 3, -1]))
print(sum_with_skips([1, 1, 1, -1, 1, 1, 1, 1, -1, 1, 1, 1]))


        