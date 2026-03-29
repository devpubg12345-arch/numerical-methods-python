from numpy import *
import matplotlib.pyplot as plt
def f(x):
    return x**3 - 2*x**2 + 1
def bisection(f, a, b, tol=1e-6, iter=35):
    if f(a) * f(b) >= 0:
        print("Invalid interval")
        return None
    print(f"{'Iter':<10}{'a':<12}{'b':<12}{'x':<12}{'f(x)':<12}")
    xs = []   

    for i in range(iter):
        x = (a + b) / 2
        xs.append(x)

        print(f"{i+1:<5}{a:<12.6f}{b:<12.6f}{x:<12.6f}{f(x):<12.6f}")

        if abs(f(x)) < tol:
            print(f"\nRoot found at iteration {i+1}")
            break
        if f(a) * f(x) < 0:
            b = x
        else:
            a = x

    print(f"\nStopped after {len(xs)} iterations")   
    plt.scatter(xs, f(array(xs)), marker="o")  
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.title("Bisection Method Graph")
    plt.grid()
    plt.show()
    return x


root = bisection(f, -1, 0)
print(f"Approximate solution is {root}")
