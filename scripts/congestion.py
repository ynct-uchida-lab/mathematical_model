import numpy as np
import functions.velocity as vel
import matplotlib.pyplot as plt
import time


def main():
    """

    渋滞をシュミレーションする関数

    """

    # 各車のスタート位置
    x = np.arange(10, 0, -2)
    num = len(x)
    # 各車の車間距離に反応する定数
    c = np.array([2] * num)
    # 各車の感応度
    a = np.array([10] * num)
    # a[2] = 25
    # 各車の初速度
    v = np.array([0] * num)
    dt = 0.05
    # 経過時間0~10まで0.1増加
    tim = np.arange(0, 20, dt)

    # 開始時刻の取得
    start = time.time()
    # 経過時間を変えながらvel.target_velocityをループする
    for t in tim:
        # 車間距離の計算
        diff = np.diff(x)
        diff = np.abs(diff)
        h = np.append(30, diff)
        # 速度の計算
        V = vel.target_valocity(h, c)
        # 3~6秒の間は先頭の車にブレーキがかかる
        if 3 <= t <= 6:
            V[0] = 0
        # 加速度の計算
        acc = a * (V - v)
        v = v + acc * dt
        # 位置を更新
        x = x + v * dt
        # 最後尾の車が20mを超えた時の経過時間
        if x[-1] > 20:
            end = time.time()
            print(end - start)
            break
        # 車の台数だけループする
        for i in range(num):
            # tに対応する車間距離の描画
            plt.plot(x[i], 0, marker='o')
        plt.xlim([0, 30])
        plt.pause(0.05)
        plt.clf()


if __name__ == '__main__':
    main()
