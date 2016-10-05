def main():
    import numpy as np
    matrix = np.matrix([[0, 1, 2],
                      [3, 4, 5],
                      [6, 7, 8]])
    print '1.) Rotate 90 left: '
    print '2.) Rotate 90 right: '
    print '3.) Rotate 180 left: '
    print '4.) Rotate 180 right: '
    choice = int(raw_input('Enter choice: '))
    print 'Orignal matrix'
    print matrix
    if choice == 1:
        print r90Left(matrix)
    elif choice == 2:
        print r90Right(matrix)
    elif choice == 3:
        print r90Left(r90Left(matrix))
    elif choice == 4:
        print r90Right(r90Right(matrix))
    else:
        print 'Wrong choice.'


def r90Left(matrix):
    print 'Matrix after rotating: '
    return matrix.transpose()[::-1]

def r90Right(matrix):
    print 'Matrix after rotating: '
    return matrix.transpose()[::1]

if __name__ == '__main__':
    main()