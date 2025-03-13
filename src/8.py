import random
def get_random_number(minimum: int, maximum: int) -> int:
    return random.randint(minimum, maximum)

print(get_random_number(10, 20))
