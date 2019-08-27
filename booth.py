import math

from uint import Uint, Int


def main():
    print("This program excecutes Booth's multiplication algorithm which calculates M * R = ??\n")
    print("Input the number of M: ", end="")
    m = int(input())

    print("Input the number of R: ", end="")
    r = int(input())

    mlen, rlen = math.ceil(math.log2(m)) * 2, math.ceil(math.log2(r)) * 2
    total = mlen + rlen + 1
    a = Uint(m, total) << (total - mlen)  # A: place M in leftmost position. Fill the left bits with 0.
    mm = -Uint(m, mlen)
    s = Uint(mm.native, total) << (total - mlen)  # S: place negative M in leftmost position.
    p = Int(r, total) << 1  # P: place R by rightmost 0.

    print("Internal variables:")
    print(f"M = {m}")
    print(f"R = {r}")
    print(f"A = {a.literal.bin}")
    print(f"S = {s.literal.bin}")
    print(f"P = {p.literal.bin}\n")

    for i in range(rlen):  # Do operation rlen times
        print(f"Step {i+1}:")

        op = p & 0b11
        print(f"\tThe last 2 bits of p are: {op:02b}")
        if op == 0b10:
            print(f"\tP = (P+S) >> 1")
            p += s
        elif op == 0b01:
            print(f"\tP = (P+A) >> 1")
            p += a
        elif op in [0b00, 0b11]:
            print(f"\tP = P >> 1")

        p >>= 1
        print(f"\tP = {p.literal.bin}\n")

    p >>= 1
    print(f"The answer is: {p.literal.bin}")


if __name__ == "__main__":
    main()
