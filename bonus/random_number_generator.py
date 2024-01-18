import random

upper_bound = int(input("Upper bonud: "))
lower_bound = int(input("Lower bonud: "))

def generate_random(lower, upper):
    return random.randint(lower,upper)

print(generate_random(lower_bound, upper_bound))