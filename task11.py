def fast_mul_gen(a, b):
    result = 0
    print("Result =", result)
    while a:
       if ((a%2) & 1):
            print("Result +=", b)
            result += b
            print(b, "+=", b)
            a = a >> 1
            b = b << 1
    print("Result =", result)
x = int(input())
y = int(input())
print("x =", x, "y =", y)
fast_mul_gen(x, y)