import random
import time

def is_prime(num):
    if num < 2:
        return False

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def generate_random_numbers(n):
    numbers = []

    for i in range(n):
        numbers.append(random.randint(1, 100))

    return numbers

def remove_primes(numbers):
    new_list = []

    for num in numbers:
        if not is_prime(num):
            new_list.append(num)

    return new_list

prime_list = []

for i in range(1, 101):
    if is_prime(i):
        prime_list.append(i)


def remove_primes_optimized(numbers):
    new_list = []
    for num in numbers:
        if num not in prime_list:
            new_list.append(num)

    return new_list

sizes = [100, 10000, 100000]

print("========== Normal Method ==========\n")

for n in sizes:

    print(f"Computing execution time for list size: {n}")

    start_generate = time.time()
    numbers = generate_random_numbers(n)
    end_generate = time.time()
    start_remove = time.time()
    result = remove_primes(numbers)
    end_remove = time.time()
    generation_time = end_generate - start_generate
    remove_time = end_remove - start_remove
    total_time = generation_time + remove_time
    print(f"Time taken to generate random numbers: {generation_time:.6f} seconds")
    print(f"Time taken to remove prime numbers: {remove_time:.6f} seconds")
    print(f"Total execution time: {total_time:.6f} seconds\n")

print("========== Optimized Method ==========\n")

for n in sizes:

    print(f"Computing execution time for list size: {n}")

    start_generate = time.time()
    numbers = generate_random_numbers(n)
    end_generate = time.time()
    start_remove = time.time()
    result = remove_primes_optimized(numbers)
    end_remove = time.time()
    generation_time = end_generate - start_generate
    remove_time = end_remove - start_remove
    total_time = generation_time + remove_time
    
    print(f"Time taken to generate random numbers: {generation_time:.6f} seconds")
    print(f"Time taken to remove prime numbers: {remove_time:.6f} seconds")
    print(f"Total execution time: {total_time:.6f} seconds\n")