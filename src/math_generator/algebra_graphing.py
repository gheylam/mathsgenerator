import numpy as np 
import matplotlib.pyplot as plt 

def linear_equation(m, c):
    x_axis = np.arange(-20, 20)
    y_axis = np.arange(-20, 20)
    x = np.arange(-10, 10)
    y = x * m + (np.ones_like(x) * c)
    plt.figure(figsize = (10, 10))
    plt.plot(x, y) 
    plt.plot(x_axis, np.zeros_like(x_axis))
    plt.plot(np.zeros_like(y_axis), y_axis)
    plt.xticks(np.arange(-20, 20))
    plt.yticks(np.arange(-20, 20))
    plt.grid()
    # plot the y axis with labels 
    plt.annotate("0", (-0.5, -0.5))
    plt.annotate("5", (-1, 4.7))
    plt.annotate("10", (-1.4, 9.7))
    plt.annotate("15", (-1.4, 14.7))
    plt.annotate("-5", (-1, -5.3))
    plt.annotate("-10", (-1.5, -10.3))
    plt.annotate("-15", (-1.5, -15.3))

    # plot the x axis with labels 
    plt.annotate("5", (4.8, -0.8))
    plt.annotate("10", (9.5, -0.8))
    plt.annotate("15", (14.5, -0.8))
    plt.annotate("-5", (-5.5, -0.8))
    plt.annotate("-10", (-10.7, -0.8))
    plt.annotate("-15", (-14.7, -0.8))
    plt.show()

def main():
    linear_equation(1, 0)

if __name__ == "__main__":
    main()