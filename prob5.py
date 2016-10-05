from itertools import product

def main():
    for x in product(['', '+', '-'], repeat=8):
        combo = (map(str, combine(range(1, 10), x)))
        string = ''.join(combo)
        if eval(string) == 100:
            print string + "=100"

def combine(a, b):
    return [v for p in map(None, a, b) for v in p if v]

if __name__ == '__main__':
    main()