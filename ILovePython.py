#!/opt/local/bin/python3.3
import random


def i_love_python():
    random.seed(0)
    s = list('hnPotylIo !e v')
    [random.shuffle(s) for i in range(100)]
    return ''.join(s)

if __name__ == '__main__':
    assert i_love_python() == "I love Python!"
