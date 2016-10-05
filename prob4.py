def main():
    list = []
    listSize = int(raw_input('Enter size of list: '))
    for element in range(0, listSize):
        list.append(int(raw_input('Enter element' + str(element) + ': ')))
    makeBiggestNum(list)

def makeBiggestNum(list):
    list.sort(cmp=lambda a, b: -1 if str(b) + str(a) < str(a) + str(b) else 1)
    biggestNum = ''.join(str(element) for element in list)
    print 'Largest number found = ' + biggestNum

if __name__ == '__main__':
    main()