import sys
from random import randint


def main():
    filename = sys.argv[1]
    file = open(filename, 'w')
    for i in range(int(sys.argv[2])):
        file.write(" " + str(randint(1, 1000)))
    file.close()

if __name__ == '__main__':
    main()
