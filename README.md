# 1D Toy Star Simulation

This repository contains a Python implementation of a simplified one-dimensional hydrodynamic model of a self-gravitating fluid — known as a "Toy Star" — based on the work of:

> J. J. Monaghan & D. J. Price (2004). *Toy stars in one dimension*.  
> Monthly Notices of the Royal Astronomical Society, 350(4), 1449–1456.  
> [DOI: 10.1111/j.1365-2966.2004.07748.x](https://doi.org/10.1111/j.1365-2966.2004.07748.x)

## 🚀 Description

This code numerically solves the fluid dynamics equations in one dimension for a compressible medium with a gravitational force modeled as a linear restoring force:

- **Continuity equation**:
  $$\frac{\partial \rho}{\partial t} + \frac{\partial (\rho v)}{\partial x} = 0$$

- **Momentum equation**:
  $$\frac{dv}{dt} = -2\kappa \frac{\partial \rho}{\partial x} - \lambda x - \nu v$$

- **Polytropic equation of state**:
  $$P = \kappa \rho^2$$

## ⚙️ Parameters

- $$\kappa = 0.1$$ — gas constant
- $$\lambda = 2.01$$ — gravitational acceleration coefficient
- $$\nu = 1.0$$— viscosity coefficient
- Domain: $$x \in [-1, 1]$$
- Time integration: Euler method

Initial conditions:
- $$\rho(x, 0) = 1$$
- $$v(x, 0) = 0$$

## 📊 Output

The simulation produces an animation of the evolution of:

- Mass density $$\rho(x, t)$$
- Velocity field $$v(x, t)$$
- Pressure $$P(x, t)$$


## 📚 References

- J. J. Monaghan & D. J. Price, *Toy stars in one dimension*, MNRAS 350, 1449–1456 (2004)




