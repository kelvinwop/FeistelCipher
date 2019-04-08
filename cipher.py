

def feistel_encode(j, i):
    """
    'long' j
    'int' i
    """
    assert isinstance(j, int)
    assert isinstance(i, int)

    i2 = j >> 32
    i3 = j
    i4 = 0
    while i4 < 16:
        i4 += 1
        i5 = i2 ^ (((i << i4) | (i >> (32 - i4))) ^ i3)
        i2 = i3
        i3 = i5
    j2 = (i3 & 4294967295) | (i2 << 32)
    return j2