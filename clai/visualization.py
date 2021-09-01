import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from .automata import CellularAutomaton1D


def plot(automaton: CellularAutomaton1D, offset: int = 0, colormap: str = 'Greys', save: bool = False, dpi: int = 100):
    cmap = plt.get_cmap(colormap)
    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    plt.imshow(automaton.generations[offset:], interpolation='none', cmap=cmap)
    if save:
        plt.savefig('automaton', dpi=dpi)
    plt.show()


def animate(automaton: CellularAutomaton1D, colormap: str = 'Greys', interval: int = 50, save: bool = False, dpi: int = 100):
    # TODO: this is very basic and has issues (expand/optimize)
    
    fig, ax = plt.subplots()
    ax.axis('off')

    grid = np.zeros((automaton.num_generations, automaton.width))

    def _animate(frame: int):
        grid[frame] = np.array(automaton.generations[frame])
        img = ax.imshow(grid, interpolation='none', cmap=plt.get_cmap(colormap))
        return img,

    anim = animation.FuncAnimation(fig, _animate, frames=automaton.num_generations, interval=interval, blit=True)
    if save:
        anim.save('automaton.gif', writer='ffmpeg', dpi=dpi)
    plt.show()
