import sys


def nt(num):
    n = j = 0
    s = bin(num)[2:]
    for i in range(len(s) - 1, -1, -1):
        if s[i] == '0':
            n += i - j
            j += 1
    return n


with open(sys.argv[1]) as f:
    for i, line in enumerate(f):
        if i == 0: continue
        print('MAT' if nt(int(line)) % 2 == 0 else 'PAT')
