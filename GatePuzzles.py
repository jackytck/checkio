#!/opt/local/bin/python3.3
import re
from fractions import Fraction
from operator import itemgetter


def likeness(w1, w2):
    ret = 0
    if w1[0] == w2[0]:
        ret += 10
    elif w1[-1] == w2[-1]:
        ret += 10
    if len(w1) > len(w2):
        w1, w2 = w2, w1
    ret += Fraction(len(w1), len(w2)) * 30
    ret += Fraction(len(set(w1) & set(w2)), len(set(w1 + w2))) * 50
    return ret


def find_word(message):
    words = [w.lower() for w in re.findall('\w+', message)][::-1]
    return max(((sum(likeness(w1, w2) for w2 in words), w1)
               for w1 in words), key=itemgetter(0))[1]


if __name__ == '__main__':
    assert find_word("Speak friend and enter.") == "friend", "Friend"
    assert find_word("Beard and Bread") == "bread", "Bread is Beard"
    assert find_word("The Doors of Durin, Lord of Moria. Speak friend and enter. "
                     "I Narvi made them. Celebrimbor of Hollin drew these signs") == "durin", "Durin"
    assert find_word("Aoccdrnig to a rscheearch at Cmabrigde Uinervtisy."
                     " According to a researcher at Cambridge University.") == "according", "Research"
    assert find_word("One, two, two, three, three, three.") == "three", "Repeating"
