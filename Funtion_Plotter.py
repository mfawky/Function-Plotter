import sys
from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)
import matplotlib.pyplot as plt
import numpy as np

class FunctionPlot(QWidget):
    def __init__(obj):
        super().__init__()
        obj.setWindowTitle("Function Plotter")

        # Creates the GUI and creates labels and input fields
        obj.func_label = QLabel("Enter any function of x:", obj)
        obj.func_input = QLineEdit(obj)
        obj.min_label = QLabel("Choose the minimum value of x:", obj)
        obj.min_input = QLineEdit(obj)
        obj.max_label = QLabel("Choose the maximum value of x:", obj)
        obj.max_input = QLineEdit(obj)

        # Creates the button to plot function
        obj.plot_button = QPushButton("Plot Function", obj)
        obj.plot_button.clicked.connect(obj.plot_function)

        # adjusts the size of the input
        obj.setFixedSize(300, 300)

        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(obj.func_label)
        layout.addWidget(obj.func_input)
        layout.addWidget(obj.min_label)
        layout.addWidget(obj.min_input)
        layout.addWidget(obj.max_label)
        layout.addWidget(obj.max_input)
        layout.addWidget(obj.plot_button)

        # Set the layout
        obj.setLayout(layout)

    def plot_function(obj):
        # Get function and x range from user input
        
        func_str = obj.func_input.text()
        x_min_str = obj.min_input.text()
        x_max_str = obj.max_input.text()

        # Validate user input
        try:
            # Convert x range to floats
            x_min = float(x_min_str)
            x_max = float(x_max_str)

            # Generates x values for the function plot
            x_vals = np.linspace(x_min, x_max, 1000)

            # Evaluates the function at each x value
            y_vals = eval(func_str, {"x": x_vals})

            # Creates the plot
            plt.plot(x_vals, y_vals)
            plt.xlabel("x")
            plt.ylabel("y")
            plt.title("Function Plot: " + func_str)

            # Show the plot on GUI
            plt.show()

        except Exception as e:
            # Display an error message if the user input is invalid
            error_msg = "Wrong input"
            error_label = QLabel(error_msg, obj)
            error_label.show()

        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    plotter = FunctionPlot()
    plotter.show()
    sys.exit(app.exec_())
