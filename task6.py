def twice(f):
    def g(x):
        return f(f(x))

    return g


print((lambda x: x * x)(3))
print(twice(lambda x: x * x)(5))
print(twice(twice(lambda x: x * x))(5))
