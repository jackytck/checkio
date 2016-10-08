#!/opt/local/bin/python3.3
def checkio(number):
    ret = ''
    if number % 3 == 0:
        ret += 'Fizz'
    if number % 5 == 0:
        if ret:
            ret += ' '
        ret += 'Buzz'
    if not ret:
        ret = str(number)
    return ret

if __name__ == '__main__':
    assert checkio(15) == "Fizz Buzz", "15 is divisible by 3 and 5"
    assert checkio(6) == "Fizz", "6 is divisible by 3"
    assert checkio(5) == "Buzz", "7 is divisible by 5"
    assert checkio(7) == "7", "15 is not divisible by 3 or 5"
