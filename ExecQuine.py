#!/opt/local/bin/python3.3
s='s=%r;quine=lambda:s%%s';quine=lambda:s%s
print("s='s=%r;quine=lambda:s%%s';quine=lambda:s%s")
print(quine())
