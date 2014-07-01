from bitwise import *

def main():
    print("This program excecutes Booth recoding algorithm.\n")
    print("The formula it's going to calculate is:  M * R = ?")
    print("Input the bit length of first variable M: ", end="")
    mlen = int(input())
    print("Input the bit length of second variable R: ", end="")
    rlen = int(input())

    print("Input the number of first variable M: ", end="")
    m = int(input())
    if m < 0:
        m = TwoComp( ("{0:0%db}" % (mlen + rlen)).format(m) )    #Calculate the two's complement number of m
    else:
        m = ("{0:0%db}" % (mlen + rlen)).format(m)   #Convert to bits and assign directly

    print("Input the number of second variable R: ", end="")
    r = int(input())
    if r < 0:
        r = TwoComp( ("{0:0%db}" % rlen).format(r) )
    else:
        r = ("{0:0%db}" % rlen).format(r)

    rs = CalcBoothRecoding(r)
    print("Internal variables:")
    print("M = %s" % m)
    print("R = %s\n" % BoothRecToString(rs, 4)[4:])

    r = list(rs)
    r.reverse()

    acc = GenZeroStr(mlen + rlen)


    for i in range(rlen):
        if   r[i] == "0":
            y = GenZeroStr(len(acc))
        elif r[i] == "1":
            y = BitShift(m, -i)
        elif r[i] == "2":
            y = BitShift(TwoComp(m), -i)
        acc = BitAdd(acc, y, len(acc))

        if i == rlen - 1:
            print("+)" + y[:len(y) - i])
        else:
            print("  " + y[:len(y) - i])
    else:
        print("  " + "-" * len(y))
        print("  " + acc)
        print("")

    print("The answer is: %s" % acc)

if __name__ == "__main__":
    main()