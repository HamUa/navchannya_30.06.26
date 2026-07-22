import string
MAX_HASHTAG_LENGTH = 140
def make_hashtag(text: str) -> str:
    text_without_punctuation = ""

    for symbol in text:
        if symbol not in string.punctuation:
            text_without_punctuation += symbol

    words = text_without_punctuation.split()
    hashtag = "#"

    for word in words:
        hashtag += word.capitalize()

    return hashtag[:MAX_HASHTAG_LENGTH]


if __name__ == "__main__":
    user_text = input("Введіть рядок: ")
    print(make_hashtag(user_text))



