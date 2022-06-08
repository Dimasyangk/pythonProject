def main(x):
    A = x & 0b11111111111111
    B = (x >> 14) & 0b111111111111111
    C = (x >> 29) & 0b111
    result = 0
    result |= A << 18
    result |= C << 15
    result |= B << 0
    return result


print(hex(main(0x74d507c1)))
print(hex(main(0x1159da55)))
print(hex(main(0x08fb9f98)))
print(hex(main(0xc098dda3)))
print(hex(main(0xd389c1a6)))