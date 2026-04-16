import sys
from texts import message, bye

def main():
    if len(sys.argv) >= 2 and sys.argv[1] == "b":
        print(bye(), ":(")
    else:
        print(message())

if __name__ == "__main__":
    main()

