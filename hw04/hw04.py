import os

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


OUT_PATH = os.path.join(os.getcwd(), "hw04")

def q_4() -> None:
    t = np.linspace(-3, 3, num=10_000)
    # x = np.piecewise(t,
    #     [(0 <= t) & (t <= 1), (1 < t) & (t <= 2)],
    #     [lambda t: t + 1, lambda t: 2 - t, 0]
    # )

    x_a = np.piecewise(t,
        [(-2 <= t) & (t <= -1), (-1 < t) & (t <= 0)],
        [lambda t: t + 3, lambda t: -t, 0]
    )
    x_b = np.piecewise(t,
        [(-1 <= t) & (t <= 0), (0 < t) & (t <= 1)],
        [lambda t: t + 2, lambda t: 1 - t, 0]
    )

    # resp = np.roll(x, -2) + 2 * np.roll(x, -1)
    resp = x_a + 2 * x_b

    plt.xlabel("$t$")
    plt.ylabel("$x(t) \\ast h(t)")
    plt.plot(t, resp)
    plt.savefig(os.path.join(OUT_PATH, "q4.pgf"))

def main() -> None:
    matplotlib.use("pgf")
    matplotlib.rcParams.update({
        "pgf.texsystem": "lualatex",
        'font.family': 'serif',
        'text.usetex': True,
        'pgf.rcfonts': False,
    })
    q_4()

if __name__ == "__main__":
    main()
