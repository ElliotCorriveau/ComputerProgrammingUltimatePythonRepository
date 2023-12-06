def is_alliteration(word1, word2):
    if word1[0] == word2[0]:
            return True
    else:
        return False
print("is_alliteration --------------------------------------") 
print(is_alliteration("word", "words"))
print(is_alliteration("word", "book"))

def count_vowels(word):
    count = 0
    for vowels in word:
        if vowels in "aeiou":
            count = count + 1
    return count 
print("count_vowels --------------------------------------") 
print(count_vowels("aeiou"))
print(count_vowels("hello"))


def count_numbers(number):
    count = 0
    for numbers in number:
        if numbers in "1234567890":
            count = count + 1
    return count
print("count_numbers --------------------------------------") 
print(count_numbers("1, 2, 3"))
print(count_numbers("1"))
print(count_numbers("sale for 5.99"))

def count_target_letters(word, character):
    count = 0
    for letter in word:
        if character == letter:
            count = count + 1
    return count
print("count_target_letters --------------------------------------") 
print(count_target_letters("hello", "l"))

def in_alphabetical_order(word):
    current = "a"
    for letter in word:
        if letter < current:
            return False
        else:
            current = letter
    return True       
print("in_alphabetical_order --------------------------------------") 
print(in_alphabetical_order("abc"))
print(in_alphabetical_order("acb"))

def alternate_case(word):
    next_upper = True 
    result = ""
    for letter in word:
        if next_upper == True:
            result = result + letter.upper()
            next_upper = False
        else:
            result = result + letter
            next_upper = True
    return result
print("alternate_case --------------------------------------") 
print(alternate_case("python"))

def remove_vowels(word):
    result = ""
    for letter in word:
        if letter in "aeiou":
            pass
        else:
            result = result + letter
    return result
print("remove_vowels --------------------------------------") 
print(remove_vowels("hello"))

def to_camel_case(words):
    next_upper = False
    result = ""
    for letter in words:
        if letter == " ":
            next_upper = True
            result = result + letter

        elif next_upper == True:
            result = result + letter.upper()
            next_upper = False
        else:
            result = result + letter 
        result = result.strip()
    return result
print("to_camel_case --------------------------------------") 
print(to_camel_case("hello how are you"))


def to_snake_case(words):
    result = words.replace(" ","_")
    return result
print("to_snake_case --------------------------------------") 
print(to_snake_case("hello how are you"))


def without_duplicates(integers):
    previous = ""
    result = []
    for number in integers:
        if number == previous:
            previous = number
        else:
            result.append(number)
            previous = number
    return result
print("without_duplicates --------------------------------------") 
print(without_duplicates([1, 1, 2, 3]))

def filter_valid_act_score(scores):
    result = []
    for score in scores:
        if score > 0 and score < 37:
            result.append(score)
        else:
            pass
    return result 
print("filter_valid_act_score --------------------------------------") 
print(filter_valid_act_score([37, 36, 1, 0]))
