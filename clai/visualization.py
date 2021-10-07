from __future__ import annotations
from typing import TYPE_CHECKING, Union

import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

from .automata import CellularAutomaton1D, CellularAutomaton2D

if TYPE_CHECKING:
    from matplotlib.colors import Colormap


def plot(
        automaton: CellularAutomaton1D,
        offset: int = 0,
        colormap: Union[str, Colormap] = 'Greys',
        save: bool = False,
        filename: str = 'automaton',
        dpi: int = 100
):
    cmap = plt.get_cmap(colormap)
    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    plt.imshow(automaton.generations[offset:], interpolation='none', cmap=cmap)
    if save:
        plt.savefig(filename, dpi=dpi)
    else:
        plt.show()


def animate(
        automaton: CellularAutomaton1D,
        colormap: Union[str, Colormap] = 'Greys',
        interval: int = 50,
        save: bool = False,
        filename: str = 'automaton.gif',
        dpi: int = 100
):
    fig, ax = plt.subplots(frameon=False)
    ax.axis('off')
    colormap = plt.get_cmap(colormap)

    grid = np.zeros((len(automaton.generations), automaton.width))

    def _animate(frame: int):
        grid[frame] = np.array(automaton.generations[frame])
        img = ax.imshow(grid, interpolation='none', cmap=colormap)
        return img,

    anim = animation.FuncAnimation(fig, _animate, frames=len(automaton.generations), interval=interval, blit=True)
    if save:
        anim.save(filename, writer='ffmpeg', dpi=dpi)
    else:
        plt.show()


def plot2d(
        automaton: CellularAutomaton2D,
        colormap: Union[str, Colormap] = 'Greys',
        save: bool = False,
        filename: str = 'automaton',
        dpi: int = 100
):
    fig = plt.figure(frameon=False)
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    plt.imshow(automaton.generations[-1], interpolation='none', cmap=plt.get_cmap(colormap))
    if save:
        plt.savefig(filename, dpi=dpi)
    else:
        plt.show()


def animate2d(
        automaton: CellularAutomaton2D,
        colormap: Union[str, Colormap] = 'Greys',
        interval: int = 50,
        save: bool = False,
        filename: str = 'automaton.gif',
        dpi: int = 100
):
    fig, ax = plt.subplots(frameon=False)
    ax.axis('off')
    colormap = plt.get_cmap(colormap)

    def _animate(frame: int):
        img = ax.imshow(automaton.generations[frame], interpolation='none', cmap=colormap)
        return img,

    anim = animation.FuncAnimation(fig, _animate, frames=len(automaton.generations), interval=interval, blit=True)
    if save:
        anim.save(filename, writer='ffmpeg', dpi=dpi)
    else:
        plt.show()
