import matplotlib.pyplot as plt
import numpy as np

def plot_parabola(a, b, c):
    # Generate x values
    x = np.linspace(-10, 10, 400)

    # Calculate y values based on the parabola equation
    y = a * x**2 + b * x + c

    # Plotting
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, label=f'y = {a}x² + {b}x + {c}')
    plt.title('Parabola Graph')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(color='gray', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.show()

# Interactive input
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

plot_parabola(a, b, c)
