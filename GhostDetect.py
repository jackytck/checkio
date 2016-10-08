#!/opt/local/bin/python3.3
def recognize(number):
    return len(set(bin(number)[2:].replace('0', ' ').split())) == 1

if __name__ == '__main__':
    assert recognize(21) == True, "First example"
    assert recognize(1587) == True, "Second example"
    assert recognize(3687) == False, "Thid example"
