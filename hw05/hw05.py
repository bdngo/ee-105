#!/usr/bin/env python3

import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


OUT_PATH = os.path.join(os.getcwd(), "hw05")


def q_3() -> None:
    t = np.linspace(-1, 10, num=1000)
    # x = np.piecewise(t,
    #     [(0 <= t) & (t <= 1), (1 < t) & (t <= 2)],
    #     [lambda t: t + 1, lambda t: 2 - t, 0]
    # )
    final_val = 3

    x_a = np.piecewise(t,
                       [(0 <= t) & (t <= 4)],
                       [1, 0]
                       )
    x_b = np.piecewise(t,
                       [(0 <= t) & (t < final_val/2), (final_val/2 <= t) & (t < final_val/2 + 4), (final_val/2 + 4 <= t) & (t <= final_val + 4)],
                       [lambda x: 2*x, final_val, lambda x: final_val - 2*(x - (final_val/2 + 4)), 0]
                       ) + 0.2

    _, ax = plt.subplots()
    ax.set_xlabel("$t$ [µs]")
    ax.set_ylabel("Volts")

    color = "tab:blue"
    ax.plot(t, x_a, color=color, label="$V_i$")

    color = "tab:red"
    ax.plot(t, x_b, color=color, label="$V_o$")

    ax.axhline(final_val + 0.2, color="tab:gray", linestyle="--")
    ax.axvline(final_val/2, color="tab:gray", linestyle="--")
    ax.axvline(final_val/2 + 4, color="tab:gray", linestyle="--")
    ax.text(8, 3, f"{final_val + 0.2} V")
    ax.text(2, 2, f"{final_val/2} µs")
    ax.text(4.5, 2, f"{final_val/2 + 4} µs")

    ax.legend()
    plt.savefig(os.path.join(OUT_PATH, "q3.pgf"))


def main() -> None:
    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "lualatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
    })
    q_3()


if __name__ == "__main__":
    main()
