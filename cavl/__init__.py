from .automata import init, CellularAutomaton1D, CellularAutomaton2D
from .neighborhoods import moore, von_neumann
from .rules import General1DRule, Totalistic1DRule
from .visualization import plot, animate, plot2d, animate2d

__version__ = "0.4.1"
