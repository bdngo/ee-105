import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import scipy.signal as sig


I_1 = 1
Q_1 = 1
V_1 = 1
R = 1
C = 1
EPSILON = 1e-2
def main() -> None:
    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "lualatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
    })

    t_0 = 2
    vals = np.linspace(0, 10, num=500)
    V_1_c = V_1
    I_1_c = I_1 * R * (1 - np.exp(-vals / (R * C))) * np.heaviside(vals, 1)
    Q_1_c = -Q_1 / C * np.exp(-(vals - t_0) / (R * C)) * np.heaviside(vals - t_0, 1)
    V_c = I_1_c + Q_1_c + V_1_c
    plt.ylabel("$V_c(t)$ [V]")
    plt.xlabel("$t$ [s]")
    plt.plot(vals, V_c)
    # plt.show()
    plt.savefig(os.path.join(os.getcwd(), "hw02", "q3.pgf"))

if __name__ == "__main__":
    main()
