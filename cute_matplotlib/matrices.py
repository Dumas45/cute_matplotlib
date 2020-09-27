import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

CUTE_BLUES_COLORMAP = LinearSegmentedColormap(
    'cute_blues_cm',
    segmentdata=dict(red=[(0.0, 1.0, 1.0), (1.0, 0.0, 0.0)],
                     green=[(0.0, 1.0, 1.0), (1.0, 0.4, 0.4)],
                     blue=[(0.0, 1.0, 1.0), (1.0, 1.0, 1.0)]))


def print_matrix(matrix, show=True):
    height, width = matrix.shape

    fig, ax = plt.subplots()

    ax.matshow(matrix, cmap=CUTE_BLUES_COLORMAP)

    for i in range(width):
        for j in range(height):
            c = matrix[j, i]
            ax.text(i, j, str(c), va='center', ha='center')

    if show:
        plt.show()
