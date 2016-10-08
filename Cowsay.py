#!/opt/local/bin/python3.3
import re
import textwrap

COW = r'''
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''


def cowsay(text):
    wrap = textwrap.fill(re.sub('\s+', ' ', text), 39).split('\n')
    if text[-1] == ' ':
        if len(wrap[-1]) == 39:
            wrap[-1] += '\n'
        wrap[-1] += ' '
    length = max(len(x) for x in wrap)
    wrap = ['| %s |' % x.ljust(length) for x in wrap]
    if len(wrap) == 1:
        wrap[0] = '<%s>' % wrap[0][1:-1]
    else:
        wrap[0] = '/%s\\' % wrap[0][1:-1]
        wrap[-1] = '\\%s/' % wrap[-1][1:-1]
    say = ['\n ' + '_' * (length + 2)]
    say.extend(wrap)
    say.append(' ' + '-' * (length + 2))
    return '\n'.join(say) + COW

if __name__ == '__main__':
    expected_cowsay_one_line = r'''
 ________________
< Checkio rulezz >
 ----------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''
    expected_cowsay_two_lines = r'''
 ________________________________________
/ A                                      \
\ longtextwithonlyonespacetofittwolines. /
 ----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    expected_cowsay_many_lines = r'''
 _________________________________________
/ Lorem ipsum dolor sit amet, consectetur \
| adipisicing elit, sed do eiusmod tempor |
| incididunt ut labore et dolore magna    |
\ aliqua.                                 /
 -----------------------------------------
        \   ^__^
         \  (oo)\_______
            (__)\       )\/\
                ||----w |
                ||     ||
'''

    cowsay_one_line = cowsay('Checkio rulezz')
    assert cowsay_one_line == expected_cowsay_one_line, 'Wrong answer:\n%s' % cowsay_one_line

    cowsay_two_lines = cowsay('A longtextwithonlyonespacetofittwolines.')
    assert cowsay_two_lines == expected_cowsay_two_lines, 'Wrong answer:\n%s' % cowsay_two_lines

    cowsay_many_lines = cowsay('Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do '
                                'eiusmod tempor incididunt ut labore et dolore magna aliqua.')
    assert cowsay_many_lines == expected_cowsay_many_lines, 'Wrong answer:\n%s' % cowsay_many_lines
    print(cowsay('b '))
