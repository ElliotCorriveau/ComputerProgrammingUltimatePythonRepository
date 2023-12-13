import csv
f = open("../data/4000-most-common-english-words.csv", "r")
words = f.read().split("\n")
f.close()

def find_average_word_length(words):
    count = 0 
    total = 0
    final = 0
    for word in words:
        total = total + len(word)
        count = count + 1
    final = total / count
    final = round(final, 2)


    return final
print(find_average_word_length(words))

def word_with_most_vowels(words):
    winning_word  = "" 
    winning_count = 0
    for word in words:
        vowelcount = 0
        # count vowels
        for letter in word:
            if letter in "aeiou":
                vowelcount = vowelcount + 1
        # if the current vowelcount is higher than the max vowelcount,
            if vowelcount > winning_count:
                winning_word = word
                winning_count = vowelcount
        # update the winners
    return winning_word, winning_count
    
print(word_with_most_vowels(words))

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 

def number_of_abcdf(reader):
    a_count = 0
    b_count = 0
    c_count = 0
    d_count = 0
    f_count = 0
    for row in reader:
        name, gradelevel, percent = row
        percent = int(percent)
        if percent > 89:
            a_count = a_count + 1
        elif percent > 79:
            b_count = b_count +1
        elif percent > 69:
         c_count = c_count + 1
        elif percent > 59:
            d_count = d_count + 1
        else:
            f_count = f_count + 1
    return a_count, b_count, c_count, d_count, f_count
print (number_of_abcdf(reader))

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
def average_grades(reader):
    fcount = 0 
    ftotal = 0
    socount = 0
    sototal = 0
    juncount = 0
    juntotal = 0
    sencount = 0
    sentotal = 0
    f_average = 0
    so_average = 0
    jun_average = 0
    sen_average = 0
    for row in reader:
        name, gradelevel, percent = row
        gradelevel = int(gradelevel)
        percent = int(percent)
        if gradelevel == 9:
            ftotal = ftotal + percent
            fcount = fcount + 1
            f_average = ftotal / fcount

        if gradelevel == 10:
            sototal = sototal + percent
            socount = socount + 1
            so_average = sototal / socount

        if gradelevel == 11:
            juntotal = juntotal + percent
            juncount = juncount + 1
            jun_average = juntotal / juncount

        if gradelevel == 12:
            sentotal = sentotal + percent
            sencount = sencount + 1
            sen_average = sentotal / sencount
    return  round(f_average, 2), round(so_average, 2), round(jun_average, 2), round(sen_average, 2)
print(average_grades(reader))

f = open("../data/gradebook_data.csv", "r")
reader = csv.reader(f) 
def seniors_with_f(reader):

    for row in reader:
        name, gradelevel, percent = row
        gradelevel = int(gradelevel)
        percent = int(percent)
        if gradelevel == 12 and percent < 60:
           print(name)

    return ""

print(seniors_with_f(reader))