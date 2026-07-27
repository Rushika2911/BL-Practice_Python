import random

# GST Rates
HOUSEHOLD_GST = 0.05
PROCESSED_FOOD_GST = 0.12

# Item List
items = [
    "Rice", "Wheat Flour", "Sugar", "Salt", "Milk",
    "Bread", "Biscuits", "Noodles", "Tea", "Coffee",
    "Banana", "Tomato", "Masala", "Cooking Oil", "Soap"
]

# Price List
prices = [
    60, 45, 50, 20, 30,
    40, 25, 35, 120, 180,
    15, 10, 200, 150, 35
]

# GST Category
# Household = 5%
# Processed = 12%

gst_category = [
    HOUSEHOLD_GST,      # Rice
    HOUSEHOLD_GST,      # Wheat Flour
    HOUSEHOLD_GST,      # Sugar
    HOUSEHOLD_GST,      # Salt
    HOUSEHOLD_GST,      # Milk
    PROCESSED_FOOD_GST, # Bread
    PROCESSED_FOOD_GST, # Biscuits
    PROCESSED_FOOD_GST, # Noodles
    PROCESSED_FOOD_GST, # Tea
    PROCESSED_FOOD_GST, # Coffee
    HOUSEHOLD_GST,      # Banana
    HOUSEHOLD_GST,      # Tomato
    PROCESSED_FOOD_GST, # Masala
    HOUSEHOLD_GST,      # Cooking Oil
    HOUSEHOLD_GST       # Soap
]

buyer = input("Enter the buyer name: ")

# Randomly choose 3 different items
selected_items = random.sample(range(len(items)), 3)

total = 0
gst = 0

print("\nRetail Invoicing App")
print("-" * 40)
print("Buyer Name:", buyer)
print("-" * 40)
print(f"{'Item':15}{'Qty':>6}{'Price':>10}")
print("-" * 40)

for index in selected_items:

    quantity = random.randint(1, 5)

    amount = prices[index] * quantity

    total += amount

    gst += amount * gst_category[index]

    print(f"{items[index]:15}{quantity:>6}{prices[index]:>10}")

print("-" * 40)
print(f"{'Total':25}Rs {total:.2f}")
print(f"{'GST':25}Rs {gst:.2f}")
print("-" * 40)
print(f"{'Total Billing':25}Rs {total + gst:.2f}")
print("-" * 40)