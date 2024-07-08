import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python day00_ex01.py 'text'")
        sys.exit(1)
    print(''.join(word[0] for word in sys.argv[1].split()))


if __name__ == "__main__":
    main()
