import sys


def main():
    filename = sys.argv[1]
    file = open(filename, 'r')
    content = file.read()
    print(content)
    file.close()

if __name__ == '__main__':
    main()
