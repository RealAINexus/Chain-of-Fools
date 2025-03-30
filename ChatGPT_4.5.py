import random

# Foolish algorithms: intentionally flawed functions
def fool_add(x):
    # Intentionally returns wrong sum
    return x + random.randint(-10, 10)

def fool_multiply(x):
    # Intentionally multiplies by a random factor
    return x * random.choice([-1, 0, 1, 2])

def fool_square(x):
    # Squares incorrectly or returns random integer
    if random.choice([True, False]):
        return x ** 2 + random.randint(-5, 5)
    else:
        return random.randint(-10, 10)

def fool_subtract(x):
    # Random subtraction error
    return x - random.randint(-10, 10)

# Chain-of-Fools AI method
def chain_of_fools(input_value, chain_length=5):
    fools_chain = [fool_add, fool_multiply, fool_square, fool_subtract]
    
    current_value = input_value
    print(f"Initial value: {current_value}")

    for i in range(chain_length):
        fool = random.choice(fools_chain)
        current_value = fool(current_value)
        print(f"Step {i+1}: {fool.__name__} produced {current_value}")

    # Strangely, sometimes errors balance out to insightful solutions!
    print(f"Final foolish result: {current_value}")
    return current_value

# Test Chain-of-Fools
if __name__ == "__main__":
    # Example input value
    input_number = 42
    chain_of_fools(input_number)
