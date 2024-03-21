import matplotlib.pyplot as plt


# takes two functions of time and plots them on the same plot for comparison with labels differing colors
def plot_input_vs_output_xy(ax , t_space , fout , fin , title , label_in = "Input Function" ,
                            label_out = "Output Function" , color_in = "magenta" ,
                            color_out = "green" , x_label = "Time (t)" , y_label = "f(t)") :
    """
       Plot two functions of time on the same plot for comparison.

       Parameters:
       - ax: Matplotlib axis object.
       - t_space: Time values.
       - fout: Output function values.
       - fin: Input function values.
       - title: Plot title.
       - label_in: Label for the input function (default is "Input Function").
       - label_out: Label for the output function (default is "Output Function").
       - color_in: Color for the input function plot (default is "magenta").
       - color_out: Color for the output function plot (default is "green").
       - x_label: Label for the x-axis (default is "Time (t)").
       - y_label: Label for the y-axis (default is "f(t)").

       Returns:
       - ax: Matplotlib axis object.
       """

    ax.plot(t_space , fout , color_out , label_out)
    ax.plot(t_space , fin , color_in , label_in)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.title(title)
    return ax


def plot_versus_time(ax , t_space , x_space , title , y_label = "f(t)" , color = "red" , x_label = "Time (t)" ,
                     f_label = 'f(t)') :
    """
        Plot a function of time.

        Parameters:
        - ax: Matplotlib axis object.
        - t_space: Time values.
        - x_space: Function values.
        - title: Plot title.
        - y_label: Label for the y-axis (default is "f(t)").
        - color: Color for the plot (default is "red").
        - x_label: Label for the x-axis (default is "Time (t)").
        - f_label: Label for the function plot (default is 'f(t)').

        Returns:
        - ax: Matplotlib axis object.
    """

    ax.plot(t_space , x_space , color = color , label = f_label)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.legend()
    ax.set_title(title)
    ax.grid(True)

    return ax

def plot_multiple_versus_time(ax, t_space, x_spaces, title, y_labels=None, colors=None, x_label="Time (t)", f_labels=None):
    """
    Plot multiple functions of time on the same graph.

    Parameters:
    - ax: Matplotlib axis object.
    - t_space: Time values.
    - x_spaces: List of function values arrays.
    - title: Plot title.
    - y_labels: List of labels for the y-axes (defaults to ["f1(t)", "f2(t)", ..., "fn(t)"]).
    - colors: List of colors for the plots (defaults to a predefined list of colors).
    - x_label: Label for the x-axis (default is "Time (t)").
    - f_labels: List of labels for the function plots (defaults to ['f1(t)', 'f2(t)', ..., 'fn(t)']).

    Returns:
    - ax: Matplotlib axis object.
    """

    # Default color cycle for matplotlib if not specified
    default_colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']
    colors = colors if colors is not None else default_colors[:len(x_spaces)]

    # Generate default function labels if not specified
    if f_labels is None:
        f_labels = [f'f{i}(t)' for i in range(1, len(x_spaces) + 1)]

    # Generate default y labels if not specified
    if y_labels is None:
        y_labels = [f'f{i}(t)' for i in range(1, len(x_spaces) + 1)]

    # Plot each function
    for i, (x_space, color, f_label, y_label) in enumerate(zip(x_spaces, colors, f_labels, y_labels), start=1):
        ax.plot(t_space, x_space, color=color, label=f_label)
        ax.set_ylabel(y_label)

    ax.set_xlabel(x_label)
    ax.legend()
    ax.set_title(title)
    ax.grid(True)

    return ax