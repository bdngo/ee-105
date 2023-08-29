import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal


R = 10
L = 1e-6
C = 1e-9
R_L = 1e+3
OUT_PATH = os.path.join(os.getcwd(), "hw03")

def q_1() -> None:
    w = 2 * np.pi * np.logspace(5, 10)

    num = [R_L / L, 0]
    dem = [1, (R_L + R) / L, 1 / (L * C)]
    H_s_no_K = signal.TransferFunction(num, dem)
    _, mag, _ = signal.bode(H_s_no_K, w=w)

    plt.xlabel("$\\omega$ [Hz]")
    plt.ylabel("$|H(s)|$ [dB]")
    plt.semilogx(w, mag)
    plt.savefig(os.path.join(OUT_PATH, "q1.pgf"))
    plt.close()

def q_2():
    w_mag = [1, 1e+2, 5e+3, 1e+4, 1e+5]
    mag = [0, 0, -30, -60, -80]

    w_phase = [
        1,
        10,
        5e+2,
        1e+3,
        5e+3,
        1e+4,
        5e+4,
        1e+5,
        1e+6
    ]
    phase = [
        0,
        0,
        -45,
        -90 - 45/2,
        -90 - 45 + 45/2,
        -90 - 45 * 3/2 + 45,
        -90 - 90 + 45 * 3/2,
        -90 - 90 + 90,
        -90
    ]
    _, (ax1, ax2) = plt.subplots(nrows=2)


    color = 'tab:blue'
    ax1.set_ylabel("$|H(s)|$ [dB]")
    ax1.semilogx(w_mag, mag, color=color)
    ax1.text(1e+3, -10, "-20 dB/dec")
    ax1.text(1e+4, -45, "-40 dB/dec")
    ax1.text(2e+4, -65, "-20 dB/dec")
    ax1.tick_params(axis='y', labelcolor=color)

    color = 'tab:red'
    ax2.set_xlabel("$\\omega$ [rad/s]")
    ax2.set_ylabel("$\\angle H(s)$ [deg]")
    ax2.semilogx(w_phase, phase, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.savefig(os.path.join(OUT_PATH, "q2.pgf"))

def main() -> None:
    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "lualatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
    })
    q_1()
    q_2()

if __name__ == "__main__":
    main()
