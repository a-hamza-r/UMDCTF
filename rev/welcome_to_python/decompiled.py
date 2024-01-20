# Source Generated with Decompyle++
# File: chal.pyc (Python 3.10)

from math import sqrt, sin, cos
from ctypes import c_uint32, c_float
from sys import exit as exit_
source = [
    672662614,
    741343303,
    495239261,
    744259788,
    722021046,
    0xA70AA247L,
    1053692,
    0xA8050035L,
    0xA982A820L,
    624689,
    0xA90D20BCL,
    41134,
    295340,
    0xA0028102L,
    622681,
    576469,
    671170814,
    0x8041086EL,
    765,
    680595550,
    0x80200166L,
    698368102,
    2437137,
    0x8042C1EEL,
    570966112,
    4612341,
    0x800008D4L,
    0xA94D02CEL,
    16484,
    2103301,
    136226,
    9438506,
    663820758,
    0x8013523BL,
    8405532,
    0xA4000875L,
    0x80030A78L,
    136768]
seed = 64

def wandom(x):
    return x * x * cos(x) * sin(x) / 1000


def evil_bit_hack(y):
    return int(c_uint32.from_buffer(c_float(y)).value)

print('==========================================')
print('Professional flag checker service (v 97.2)')
print('==========================================')
flag = input('Show me the flag: ')
lf = len(flag)
ls = len(source)
l = lf if lf < ls else ls
for i in range(seed, seed + l):
    w = wandom(i)
    c = ~(~ord(flag[i - seed]) ^ evil_bit_hack(wandom(wandom(w))) & evil_bit_hack(w)) + 1
    if source[i - seed] != c:
        print("Uh oh! We don't think your flag is correct... :(")
        exit_(1)
if lf == ls:
    print('Your flag is correct!')
    return None
None('Some of your flag is correct...')
