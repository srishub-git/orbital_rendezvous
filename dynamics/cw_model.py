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

    A = np.array ([

        0, 0, 0, 1, 0, 0
        0, 0, 0, 0, 1, 0
        0, 0, 0, 0, 0, 1
        3*n**2, 0, 0, 0, 2*n, 0
        0, 0, 0, -2*n, 0, 0
        0, 0, -n**2, 0, 0, 0

    ])

    B = np.array([

        0, 0, 0
        0, 0, 0
        0, 0, 0
        1, 0, 0
        0, 1, 0
        0, 0, 1

    ])

    return A, B