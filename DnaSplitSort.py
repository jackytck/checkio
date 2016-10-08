#!/opt/local/bin/python3.3
golf=lambda s,p:''.join(sorted([s[i*p:(i+1)*p] for i in range(len(s)//p)],key=lambda s:sum(x>y for i,x in enumerate(s) for y in s[i+1:])))

if __name__ == '__main__':
    assert golf("ACGGCATAACCCTCGA",3) == "ACGCCCTAATCGGCA"
