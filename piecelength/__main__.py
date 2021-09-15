import sys
from piecelength import piece_length

if __name__ == '__main__':
    args = sys.argv[1]
    sys.stdout.write(piece_length(args))
