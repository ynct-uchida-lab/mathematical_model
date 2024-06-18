import numpy as np
import matplotlib.pyplot as plt


def target_valocity(h, c):
    """車間距離による速度モデルの関数

    Args:
        h (int or float or numpy.ndarray): 車間距離
        c (int or float or numpy.ndarray): 車間距離に反応する定数

    Returns:
        float or numpy.ndarray: 車間距離に対する目標速度

    Examples:
        >>> target_valocity(5, 2)
        1.9590823337625474
        >>> target_valocity(np.array([3, 4]), 2)
        [1.72562174 1.92805516]
        >>> target_valocity(np.array([1, 2]), np.array([3, 4]))
        [0.03102717 0.03530172]

    """
    return np.tanh(h - c) + np.tanh(c)


def main():
    """

    target_valocityをテストする関数

    """

    # 車間距離0~10まで0.1刻みで増加    
    h = np.arange(0, 10, 0.1)

    # 車間距離に反応する定数を変えながらtarget_valocityをループする関数
    for c in range(10):
        # 速度の計算
        v = target_valocity(h, c)
        # 車間距離に対応する速度の描画
        plt.plot(h, v)
        plt.xlabel('Distance [m]')
        plt.ylabel('Velocity [m/s]')
        plt.xlim([0, 10])
        plt.ylim([0, 2])
        # 保存
        plt.savefig('../../outputs/target_velocity_' + str(c) + '.png')
        plt.clf()


if __name__ == '__main__':
    main()
