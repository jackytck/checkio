#!/opt/local/bin/python3.3
golf=lambda x:next(x for x in range(x+1,4**9) if str(x)==str(x)[::-1]*all(x%i for i in range(2,x)))

if __name__ == '__main__':
    assert golf(2) == 3
    assert golf(13) == 101
    assert golf(101) == 131
    assert golf(31) == 101
    assert golf(130) == 131
    assert golf(5157) == 10301
