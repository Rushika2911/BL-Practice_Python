import re


# Function to check presence of "Modi"
def check_modi(news):
    return "modi" in news.lower()


# Function to count total words
def count_words(news):
    return len(news.split())


# Function to count occurrences of "the"
def count_the(news):
    words = news.lower().split()
    count = 0

    for word in words:
        # Remove punctuation before comparison
        word = word.strip('.,!?";:“”()')
        if word == "the":
            count += 1

    return count


# Function to check presence of digits
def has_digits(news):
    return any(char.isdigit() for char in news)


# Function to remove articles
def remove_articles(news):
    articles = {"a", "an", "the"}

    words = news.split()

    new_words = [
        word for word in words
        if word.strip('.,!?";:“”()').lower() not in articles
    ]

    return " ".join(new_words)


# Function to remove vowels
def remove_vowels(news):
    vowels = "aeiouAEIOU"

    result = []

    for word in news.split():
        new_word = "".join([ch for ch in word if ch not in vowels])
        result.append(new_word)

    return " ".join(result)


news_paragraph = """Government is set to issue Google a notice after the firm’s AI platform Gemini threw up unsubstantiated allegations in response to a query on PM Modi.
Minister of state for IT Rajeev Chandrasekhar took a serious view of the matter after it was flagged by a user on X.
These are direct violations of Rule 3(1)(b) of Intermediary Rules (IT rules) of IT act and violations of several provisions of the criminal code,
he posted on X, in a clear indication that govt intends to initiate action.
Gemini attributed allegations of rising authoritarianism and communalism under Modi to unnamed experts, as per the X post."""

print("Presence of 'Modi':", check_modi(news_paragraph))
print("Number of words:", count_words(news_paragraph))
print("Number of occurrences of 'the':", count_the(news_paragraph))
print("Presence of digits:", has_digits(news_paragraph))

compact_news = remove_articles(news_paragraph)
print("\nCompact news data without articles:")
print(compact_news)

compact_news_vowels = remove_vowels(compact_news)
print("\nCompact news data without vowels:")
print(compact_news_vowels)