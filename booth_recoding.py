import math

from uint import Uint, Int


def main():
    print("This program excecutes Booth recoding algorithm which calculates M * R = ??\n")
    print("Input the number of M: ", end="")
    m = int(input())

    print("Input the number of R: ", end="")
    r = int(input())

    mlen, rlen = math.ceil(math.log2(m)) * 2, math.ceil(math.log2(r)) * 2
    m, r = Int(m, mlen + rlen), Uint(r, rlen)

    b = []
    rs = r << 1
    for x, y in zip(rs.literal.bin[2:], r.literal.bin[2:]):
        x, y = int(x), int(y)
        if x-y == -1:
            b.append(2)
        else:
            b.append(x-y)

    bl1 = ''.join("  ^"[n] for n in b)
    bl2 = ''.join("011"[n] for n in b)

    print("Internal variables:")
    print(f"M = {m}")
    print(f"R = {r}")
    print(f"Recoding = {bl1}")
    print(f"           {bl2}\n")

    b.reverse()
    acc = Uint(0, mlen + rlen)

    for i in range(rlen):
        y = 0
        if b[i] == 0:
            pass
        elif b[i] == 1:
            y = m << i
            y = y.native
        elif b[i] == 2:
            y = -m << i
            y = y.native
        acc += y

        f = '{:0%db}' % (mlen + rlen)
        f = f.format(y)
        if i != 0:
            f = f[:-i]

        if i < rlen - 1:
            print("  " + f)
        else:
            print("+)" + f)
    else:
        print("  " + "-" * acc.bits)
        print("  " + acc.literal.bin[2:])
        print("")

    print(f"The answer is: {acc.literal.bin}")


if __name__ == "__main__":
    main()
