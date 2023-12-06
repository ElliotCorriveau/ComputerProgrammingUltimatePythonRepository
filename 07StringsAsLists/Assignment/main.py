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
    for letter in word:
        if next_upper == True:
            letter = letter.upper()
            next_upper = False
        else:
            next_upper = True
    return word
print("alternate_case --------------------------------------") 
print(alternate_case("python"))



