
import numpy as np
from dynamics.cw_model import discretize_cw


def propagate(x0, dt, n_steps, n):

    """
    Args:
        x0: initial position
        dt: time step
        n_steps: number of steps
        n: mean motion

    Returns:
        trajectory: (n_steps+1, 6) array of states over time

    """

    Ad, Bd = discretize_cw(n, dt)

    trajectory = np.zeros((n_steps + 1, 6))
    trajectory[0] = x0

    for k in range(n_steps):

        x = trajectory[k]
        u = np.zeros(3)
        trajectory[k+1] = Ad @ x + Bd @ u

    return trajectory

