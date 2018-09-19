#!/bin/env python
import matplotlib.pyplot as plt
import numpy as np


def main():
    x = np.arange(0, 3.14 / 2, 0.001)
    y = np.tan(x)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    plt.show()


if __name__ == "__main__":
    main()