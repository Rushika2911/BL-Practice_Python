str1="P@#yn26at^&i5ve"

letters= sum(1 for ch in str1 if ch.isalpha())
digits= sum(1 for ch in str1 if ch.isdigit())
special_char= len(str1)-letters-digits


print(f"letters: {letters}")
print(f"digits: {digits}")
print(f"special charcters: {special_char}")