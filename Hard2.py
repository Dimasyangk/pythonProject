import math


def main(y):
    if y < 142:
        return pow(y, 6)
    elif 142 <= y < 212:
        return 52 * pow(y, 2)
    elif 212 <= y < 292:
        return y/88 - 96 * pow(93 * pow(y, 3), 3) - 60 * pow(y, 5)
    elif y >= 292:
        return 14 * pow(y, 4) + pow(y, 3)


if __name__ == "__main__":
    print(main(337),
          main(239),
          main(251),
          main(147),
          main(278))
