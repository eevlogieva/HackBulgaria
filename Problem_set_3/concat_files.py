import sys


def main():
    file_to_write_in = "MEGATRON.txt"
    for arg in sys.argv[1:]:
        filename = arg
        file = open(filename, "r")
        content = file.read()
        file.close()
        file = open(file_to_write_in, "a")
        file.write(content + "\n")
        file.close()
        content = ''
        print(1)

if __name__ == '__main__':
    main()
