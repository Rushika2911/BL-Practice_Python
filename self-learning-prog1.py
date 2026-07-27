import random

numbers = []
for i in range(1000):
    numbers.append(random.uniform(0.0, 100.0))


bucket1 = 0   
bucket2 = 0  
bucket3 = 0  
bucket4 = 0  
bucket5 = 0   

for num in numbers:
    if 0 <= num < 20:
        bucket1 += 1
    elif 20 <= num < 40:
        bucket2 += 1
    elif 40 <= num < 60:
        bucket3 += 1
    elif 60 <= num < 80:
        bucket4 += 1
    else:   
        bucket5 += 1

print("Bucket 0 to 20 :", bucket1, "numbers")
print("Bucket 20 to 40:", bucket2, "numbers")
print("Bucket 40 to 60:", bucket3, "numbers")
print("Bucket 60 to 80:", bucket4, "numbers")
print("Bucket 80 to 100:", bucket5, "numbers")