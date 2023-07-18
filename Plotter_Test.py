import pytest
from PySide2.QtWidgets import QApplication

from Function_Plotter import FunctionPlot


@pytest.fixture(scope="session")
def app():
    # Create an instance of the QApplication for use in tests
    qapp = QApplication([])
    return qapp


def test_plot():
    # Test that the plot function creates a plot widget when given valid input
    data = [(1, 4), (2, 5), (3, 6)]
    plot_widget = FunctionPlot.plot_function(data)
    assert plot_widget is not None
    assert plot_widget.isVisible()

def test_plot_invalid_input(app):
    # Test that the plot function raises an exception when given invalid input
    with pytest.raises(ValueError):
        FunctionPlot.plot_function(app)
        
def test_plot_clear(app):
    # Test that the plot function properly clears the plot widget when called with no arguments
    plot_widget = FunctionPlot.plot_function(app)
    assert plot_widget is not None
    assert plot_widget.isVisible()
    
    FunctionPlot.plot_function(app, plot_widget)
    assert not plot_widget.isVisible()