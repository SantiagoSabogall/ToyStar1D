import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Parameters of the simulation
kappa = 0.1
lambda_ = 2.01  # Fixed: was using lambda (reserved keyword) later
nu = 1.0
L = 1.0
N = 200
x = np.linspace(-L, L, N)
dx = x[1] - x[0]

# Initial conditions
rho = np.ones(N)
v = np.zeros(N)
p = np.zeros(N)

# Time parameters
dt = 0.0005
t_max = 2.0  
steps = int(t_max / dt)

 # Gravity as a function of position
g = -lambda_ * x 

# Conservation equation
def compute_drho_dt(rho, v):
    flux = rho * v
    drho_dt = np.zeros_like(rho)
    
    drho_dt[0] = -(flux[1] - flux[0]) / dx  
    drho_dt[-1] = -(flux[-1] - flux[-2]) / dx  
    drho_dt[1:-1] = -(flux[2:] - flux[:-2]) / (2 * dx)  
    return drho_dt

# Motion equation
def compute_dv_dt(rho, v):
    
    drho_dx = np.zeros_like(rho)
    
    drho_dx[0] = (rho[1] - rho[0]) / dx 
    drho_dx[-1] = (rho[-1] - rho[-2]) / dx 
    drho_dx[1:-1] = (rho[2:] - rho[:-2]) / (2 * dx)  
    dv_dt = -2 * kappa * drho_dx + g - nu * v
    return dv_dt

# Initialize lists to store frames for animation
frames_rho = []
frames_v = []
frames_P = []

for step in range(steps):
    drho_dt = compute_drho_dt(rho, v)
    dv_dt = compute_dv_dt(rho, v)
    
    # Euler method for time integration
    rho += dt * drho_dt
    v += dt * dv_dt
    p = kappa * rho**2
    
    # Boundary conditions
    rho[0] = rho[-1] = 1.0  
    v[0] = v[-1] = 0.0
    
    if step % 20 == 0:
        frames_rho.append(rho.copy())
        frames_v.append(v.copy())
        frames_P.append(p.copy())

fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(8, 12))

line1, = ax1.plot(x, frames_rho[0], color='blue')
ax1.set_title(r'Density $\rho (x, t)$')
ax1.set_ylim(-1, 3.5)
ax1.grid()

line2, = ax2.plot(x, frames_v[0], color='red')
ax2.set_title(r'Velocity $v(x, t)$')
ax2.set_ylim(-5.5, 5.5) 
ax2.grid() 

line3, = ax3.plot(x, frames_P[0], color='green')
ax3.set_title(r'Pressure $P(x, t)$')
ax3.set_ylim(0, 1.5)
ax3.set_xlabel('x')
ax3.grid()

def update(frame):
    line1.set_ydata(frames_rho[frame])
    line2.set_ydata(frames_v[frame])
    line3.set_ydata(frames_P[frame])
    return line1, line2, line3

ani = FuncAnimation(fig, update, frames=len(frames_rho), interval=50, blit=True)
plt.tight_layout()
plt.show()