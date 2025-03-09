import random

def get_random_integer(min_value, max_value):
    return random.randint(min_value, max_value)

def get_random_string(length):
    return ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(length))
