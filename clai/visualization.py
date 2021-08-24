import matplotlib.pyplot as plt

from .automata import CellularAutomaton1D


def plot(automaton: CellularAutomaton1D, offset: int = 0, colormap: str = 'Greys', save: bool = False):
    cmap = plt.get_cmap(colormap)
    fig = plt.figure(frameon=False)
    plt.box(False)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    plt.imshow(automaton.generations[offset:], interpolation='none', cmap=cmap)
    if save:
        plt.savefig('automaton')
    plt.show()
