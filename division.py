from bitwise import *

def split(l, c=0):
    """Split the given list in two."""
    return (l[: int(len(l)/2)], l[int(len(l)/2) : None if c == 0 else c])

def main():
    print("This program excecutes (Non-)restoring division algorithm.\n")
    print("The formula it's going to calculate is:  X / Y = ?")
    print("Choose which algorithm (R)estoring or (N)on-restoring [r/n]: ", end="")
    while True:
        inp = str(input())[0]
        if   inp in ["n", "N"]:
            algorithm = "n"
            break
        elif inp in ["r", "R"]:
            algorithm = "r"
            break
        else:
            print("Input R or N. ", end="")
    algorithm = inp

    print("Input the bit length of SECOND variable Y: ", end="")
    ylen = int(input())
    xlen = ylen * 2
    print("(The bit length of X is: len(Y)*2 = %d)" % xlen)

    print("Input the number of first variable X: ", end="")
    x = int(input())
    if x < 0:
        x = TwoComp( ("{0:0%db}" % xlen).format(x) )    #Calculate the two's complement number of x
    else:
        x = ("{0:0%db}" % xlen).format(x)   #Convert to bits and assign directly

    print("Input the number of second variable Y: ", end="")
    y = int(input())
    if y < 0:
        y = TwoComp( ("{0:0%db}" % ylen).format(y) )
    else:
        y = ("{0:0%db}" % ylen).format(y)

    n = ylen
    c = ""

    #----- Prepare internal variables -----#

    print("Internal variables:")
    print("X = %s %s" % (x[:ylen], x[ylen:]))
    print("Y =", y)
    print("n =", n)
    print("")

    #----- Algorithm start -----#

    print("#Algorithm start: %s\n" % ("Restoring" if algorithm == "r" else "Non-restoring"))
    if not "1" in y:
        print("Y is zero. Aborting.")
        return

    print("X1 = X1 - Y\t\t", end="")
    x = BitAdd(x, TwoComp(y) + GenZeroStr(ylen), xlen)
    print("X = %s %s" % split(x))

    if x[0] == "0":
        print("X1 is positive or zero. Aborting.")
        return

    x = BitShift(x, -1)
    print("[X1][X2][C] << 1\tX = %s %sC" % split(x, -1))
    
    print("X1 = X1 + Y\t\t", end="")
    x = BitAdd(x, y + GenZeroStr(ylen), xlen)
    print("X = %s %sC" % split(x, -1))
    print("n = n - 1 = %d" % (n-1))
    n -= 1

    #--- Go into the loop --- #

    print("\n#Into the loop...\n")

    if algorithm == "r":
        pass
    elif algorithm == "n":
        for i in range(n):  # X1 != 0
            print("Step %d:" % (i+1))
            if x[0] == "0": # X1 >= 0
                c = "1"
                print("X1 >= 0 -> c = 1", end="")
                x = x[:-1] + c #[X1][X2][C] << 1
                print("\tX = %s %s" % split(x))
                x = BitShift(x, -1) #Shift bits leftward
                print("[X1][X2][C] << 1\tX = %s %sC" % split(x, -1))
                x = BitAdd(x, TwoComp(y) + GenZeroStr(ylen), xlen)    #X1 = X1 - Y
                print("X1 = X1 - Y\t\tX = %s %sC" % split(x, -1))
            else:
                c = "0"
                print("X1 < 0 -> c = 0", end="")
                x = x[:-1] + c
                print("\t\tX = %s %s" % split(x))
                x = BitShift(x, -1)
                print("[X1][X2][C] << 1\tX = %s %sC" % split(x, -1))
                x = BitAdd(x, y + GenZeroStr(ylen), xlen)    #X1 = X1 + Y
                print("X1 = X1 + Y\t\tX = %s %sC" % split(x, -1))

            print("")

        if x[0] == "0": # X1 >= 0
            print("X1 >= 0 -> C = 1")
            c = "1"
            x = x[:-1] + c
        else:
            print("X1 < 0 -> C = 0")
            c = "0"
            x = x[:-1] + c
            x = BitAdd(x, y + GenZeroStr(ylen), xlen)
            print("X1 = X1 + Y")
        print("X = %s %s" % split(x))

    print("")
    print("The answer is: R = %s, Q = %s" % split(x))


if __name__ == "__main__":
    main()