import random 
import numpy as np 
import matplotlib.pyplot as plt 
#from . import algebra_helpers 
#from . import numbers_fractions_operators as helper


class AlgebraGraphingGenerator:
    def __init__(self, doc):
        self.doc = doc 
        doc.add_section("Graphs")

def __generate_simultaneous_linear_graph(xs, ys, titles):
    x_axis = np.arange(-20, 20)
    y_axis = np.arange(-20, 20)

    plt.figure(figsize=(10, 10))
    plt.tick_params(
            axis='both',          # changes apply to the x-axis and y-axis
            which='both',      # both major and minor ticks are 
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            left=False,
            right=False,
            labelleft=False,
            labelbottom=False) # labels along the bottom edge are off

    plt.plot(xs[0], ys[0])
    plt.plot(xs[1], ys[1])
    plt.plot(x_axis, np.zeros_like(x_axis))
    plt.plot(np.zeros_like(y_axis), y_axis)
    plt.grid()
    plt.xticks(np.arange(-20, 20))
    plt.yticks(np.arange(-20, 20))
        
    # plot origin label 
    plt.annotate("0", (-1, -1))
    
    # plot the y axis with labels 
    plt.annotate("y", (-1, 19))
    plt.annotate("5", (-1, 4.7))
    plt.annotate("10", (-1.4, 9.7))
    plt.annotate("15", (-1.4, 14.7))
    plt.annotate("-5", (-1, -5.3))
    plt.annotate("-10", (-1.5, -10.3))
    plt.annotate("-15", (-1.5, -15.3))

    # plot the x axis with labels 
    plt.annotate("x", (19, -0.8))
    plt.annotate("5", (4.8, -0.8))
    plt.annotate("10", (9.5, -0.8))
    plt.annotate("15", (14.5, -0.8))
    plt.annotate("-5", (-5.5, -0.8))
    plt.annotate("-10", (-10.7, -0.8))
    plt.annotate("-15", (-15.7, -0.8))

    # add the equation by annotation 
    eq1_pt = (xs[0][0], ys[0][0])
    eq2_pt = (xs[1][-1], ys[1][-1])
    plt.annotate(titles[0], eq1_pt)
    plt.annotate(titles[1], eq2_pt)
    plt.savefig("C:/Users/TszHeyLam/Personal/mathsgenerator/graph_sim.png")
    plt.show()

def __generate_double_linear_graphs(xs, ys, titles):
    x_axis = np.arange(-20, 20)
    y_axis = np.arange(-20, 20)

    fig, axes = plt.subplots(1, 2)
    fig.set_size_inches(20, 10)
    axes[0].set_title(titles[0])
    axes[1].set_title(titles[1])

    for fig_index in range(2):
        axes[fig_index].tick_params(
            axis='both',          # changes apply to the x-axis and y-axis
            which='both',      # both major and minor ticks are 
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            left=False,
            right=False,
            labelleft=False,
            labelbottom=False) # labels along the bottom edge are off

        axes[fig_index].plot(xs[fig_index], ys[fig_index])
        axes[fig_index].plot(x_axis, np.zeros_like(x_axis))
        axes[fig_index].plot(np.zeros_like(y_axis), y_axis)
        axes[fig_index].grid()
        axes[fig_index].set_xticks(np.arange(-20, 20))
        axes[fig_index].set_yticks(np.arange(-20, 20))
        
        # plot origin label 
        axes[fig_index].annotate("0", (-1, -1))
        
        # plot the y axis with labels 
        axes[fig_index].annotate("y", (-1, 19))
        axes[fig_index].annotate("5", (-1, 4.7))
        axes[fig_index].annotate("10", (-1.4, 9.7))
        axes[fig_index].annotate("15", (-1.4, 14.7))
        axes[fig_index].annotate("-5", (-1, -5.3))
        axes[fig_index].annotate("-10", (-1.5, -10.3))
        axes[fig_index].annotate("-15", (-1.5, -15.3))

        # plot the x axis with labels 
        axes[fig_index].annotate("x", (19, -0.8))
        axes[fig_index].annotate("5", (4.8, -0.8))
        axes[fig_index].annotate("10", (9.5, -0.8))
        axes[fig_index].annotate("15", (14.5, -0.8))
        axes[fig_index].annotate("-5", (-5.5, -0.8))
        axes[fig_index].annotate("-10", (-10.7, -0.8))
        axes[fig_index].annotate("-15", (-15.7, -0.8))
    plt.savefig("C:/Users/TszHeyLam/Personal/mathsgenerator/graph.png")
    plt.show()
    

def linear_equation(m, c):
    xs = np.arange(-10, 10)
    ys = xs * m + (np.ones_like(xs) * c)
    # bound the y_values
    low_bound_index = 0
    high_bound_index = 19
    for y_index in range(20): 
        if ys[y_index] < -20:
            low_bound_index = y_index + 1
    for y_index in range(19, 0, -1):
        if ys[y_index] > 20:
            high_bound_index = y_index 
    ys = ys[low_bound_index:high_bound_index]
    xs = xs[low_bound_index:high_bound_index]
    if m == 1:
        m_txt = ""
    elif m == -1:
        m_txt = "-"
    else:
        m_txt = f"{m}"
    if c > 0:
        title = f"y = {m_txt}x + {c}"
    else:
        title = f"y = {m_txt}x - {np.abs(c)}"
    return (title, xs, ys)
 

def main():
    title1, x1, y1 = linear_equation(-1, -5)
    title2, x2, y2 = linear_equation(2, 7)
    
    xs = [x1, x2]
    ys = [y1, y2]
    titles = [title1, title2]
    #__generate_double_linear_graphs(xs, ys, titles)
    __generate_simultaneous_linear_graph(xs, ys, titles)

if __name__ == "__main__":
    main()