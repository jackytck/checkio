#!/opt/local/bin/python3.3
def checkio(first, second):
    return ','.join(sorted(set(first.split(',')) & set(second.split(','))))

if __name__ == '__main__':
    assert checkio("hello,world", "hello,earth") == "hello", "Hello"
    assert checkio("one,two,three", "four,five,six") == "", "Too different"
    assert checkio("one,two,three", "four,five,one,two,six,three") == "one,three,two", "1 2 3"
