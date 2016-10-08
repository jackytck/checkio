#!/opt/local/bin/python3.3
def check_pangram(text):
    return len(set(t.lower() for t in text if t.isalpha())) == 26

if __name__ == '__main__':
    assert check_pangram("The quick brown fox jumps over the lazy dog."), "brown fox"
    assert not check_pangram("ABCDEF"), "ABC"
    assert check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?"
