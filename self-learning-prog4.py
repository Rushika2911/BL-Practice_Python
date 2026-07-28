def count_characters(text):
    text = text.lower()
    count = {}

    for ch in text:
        if ch.isalpha():   
            if ch in count:
                count[ch] += 1
            else:
                count[ch] = 1

    return count

input_string = input("Input String: ")
result = count_characters(input_string)
print("Character Counts:", result)