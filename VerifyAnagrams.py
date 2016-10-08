#!/opt/local/bin/python3.3
from collections import Counter


def trans(t):
    return t.replace(' ', '').lower()


def verify_anagrams(first_word, second_word):
    return Counter(trans(first_word)) == Counter(trans(second_word))

if __name__ == '__main__':
    assert isinstance(verify_anagrams("a", 'z'), bool), "Boolean!"
    assert verify_anagrams("Programming", "Gram Ring Mop") == True, "Gram of code"
    assert verify_anagrams("Hello", "Ole Oh") == False, "Hello! Ole Oh!"
    assert verify_anagrams("Kyoto", "Tokyo") == True, "The global warming crisis of 3002"
