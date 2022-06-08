def main(x):
    result = 0

    A = x & 0b111111111
    B = (x >> 9) & 0b111111111
    C = (x >> 18) & 0b11
    D = (x >> 20) & 0b111
    E = (x >> 23) & 0b11111
    F = (x >> 28) & 0b1111
    result = 0
    result |= B << 23
    result |= F << 19
    result |= A << 10
    result |= C << 8
    result |= D << 5
    result |= E << 0

    return result


print(main(0xa26ab26a))  # 0xc8a5fc3b
print(main(0xa416b67f))
