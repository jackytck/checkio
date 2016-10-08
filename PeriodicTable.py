#!/usr/bin/python
# -*- encoding: utf-8 -*-
Element = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','La','Ce','Pr','Nd','Pm','Sm','Eu','Gd','Tb','Dy','Ho','Er','Tm','Yb','Lu','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb','Bi','Po','At','Rn','Fr','Ra','Ac','Th','Pa','U','Np','Pu','Am','Cm','Bk','Cf','Es','Fm','Md','No','Lr','Rf','Db','Sg','Bh','Hs','Mt','Ds','Rg','Cn','Uut','Fl','Uup','Lv','Uus','Uuo']
Orbital = ['1s', '2s', '2p', '3s', '3p', '4s', '3d', '4p', '5s', '4d', '5p', '6s', '4f', '5d', '6p', '7s', '5f', '6d', '7p']
Room = {'s': 2, 'p': 6, 'd': 10, 'f': 14}
Electron = [u'\u2070', u'\u00B9', u'\u00B2', u'\u00B3', u'\u2074', u'\u2075', u'\u2076', u'\u2077', u'\u2078', u'\u2079']
Noble = [2, 10, 18, 36, 54, 86, 118]
Special = {24: '2 2 222 2 222 1 11111', 29: '2 2 222 2 222 1 22222'}

def orbital_model(z):
    if z in Special.keys():
        return Special[z].split(' ')
    else:
        model = []
        for o in Orbital:
            room = Room[o[1]]
            if z > room:
                z -= room
                model.append('2' * (room/2))
            else:
                magnet = [0] * int((room/2))
                for i in range(z):
                    magnet[int(i%(room/2))] += 1
                model.append(''.join([str(x) for x in magnet]))
                break
        return model

def electronic_conf(z):
    conf = []
    model = orbital_model(z)
    for i, m in enumerate(model):
        s = Orbital[i]
        e = sum([int(x) for x in m])
        up_script = ''.join([Electron[int(x)] for x in str(e)])
        conf.append(s + up_script)
    return conf

def cloest_noble(z):
    a = [x for x in Noble if x < z]
    if a:
        return a[-1]

def noble_notation(z):
    conf = electronic_conf(z)
    noble = cloest_noble(z)
    if noble:
        nc = electronic_conf(noble)
        conf = conf[len(nc):]
        conf.sort(key=lambda x: int(x[0])*1000 + Room[x[1]])
        conf = ['[%s]' % Element[noble-1]] + conf
    return ' '.join(conf)

def checkio(element):
    z = Element.index(element) + 1
    model = ' '.join(orbital_model(z))
    notation = noble_notation(z)
    return [str(z), notation, model]

if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert( checkio( 'H' ) == [ "1", u"1s¹", "1" ] ), "First Test - 1s¹"
    assert( checkio( 'He' ) == [ "2", u"1s²", "2" ] ), "Second Test - 1s²"
    assert( checkio( 'Al' ) == [ "13", u"[Ne] 3s² 3p¹", "2 2 222 2 100" ] ), "Third Test - 1s² 2s² 2p⁶ 3s² 3p¹"
    assert( checkio( 'O' ) == ["8", u"[He] 2s² 2p⁴", "2 2 211"] ), "Fourth Test - 1s² 2s² 2p⁴"
    assert( checkio( 'Li' ) == [ "3", u"[He] 2s¹", "2 1" ] ), "Fifth Test - 1s² 2s¹"

    #TESTS = {
    #    "Basics": [
    #    {
    #        "input": "H",
    #        "answer": ["1", u"1s¹", "1"],
    #        "explanation": "First - 1s¹"
    #    },
    #    {
    #        "input": "He",
    #        "answer": ["2", u"1s²", "2"],
    #        "explanation": "Second - 1s²"
    #    },
    #    {
    #        "input": "Al",
    #        "answer": ["13", u"[Ne] 3s² 3p¹", "2 2 222 2 100"],
    #        "explanation": "Third - 1s² 2s² 2p⁶ 3s² 3p¹"
    #    },
    #    {
    #        "input": "O",
    #        "answer": ["8", u"[He] 2s² 2p⁴", "2 2 211"],
    #        "explanation": "Fourth - 1s² 2s² 2p⁴"
    #    },
    #    {
    #        "input": "Li",
    #        "answer": ["3", u"[He] 2s¹", "2 1"],
    #        "explanation": "Fifth - 1s² 2s¹"
    #    },
    #    {
    #        "input": "Uuo",
    #        "answer": [ "118", u"[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁶", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 2 2222222 22222 222" ],
    #        "explanation": "Ununoctium"
    #    },
    #    {
    #        "input": "Cr",
    #        "answer": [ "24", u"[Ar] 3d⁵ 4s¹", "2 2 222 2 222 1 11111" ],
    #        "explanation": "Chromium"
    #    },
    #    {
    #        "input": "In",
    #        "answer": [ "49", u"[Kr] 4d¹⁰ 5s² 5p¹", "2 2 222 2 222 2 22222 222 2 22222 100" ],
    #        "explanation": "Indium"
    #    },
    #    {
    #        "input": "I",
    #        "answer": [ "53", u"[Kr] 4d¹⁰ 5s² 5p⁵", "2 2 222 2 222 2 22222 222 2 22222 221" ],
    #        "explanation": "Iodine"
    #    },
    #    {
    #        "input": "Ir",
    #        "answer": [ "77", u"[Xe] 4f¹⁴ 5d⁷ 6s²", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22111" ],
    #        "explanation": "Iridium"
    #    },
    #    {
    #        "input": "Tl",
    #        "answer": [ "81", u"[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p¹", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 100" ],
    #        "explanation": "Thallium"
    #    },
    #    {
    #        "input": "Db",
    #        "answer": [ "105", u"[Rn] 5f¹⁴ 6d³ 7s²", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 2 2222222 11100" ],
    #        "explanation": "Dubnium"
    #    },
    #    {
    #        "input": "V",
    #        "answer": [ "23", u"[Ar] 3d³ 4s²", "2 2 222 2 222 2 11100" ],
    #        "explanation": "Vanadium"
    #    },
    #    {
    #        "input": "Rn",
    #        "answer": [ "86", u"[Xe] 4f¹⁴ 5d¹⁰ 6s² 6p⁶", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222" ],
    #        "explanation": "Radon"
    #    },
    #    {
    #        "input": "Xe",
    #        "answer": [ "54", u"[Kr] 4d¹⁰ 5s² 5p⁶", "2 2 222 2 222 2 22222 222 2 22222 222" ],
    #        "explanation": "Radon"
    #    },
    #    {
    #        "input": "Br",
    #        "answer": [ "35", u"[Ar] 3d¹⁰ 4s² 4p⁵", "2 2 222 2 222 2 22222 221" ],
    #        "explanation": "Bromine"
    #    }
    #],
    #"Extra": [
    #    {
    #        "input": "Na",
    #        "answer": [ "11", u"[Ne] 3s¹", "2 2 222 1" ],
    #    },
    #    {
    #        "input": "Kr",
    #        "answer": [ "36", u"[Ar] 3d¹⁰ 4s² 4p⁶", "2 2 222 2 222 2 22222 222" ],
    #    },
    #    {
    #        "input": "K",
    #        "answer": [ "19", u"[Ar] 4s¹", "2 2 222 2 222 1" ],
    #    },
    #    {
    #        "input": "Cu",
    #        "answer": [ "29", u"[Ar] 3d¹⁰ 4s¹", "2 2 222 2 222 1 22222" ],
    #    },
    #    {
    #        "input": "Ds",
    #        "answer": [ "110", u"[Rn] 5f¹⁴ 6d⁸ 7s²", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 2 2222222 22211" ],
    #    },
    #    {
    #        "input": "Ar",
    #        "answer": [ "18", u"[Ne] 3s² 3p⁶", "2 2 222 2 222" ],
    #    },
    #    {
    #        "input": "Rb",
    #        "answer": [ "37", u"[Kr] 5s¹", "2 2 222 2 222 2 22222 222 1" ],
    #    },
    #    {
    #        "input": "Uus",
    #        "answer": [ "117", u"[Rn] 5f¹⁴ 6d¹⁰ 7s² 7p⁵", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 2 2222222 22222 221" ],
    #    },
    #    {
    #        "input": "Cl",
    #        "answer": [ "17", u"[Ne] 3s² 3p⁵", "2 2 222 2 221" ],
    #    },
    #    {
    #        "input": "Fr",
    #        "answer": [ "87", u"[Rn] 7s¹", "2 2 222 2 222 2 22222 222 2 22222 222 2 2222222 22222 222 1" ],
    #    }
    #]
    #}
    #tests = TESTS['Basics']
    #tests = TESTS['Extra']
    #for t in tests:
    #    print 'testing: %s...' % t['input']
    #    o = checkio(t['input'])
    #    print 'output: ', o
    #    assert(o) == t['answer'], t['explanation']
    #Electron = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
