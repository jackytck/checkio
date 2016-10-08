#!/opt/local/bin/python3.3
r=range(-1,2)
e=enumerate
u=sum
q=lambda d,x,y:u(d.get((x+i,y+j),' ')!=' ' for i in r for j in r)==8
d=lambda s:{(i,j): y for i,x in e(s) for j,y in e(x)}
golf=lambda s:u(1 for k,v in d(s).items() if v == ' ' and q(d(s),*k))

if __name__ == '__main__':
    assert golf(["How are you doing?",
      "I'm fine. OK.",
      "Lorem Ipsum?",
      "Of course!!!",
      "1234567890",
      "0        0",
      "1234567890",
      "Fine! good buy!"]) == 3
