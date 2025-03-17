import random
def generate_random_code():
    """Returns a randomly generated 8-digit code"""
    return "".join(str(random.randint(0, 9)) for _ in range(8))
