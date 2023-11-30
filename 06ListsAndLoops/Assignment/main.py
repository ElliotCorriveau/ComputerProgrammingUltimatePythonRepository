def count_failing_grades(grades):
    for grade in grades:
        count = 0
        if grade < 60:
            count = count + 1 
            return count
print(count_failing_grades([70, 59, 60]))


def count_act_scores(scores):
    count = 0
    for score in scores:
        if score > 0 and score < 37:
            count = count + 1
    return count
print(count_act_scores([1, 36, 37, 0, 5]))


def number_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total
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
print(average_act_score([1, 17, 37]))

