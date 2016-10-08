#!/opt/local/bin/python3.3
def letter_queue(commands):
    q = []
    for c in commands:
        if c == 'POP':
            q = q[1:]
        else:
            q.append(c[-1])
    return ''.join(q)

if __name__ == '__main__':
    assert letter_queue(["PUSH A", "POP", "POP", "PUSH Z", "PUSH D", "PUSH O", "POP", "PUSH T"]) == "DOT", "dot example"
    assert letter_queue(["POP", "POP"]) == "", "Pop, Pop, empty"
    assert letter_queue(["PUSH H", "PUSH I"]) == "HI", "Hi!"
    assert letter_queue([]) == "", "Nothing"
