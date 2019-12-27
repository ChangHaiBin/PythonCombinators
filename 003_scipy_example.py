from scipy import optimize

def f(x):
    return x * x - 3

solution = optimize.newton(f,5)

print(solution)
