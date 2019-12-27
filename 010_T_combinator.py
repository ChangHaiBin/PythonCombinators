
def T(x,f):
    return f(x)

T = lambda x: lambda f: f(x)

##############
def f(x):
    return x + 1

print(T(100)(f))
print(T(200)(f))
print(T(300)(f))
print("############")

def g(x):
    return x * 3

print(T(100)(g))
print(T(200)(g))
print(T(300)(g))
print("############")
print("############")
print("############")

##########################################

S = lambda x: lambda y: lambda z: x(z)(y(z))
K = lambda x: lambda y: x
I = lambda x: x

T2 = S(K(S(S(K)(K))))(K)

print("SKI version:")
print(T2(100)(f))
print(T2(200)(f))
print(T2(300)(f))
print("############")

def g(x):
    return x * 3

print(T2(100)(g))
print(T2(200)(g))
print(T2(300)(g))
print("############")
