import random

def generate_number(low,high):
    return random.randint(low,high)

def check_guess(secret,guess):
    if guess < secret:
        return"low"
    elif guess > secret:
        return"high"
    else:
        return"correct"