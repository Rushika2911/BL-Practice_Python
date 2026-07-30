# a = int(input("Enter the value of a: "))
# b = int(input("Enter the value of b: "))

# print("Initial Value of a & b are")
# print("a =", a)
# print("b =", b)

# temp = a
# a = b
# b = temp

# print("\nAfter traditional swapping:")
# print("a =", a)
# print("b =", b)


a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

print("Initial Value of a & b are")
print("a =", a)
print("b =", b)

a, b = b, a

print("\nAfter pythonic swapping:")
print("a =", a)
print("b =", b)