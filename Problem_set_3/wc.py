import sys


def main():
    filename = sys.argv[2]
    file = open(filename, 'r')
    if sys.argv[1] == "lines":
        contents = file.read().split("\n")
        file.close()
        print(contents)
        print(len(contents))
    elif sys.argv[1] == "words":
        contents = file.read().split()
        file.close()
        print(contents)
        print(len(contents))
    elif sys.argv[1] == "chars":
        contents = file.read()
        file.close()
        count = 0
        for char in contents:
            count += 1
        print(count)
    else:
        print("Incorrect argument!")

if __name__ == '__main__':
    main()
