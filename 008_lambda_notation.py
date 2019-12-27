

# def f(x,y,z):
#     return x + y + z

f = lambda x: lambda y: lambda z: x + y + z

result1 = f(1)(2)(3)
print(result1)

result2 = f(1)(2)
print(result2)

result3 = f(1)
print(result3)

print("###############")


def f(x):
    def inner_1(y):
        def inner_2(z):
            return x + y + z
        return inner_2
    return inner_1

result4 = f(1)(2)(3)
print(result4)

result5 = f(1)(2)
print(result5)

result6 = f(1)
print(result6)

