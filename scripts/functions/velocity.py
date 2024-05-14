import numpy as np
import matplotlib.pyplot as plt


def target_valocity(h, c):
    v = np.tanh(h - c) + np.tanh(c)
    return v


def main():
    h = np.arange(0, 10, 0.1)
    for c in range(10):
        v = target_valocity(h, c)
        plt.plot(h, v)
        plt.xlabel('Distance [m]')
        plt.ylabel('Velocity [m/s]')
        plt.xlim([0, 10])
        plt.ylim([0, 2])
        plt.savefig('../../outputs/target_velocity_' + str(c) + '.png')
        plt.clf()


if __name__ == '__main__':
    main()
