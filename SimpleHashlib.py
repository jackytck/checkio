#!/opt/local/bin/python3.3
import hashlib


def checkio(string, algorithm):
    return getattr(hashlib, algorithm)(string.encode('utf-8')).hexdigest()

if __name__ == '__main__':
    assert checkio('welcome', 'md5') == '40be4e59b9a2a2b5dffb918c0e86b3d7'
    assert checkio('happy spam', 'sha224') == '6e9dc3e01d57f1598c2b40ce59fc3527e698c77b15d0840ae96a8b5e'
    assert checkio('密码', 'sha512') == '3ddc7f603e4311ffe52e6ab75c29cf8bc8634449a832b7896ba5c10b228bfd01b6e9d41bc7bc639e63db8f7141ddcb2d9751b673219dd5ffff5088c411b25690'
