Booth-algorithm
===============

An implementation of Booth's multiplication algorithm (and some other algorithms) in Python.

### Purpose
This repository is for understanding multiplication/division algorithm executed in digital computers.

`bitwise.py`, a file in this repo, has some implementations for bitwise calculation (e.g. two's complement, bit shift) in Python. I open this repo to the public and I encourage you to use these codes for any purpose including educational purpose.

I think these codes have serious bugs/ugly syntaxes. Please be aware of that.

### Usage
- Booth's multiplication

Run `booth.py`.

- Booth recoding multiplication

Run `booth_recoding.py`.

- (Non-)restoring division

Run `division.py`.

### Example
If you want to multiply 3 by -3 (0011 * 1101 in binary) with Booth's algorithm:

    $ python main.py
    This program excecutes Booth's multiplication algorithm.

    Input the bit length of first variable m: 4
    Input the bit length of second variable r: 4
    Input the number of first variable m: 3
    Input the number of second variable r: -3
    Internal variables:
    A = 001100000
    S = 110100000
    P = 000011010

    Step 1:
        The last 2 bits of p are: 10
        P = (P+S) >> 1
        P = 111011101

    Step 2:
        The last 2 bits of p are: 01
        P = (P+A) >> 1
        P = 000011110

    Step 3:
        The last 2 bits of p are: 10
        P = (P+S) >> 1
        P = 111011111

    Step 4:
        The last 2 bits of p are: 11
        P = P >> 1
        P = 111101111

    The answer is: 11110111
