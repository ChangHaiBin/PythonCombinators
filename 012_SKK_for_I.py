

S = lambda x: lambda y: lambda z: x(z)(y(z))
K = lambda x: lambda y: x
I = lambda x: x

print(I(1))
print(I(2))
print(I(3))
print("#############")

I2 = S(K)(K)

print(I2(1))
print(I2(2))
print(I2(3))
