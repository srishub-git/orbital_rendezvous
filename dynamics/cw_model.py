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
    

