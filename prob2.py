def main():
    num1 = int(raw_input('Enter number of elements in list 1 = '))
    num2 = int(raw_input('Enter number of elements in list 2 = '))
    print 'Enter elements of list 1 :'
    list1 = []
    for i in range(0,num1):
        list1.append(raw_input())
    print 'Enter elements of list 2 :'
    list2 = []
    for i in range(0,num2):
        list2.append(raw_input())
    list1.reverse()
    list2.reverse()
    combineList(list1,list2)

def combineList(list1, list2):
    listSize = len(list1) + len(list2)
    finalList = []
    for element in range(0,listSize):
        if len(list1) != 0:
            finalList.append(list1.pop())
        if len(list2) != 0:
            finalList.append(list2.pop())
    print finalList

if __name__ == '__main__':
    main()