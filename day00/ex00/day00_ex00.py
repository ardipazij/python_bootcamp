import sys


def read_lines(n):
    lines = []
    for _ in range(n):
        line = sys.stdin.readline()
        if not line:
            break
        lines.append(line.strip())
    return lines


def main():
    if len(sys.argv) != 2:
        print("Usage: python blocks.py <number_of_lines>")
        sys.exit(1)

    try:
        num_lines = int(sys.argv[1])
    except ValueError:
        print("Please provide a valid number for the number of lines.")
        sys.exit(1)

    lines = read_lines(num_lines)

    for line in lines:
        if len(line) == 32 and all([line[i] == '0' for i in range(5)]):
            print(line)


if __name__ == "__main__":
    main()
