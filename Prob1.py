def main():
    elements = int(raw_input('Enter number of elements of the list = '))
    numList = []
    #input elements
    for element in range(0,elements):
        numList.append(int(raw_input('Enter element:')))
    print '1.) Sum using for loop.'
    print '2.) Sum using while loop.'
    print '3.) Sum using recursion.'
    choice = int(raw_input('Enter choice: '))
    if choice == 1:
        forLoopSum(numList)
    elif choice == 2:
        whileLoopSum(numList)
    elif choice == 3:
        print 'Sum of list using recursion' + str(recursionSum(numList))
    else:
        print 'Wrong choice.'


def forLoopSum(numList):
    sum = 0
    for num in numList:
        sum += num
    print 'Sum of list using for loop = ' + str(sum)

def whileLoopSum(numList):
    sum = 0
    while len(numList) != 0:
        sum += numList.pop()
    print 'Sum of list using while loop = ' + str(sum)

def recursionSum(numList):
    if len(numList) == 1:
        return numList[0]
    else:
        return numList[0] + recursionSum(numList[1:])

if __name__ == '__main__':
    main()