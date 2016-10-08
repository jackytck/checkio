#!/usr/bin/python
import math

def checkio(data):
    'return the number of pages'
    height = data['height']
    width = data['width']
    text = data['text']

    def lines(s):
        if len(s) <= width:
            return 1
        if s[width] == ' ':
            return 1 + lines(s[width:].lstrip())
        if ' ' not in s[:width]:
            return 1 + lines(s[width:])
        for i in range(width):
            if s[width-1-i] == ' ':
                return 1 + lines(s[width-i:].lstrip())

    texts = [' '.join(x.split()) for x in text.split('\n')]
    if not texts:
        return 1
    ret = 0
    for t in texts:
        ret += lines(t)
    ret += text.count('\n')
    return int(math.ceil(ret / float(height)))
    
if __name__ == '__main__':
    assert checkio({'height':3,
             'width':5,
             'text': 'To be or not to be'
    }) == 2 , 'From description'
    
    assert checkio({'height':1,
             'width':5,
             'text': 'HI'
    }) == 1, 'with single sort word'
    
    assert checkio({'height':1,
             'width':5,
             'text': 'hello'
    }) == 1, 'with signle word with long as width'
    
    assert checkio({'height':3,
             'width':5,
             'text': ''
    }) == 1, 'one page for no words'
    
    assert checkio({'height':3,
             'width':5,
             'text': 'It\'s boooooooorrrrrrriiiiiinnnnggggg dude'
    }) == 3, 'With a one long word'
    
    assert  checkio({'height':3,
             'width':5,
             'text': '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Cras hendrerit enim ultricies justo tincidunt ut auctor ipsum hendrerit. Phasellus ultricies dolor eu arcu auctor a rutrum enim tristique. 
Phasellus purus odio, pharetra in sodales vel, adipiscing eget libero. Quisque rhoncus urna at ipsum tincidunt facilisis. In vitae diam dolor. 
Nullam eleifend aliquam porttitor. Curabitur viverra malesuada eleifend. Fusce eu dui quis neque accumsan consectetur id id metus. 
Cras rutrum purus sed massa malesuada in consequat augue viverra. Vestibulum consectetur lacinia commodo. 
Phasellus urna nisi, tincidunt a ullamcorper egestas, iaculis sed mauris.'''
    }) == 49 , 'Lorem ipsum'
    
    print 'All ok :)'
