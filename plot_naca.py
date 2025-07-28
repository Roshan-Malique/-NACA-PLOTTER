import numpy as np
import matplotlib.pyplot as plt

def naca4_airfoil(m, p, t, c, n_points=100):
    x = np.linspace(0, c, n_points)
    yt = 5 * t * (0.2969 * np.sqrt(x/c) - 0.1260 * (x/c) - 0.3516 * (x/c)**2 + 0.2843 * (x/c)**3 - 0.1015 * (x/c)**4)
    yc = np.where(x/c < p,
                  m / (p**2) * (2*p*(x/c) - (x/c)**2),
                  m / ((1 - p)**2) * ((1 - 2*p) + 2*p*(x/c) - (x/c)**2))
    dyc_dx = np.where(x/c < p,
                     2 * m / (p**2) * (p - (x/c)),
                     2 * m / ((1 - p)**2) * (p - (x/c)))
    theta = np.arctan(dyc_dx)
    xu = x - yt * np.sin(theta)
    yu = yc + yt * np.cos(theta)
    xl = x + yt * np.sin(theta)
    yl = yc - yt * np.cos(theta)
    return np.concatenate((xu[::-1], xl[1:])), np.concatenate((yu[::-1], yl[1:]))

def get_float(prompt, min_value=None, max_value=None):
    while True:
        try:
            value = float(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Value must be at least {min_value}.")
                continue
            if max_value is not None and value > max_value:
                print(f"Value must be at most {max_value}.")
                continue
            return value
        except ValueError:
            print("Please enter a valid number.")

m = get_float("Enter maximum camber (e.g. 0.02): ", 0, 1)
p = get_float("Enter position of maximum camber (e.g. 0.4): ", 0, 1)
t = get_float("Enter thickness (e.g. 0.4): ", 0, 1)
c = get_float("Enter chord length (e.g. 1): ", 0.01)

x, y = naca4_airfoil(m, p, t, c)
plt.plot(x, y)
plt.axis('equal')
plt.title('NACA 4-Digit Airfoil Shape')
plt.grid(True)
plt.show()
plt.savefig('naca4_airfoil.png')