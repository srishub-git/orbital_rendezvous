"""
Clohessy-Wiltshire (CW) relative orbital dynamics.

Reference frame: LVLH (Local Vertical Local Horizontal)
    x-axis: along track (direction of travel)
    y-axis: perpendicular to the orbital plane
    z-axis: towards earth

State vector:   [x, y, z, xdot, ydot, zdot]     metres and m/s
Control vector: [ux, uy, uz]                    specific force in m/s²

"""

import numpy as np
from scipy.linalg import expm     # importing exponential matrix

def get_cw_matrices(n: float) -> tuple[np.ndarray, np.ndarray]:
    
    """
    Args:
        n: mean motion of target orbit (rad/s)

    Returns:
        A: system matrix/Dynamics matrix (6,6)
        B: input matrix (6,3)

    """

    A = np.array([
        [0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0],
        [0, 0, 0, 0, 0, 1],
        [3 * n ** 2, 0, 0, 0, 2 * n, 0],
        [0, 0, 0, -2 * n, 0, 0],
        [0, 0, -n ** 2, 0, 0, 0],
    ])

    B = np.array([
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
        [1, 0, 0],
        [0, 1, 0],
        [0, 0, 1],
    ], dtype=float)
    return A, B

def discretize_cw(n: float, dt: float) -> tuple[np.ndarray, np.ndarray]:

    """
    Args:
        n: mean motion of target orbit (rad/s)
        dt: timestep in seconds (s)

    Returns:
        Ad: discretized system matrix (6,6)
        Bd: discretized input matrix (6,3)

    """

    A, B = get_cw_matrices(n)

    n_states = A.shape[0]   #6
    n_inputs = B.shape[1]  #3

    M = np.zeros((n_states + n_inputs, n_states + n_inputs))
    M[:n_states, :n_states] = A*dt
    M[:n_states, n_states:] = B*dt

    expM = expm(M)

    Ad = expM[:n_states, :n_states]
    Bd = expM[:n_states, n_states:]

    return Ad, Bd

def orbital_mean_motion(altitude_km: float) -> float:

    """
    Args:
    altitude_km: how high the spacecraft is (km)

    Returns:
    n: mean motion of the chaser orbit (rad/s)

    """
    mu = 3.986004418e14
    R_earth = 6.371e6

    a = R_earth + (altitude_km*1000)
    n = np.sqrt(mu/a**3)

    return n