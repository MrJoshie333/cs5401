# Starter code (run this first)
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.interpolate
import scipy.signal
from PIL import Image

def load_image(filepath):
    """Loads an image into a numpy array.
    Note: image will have 3 color channels [r, g, b]."""
    img = Image.open(filepath)
    return (np.asarray(img).astype(float)/255)[:, :, :3]


def p1_1():
    image = load_image("Homework 1 image.png")[:, :, 0]
    example_filter = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    filtered_image = scipy.signal.convolve2d(
        image, example_filter, mode='same')

    fig = plt.figure(figsize=(3, 3), dpi=300)
    plt.imshow(filtered_image, cmap='gray')
    plt.show()

def p1_1_1():
    # Starter code + plotting helper function
    image = load_image("Homework 1 image.png")[::4, ::4,
            0]


    def plot_before_after(image, filt, title):
        cmap = 'PiYG'
        plt.figure(figsize=(12, 4))
        plt.subplot(1, 3, 1)
        plt.imshow(image, cmap=cmap)
        plt.title("Image")
        plt.subplot(1, 3, 2)
        plt.imshow(filt, vmin=-0.4, vmax=0.4, cmap=cmap)
        plt.title("Filter")
        plt.subplot(1, 3, 3)
        plt.imshow(scipy.signal.convolve(
            image, filt, mode='same'), cmap=cmap)
        plt.colorbar()
        plt.title(title)

        plt.show()

    fa = [
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9],
        [1/9, 1/9, 1/9]
    ]
    fb = [
        [0, 0, 0],
        [1 / 3, 1 / 3, 1 / 3],
        [0, 0, 0]
    ]
    fc = [
        [-1/6, 0, 1/6],
        [-1/6, 0, 1/6],
        [-1/6, 0, 1/6]
    ]
    fd = [
        [1/3, 0, 0],
        [0, 1/3, 0],
        [0, 0, 1/3]
    ]

    # Plotting Code

    if fa is None or fb is None or fc is None or fd is None:
        raise NotImplementedError()

    plot_before_after(image, fa, 'fa')
    plot_before_after(image, fb, 'fb')
    plot_before_after(image, fc, 'fc')
    plot_before_after(image, fd, 'fd')



#Function to run:
# p1_1()
# p1_1_1()
