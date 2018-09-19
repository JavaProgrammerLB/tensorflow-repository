#!/bin/env python
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(0, 1000, 10)
    y = np.square(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()