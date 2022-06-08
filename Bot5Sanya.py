import math


def main(z, x, y):
    sum = 0.0
    n = len(z)
    for i in range(1, n + 1):
        difficult1 = pow(z[math.ceil(i/3)-1], 2) / 5
        difficult2 = y[(n-i)]**3
        difficult3 = x[n-math.ceil(i/4)]
        substraction_result = difficult1 - difficult2 - 82 * difficult3
        sum += math.ceil(substraction_result)

    return sum * 37


print(main([-0.15, 0.57, -0.16, -0.26, 0.52, 0.21, 0.21], [0.14, 0.32, 0.5, -0.54, -0.2, -0.38, 0.05], [0.15, 0.05, -0.65, -0.85, 0.88, 0.57, -0.65]))
print(main([0.38, -0.45, -0.5, 0.15, 0.32, 0.73, 0.73], [0.3, 0.58, 0.04, 0.05, -0.56, 0.78, 0.91], [-0.5, -0.6, -0.11, 0.47, -0.59, -0.88, -0.1]))
