from dynamics.cw_model import orbital_mean_motion
from simulation.propagator import propagate

import numpy as np
import matplotlib.pyplot as plt

altitude_km = 400
n = orbital_mean_motion(altitude_km)

x0 = np.array([

    -1000, 0, -200,
    0.5, 0, 0.1

])

dt = 10             # 10 second timesteps
n_steps = 360       # 1 hour simulation


traj = propagate(x0, dt, n_steps,n)

fig, axes = plt.subplots(1, 2, figsize=(12, 5))
fig.suptitle("CW Free Drift - 1 hour (no thrust)", fontsize=13)

ax1 = axes[0]
ax1.plot(traj[:, 0], traj[:, 2], 'steelblue', lw=1.5)
ax1.plot(traj[0, 0], traj[0, 2], 'go', ms=8, label='start')
ax1.plot(0, 0, 'r*', ms=14, label='target')
ax1.set_xlabel('Along-track x (m)')
ax1.set_ylabel('Radial z (m)')
ax1.set_title('x-z plane')
ax1.legend()
ax1.grid(True, alpha=0.3)

dist = np.linalg.norm(traj[:, :3], axis = 1)
time_min = np.arange(n_steps + 1) * dt / 60

ax2 = axes[1]
ax2.plot(time_min, dist, 'darkorange', lw=1.5)
ax2.set_xlabel('Time (min)')
ax2.set_ylabel('Distance from target (m)')
ax2.set_title('Range over time')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('outputs/day1_free_drift.png', dpi=150)
plt.show()