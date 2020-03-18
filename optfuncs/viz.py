"""
Helper functions for visualization
"""

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def handle_fig_and_ax(fig, subplot_pos, projection=None):

    if fig is None:
        fig = plt.figure()

    if subplot_pos is None:
        ax = plt.gca(projection=projection)
    else:
        ax = fig.add_subplot(subplot_pos, projection=projection)

    return fig, ax


def plot_surface(x, y, z, fig=None, subplot_pos=None, **surface_kwargs):

    fig, ax = handle_fig_and_ax(fig, subplot_pos, projection='3d')

    ax.plot_surface(x, y, z, **surface_kwargs)
    #ax.view_init(30, 10)
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z')


def plot_contour(x, y, z, fig=None, subplot_pos=None, **contourf_kwargs):

    fig, ax = handle_fig_and_ax(fig, subplot_pos)

    ax.set_aspect('equal')
    cnt = ax.contourf(x, y, z, **contourf_kwargs)
    fig.colorbar(cnt, ax=ax)


def plot_grad_as_vector_field(x_range, y_range, U, V, fig=None, subplot_pos=None, **quiver_kwargs):

    fig, ax = handle_fig_and_ax(fig, subplot_pos)

    ax.set_aspect('equal')
    q = ax.quiver(x_range, y_range, U, V, **quiver_kwargs)
