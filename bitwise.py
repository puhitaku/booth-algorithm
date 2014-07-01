def BitAdd(m, n, length):
    """Return m+n in string.
    
    Arguments:
    m -- Binary number in string
    n -- Same as above
    length -- The length of returned number (overflowed bit will be ignored)

    Returns: string
    """

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
    If shift is negative, it shifts the bits leftward.

    Arguments:
    n -- Binary number in string
    shift -- Number of times to shift

    Returns: string
    """

    if shift > 0:       #Right shift
        if n[0] == "0":
            n_ = "".join(["0"] * shift) + n
        else:
            n_ = "".join(["1"] * shift) + n
        return n_[:len(n)]
    else:
        n_ = n + "".join(["0"] * (-shift))
        return n_[-len(n):]


def CalcBoothRecoding(n):
    """Calculate the Booth recoding number of given n.

    Arguments:
    n -- Binary number to calculate in string

    Returns: string

    Attention:
    "2" in returned string represents "1-hat".
    """

    n_ = [int(x) for x in list(n + "0")]
    r = []
    for i in range(len(n)):
        x = n_[i+1] - n_[i]
        if x == -1: r.append(2)
        else:       r.append(x)
    return "".join([str(x) for x in r])


def GenZeroStr(n):
    """Generate a bunch of zeroes.

    Arguments:
    n -- Number of zeroes

    Returns: string
    """

    return "".join(["0"] * n)

def BoothRecToString(s, indent=0):
    """Convert a Booth recoding number to human-readable string.

    Arguments:
    s -- String of Booth recoding
    indent -- Number of spaces in the head of lines (optional)

    Returns: string
    """

    sp = " " * indent
    h = []
    n = []
    for i in list(s):
        if   i == "0":
            h.append(" ")
            n.append("0")
        elif i == "1":
            h.append(" ")
            n.append("1")
        elif i == "2":
            h.append("^")
            n.append("1")
    return sp + "".join(h) + "\n" + sp + "".join(n)

