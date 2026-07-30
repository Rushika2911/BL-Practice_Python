squares=[num**2 for num in range(10)]

tup_sqr= tuple(squares)

print(f"3rd element: {tup_sqr[2]}")
print(f"5th element: {tup_sqr[4]}")
print(f"7th element: {tup_sqr[6]}")
print(tup_sqr[:3])
print(tup_sqr)