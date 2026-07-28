def count_char(str1):
    letters=0
    digit=0
    special=0
    for ch in str1:
        if ch.isalpha():
            letters+=1
        elif ch.isdigit():
            digit+=1
        else:
            special+=1
    return letters, digit,special

def mainm():
    str1= 'P@#yn26at^&i5ve'

    letters, digits, special_char= count_char(str1)
    print(f"letters: {letters}")
    print(f"digits: {digits}")
    print(f"special charcters: {special_char}")

if __name__=="__main__":
    mainm()