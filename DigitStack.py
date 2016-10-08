#!/opt/local/bin/python3.3
def digit_stack(commands):
    ret, stack = 0, []
    for c in commands:
        try:
            if c == 'POP':
                ret += stack.pop()
            elif c == 'PEEK':
                ret += stack[-1]
            else:
                stack.append(int(c.split(' ')[1]))
        except IndexError:
            pass
    return ret

if __name__ == '__main__':
    assert digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
    assert digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
    assert digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
    assert digit_stack([]) == 0, "Nothing"
