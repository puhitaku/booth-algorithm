def BitAdd(m, n, length):
    """Return m+n in string.
    
    Arguments:
    m -- Binary number in string
    n -- Same as above
    length -- The length of returned number (overflowed bit will be ignored)

    Returns: string
    """

    lmin = min(len(m), len(n))
    lmax = max(len(m), len(n))
    c = 0
    ml = [0] * (lmax - len(m)) + [int(x) for x in list(m)]
    nl = [0] * (lmax - len(n)) + [int(x) for x in list(n)]
    rl = []
    for i in range(1, lmax+1):
        if ml[-i] + nl[-i] + c == 0:
            rl.insert(0, 0)
            c = 0
        elif ml[-i] + nl[-i] + c == 1:
            rl.insert(0, 1)
            c = 0
        elif ml[-i] + nl[-i] + c == 2:
            rl.insert(0, 0)
            c = 1
        elif ml[-i] + nl[-i] + c == 3:
            rl.insert(0, 1)
            c = 1
    if c == 1:
        rl.insert(0, 1)
    if length > len(rl):
        rl = [0] * (length - len(rl)) + rl
    else:
        rl = rl[-length:]
    rl = "".join([str(x) for x in rl])
    return rl


def TwoComp(n):
    """Return the two's complement of given number.

    Arguments:
    n -- Binary number in string

    Returns: string
    """

    l = list(n)
    for i in range(len(l)):
        l[i] = "0" if l[i] == "1" else "1"
    return BitAdd("".join(l), "1", len(l))


def BitShift(n, shift):
    """Shift the bits rightward in arithmetical method.

    Arguments:
    n -- Binary number in string
    shift -- Number of times to shift

    Returns: string
    """

    if n[0] == "0":
        n_ = "".join(["0"] * shift) + n
    else:
        n_ = "".join(["1"] * shift) + n
    return n_[:len(n)]


def GenZeroStr(n):
    """Generate a bunch of zeroes.

    Arguments:
    n -- Number of zeroes

    Returns: string
    """

    return "".join(["0"] * n)


def main():
    print("This program excecutes Booth's multiplication algorithm.\n")
    print("Input the bit length of first variable m: ", end="")
    mlen = int(input())
    print("Input the bit length of second variable r: ", end="")
    rlen = int(input())

    print("Input the number of first variable m: ", end="")
    m = int(input())
    if m < 0:
        m = TwoComp( ("{0:0%db}" % mlen).format(m) )
    else:
        m = ("{0:0%db}" % mlen).format(m)

    print("Input the number of second variable r: ", end="")
    r = int(input())
    if r < 0:
        r = TwoComp( ("{0:0%db}" % rlen).format(r) )
    else:
        r = ("{0:0%db}" % rlen).format(r)

    ilen = mlen + rlen + 1
    a = m + GenZeroStr(rlen + 1)
    s = TwoComp(m) + GenZeroStr(rlen + 1)
    p = GenZeroStr(mlen) + r + "0"

    print("Internal variables:")
    print("A = %s" % a)
    print("S = %s" % s)
    print("P = %s\n" % p)

    for i in range(rlen):
        print("Step %d:" % (i+1))

        op = p[-2:]
        print("    " + "The last 2 bits of p are: %s" % "".join(op))
        if   op == "10":
            print("    " + "P = (P+S) >> 1")
            p = BitAdd(p, s, len(p))
        elif op == "01":
            print("    " + "P = (P+A) >> 1")
            p = BitAdd(p, a, len(p))
        elif op == "00":
            print("    " + "P = P >> 1")
        elif op == "11":
            print("    " + "P = P >> 1")

        p = BitShift(p, 1)
        print("    " + "P = %s\n" % p)

    p = p[:-1]
    print("The answer is: %s" % p)


if __name__ == "__main__":
    main()
