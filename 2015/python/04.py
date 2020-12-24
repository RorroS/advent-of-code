import hashlib

KEY = b'yzbqklnj'

def solve(n):
    i = 1
    while True:
        hex_md5 = hashlib.md5(KEY + bytes(str(i), 'utf-8')).hexdigest()
        if hex_md5[:n] == "0" * n:
            return i
        i += 1


if __name__ == '__main__':
    print("p1:", solve(5))
    print("p2:", solve(6))

