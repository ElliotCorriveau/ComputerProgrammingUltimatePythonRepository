import random 

def number_guesser():
    rand_number = random.randint(1, 10)
    correct = False
    while correct == False:
        response = int(input("Please enter a number: "))
        if response == rand_number:
            correct = True
            print("Correct")
        elif response < rand_number:
            print("To low!")
        elif response > rand_number:
            print("To high!")

def number_guesser_with_lives():
    rand_number = random.randint(1, 10)
    correct = False
    lives = 3
    while correct == False:
        response = int(input("Please enter a number: "))
        if response == rand_number:
            corect = True
            print("Congratulations!")
        elif response > rand_number:
            print("To high, -1 life")
            lives = lives - 1
        elif response < rand_number:
            print("To low, -1 life.")
            lives = lives - 1
        else:
            print("invalid response")
        if lives == 0:
            correct = True


def vending_machine():
    amount_due = 50
    paid = False
    coin = 0
    change = 0
    while paid == False:
        print("Amount due =>", amount_due)
        coin = int(input("Please enter a coin amount."))
        if coin == 5:
            amount_due = amount_due - 5
        elif coin == 25:
            amount_due = amount_due - 25
        elif coin == 10:
            amount_due = amount_due - 10
        else:
            print("Invalid coin")
        if amount_due == 0:
            paid = True
            print("Have a good day!")
        if amount_due < 0:
            paid = True
            change = abs(amount_due)
            print("You will get back =>", change)
vending_machine()
