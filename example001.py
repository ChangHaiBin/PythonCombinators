

from combinator_SKI import S, K, I

def I2(x):
    return S(K)(K)(x)

print(I(1))
print(I(2))
print(I(3))
print("###############")

print(I2(1))
print(I2(2))
print(I2(3))

print("Hello World")