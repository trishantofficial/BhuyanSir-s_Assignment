def main():
    fibonacci()

def fibonacci():
    a = 0
    b = 1
    print a
    print b
    for num in range(0, 100):
        temp = a + b
        a = b
        b = temp
        print temp

if __name__ == '__main__':
    main()