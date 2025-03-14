import random

def get_random_code():
    numbers = "0123456789"
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_chars = "!@#$%^&*()_+-=[]{}|;':\"<>,./?`~"
    code = ""
    for i in range(8):
        code += random.choice(numbers)
        code += random.choice(letters)
        code += random.choice(special_chars)
    return code
