words = ["hi", "python", "is", "cool", "code", "a"]


def is_long_word(word): return len(word) > 3


long_words = [word for word in words if is_long_word(word)]

print(long_words)
