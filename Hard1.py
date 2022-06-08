import math


def int_r(num):
    num = int(num + (0.5 if num > 0 else -0.5))
    return num


def main(y, z):
    step1 = 38 * pow(math.ceil(y), 4)
    step2 = pow(33+86*z+93* pow(y, 3), 3)
    step3 = math.sqrt(step1+step2)
    step4 = 240*y + pow(z, 5)
    step5 = 59 * pow(23+pow(z, 2) + pow(y, 3), 2)
    res = step3 + (step4/step5)
    return res


if __name__ == "__main__":
    print(main(0.37, 0.44),
          main(0.42, -0.45),
          main(0.62, 0.6),
          main(0.8, 0.64),
          main(-0.12, 0.29))




