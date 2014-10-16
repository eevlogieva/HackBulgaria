import sys


def main():
    filename = sys.argv[1]
    file = open(filename, 'r')
    sum = 0
    content = file.read()
    lst = content.split(" ")
    lst.pop(0)
    for item in lst:
        sum += int(item)
    print(sum)
    file.close()

if __name__ == '__main__':
    main()
