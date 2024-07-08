import sys


def read_lines():
    lines = []
    line: str = sys.stdin.readline()
    while line:
        lines.append(line.strip())
        line: str = sys.stdin.readline()
        if not line:
            break
    return [char for char in ''.join(lines) if not char.isspace()]


def tantalizer(lines: []):
    correct = [0, 4, 5, 6, 8, 9, 10, 12, 14]
    incorrect = [1, 2, 3, 7, 11, 13]
    if correct == [i for i in range(15) if lines[i] == '*'] and incorrect == [i for i in range(15) if lines[i] != '*']:
        print('True')
    else:
        print('False')


def main():
    tantalizer(read_lines())


if __name__ == '__main__':
    main()
