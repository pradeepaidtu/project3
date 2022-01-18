import math
import os


def sub(a, b):
    return math.floor(a - b)


def word_count(sentence, word):
    sentence = sentence.lower().split()
    if word in sentence:
        return sum([1 for x in sentence if x == word])
    else:
        return 0

