#import necessary header
import numpy as np
 
#define the system of first-order ordinary differential equations
def f(x, y, u):
    dy_dx = -3 * y + u + 3 * np.cos(x)
    du_dx = y - 3 * u - 2 * np.cos(x) - 3 * np.sin(x)
    return dy_dx, du_dx
 
#perform a single step of the fourth-order Runge-Kutta method
def runge_kutta_step(x, y, u, h):
    k1y, k1u = f(x, y, u)
    k2y, k2u = f(x + h/2, y + h/2 * k1y, u + h/2 * k1u)
    k3y, k3u = f(x + h/2, y + h/2 * k2y, u + h/2 * k2u)
    k4y, k4u = f(x + h, y + h * k3y, u + h * k3u)
    
    next_y = y + h * (k1y + 2*k2y + 2*k3y + k4y) / 6
    next_u = u + h * (k1u + 2*k2u + 2*k3u + k4u) / 6
    return next_y, next_u
 
#solve the system of equations using the Runge-Kutta method
def runge_kutta_solver(y_0, u_0, x_0, x_end, h):
    n = int((x_end - x_0) / h)
    xs = np.linspace(x_0, x_end, n+1)
    y = y_0
    u = u_0
    ys = [y_0]
    us = [u_0]
    for x in xs:
        y, u = runge_kutta_step(x, y, u, h)
        ys.append(y)
        us.append(u)
    return xs, ys, us
 
#determine the initial conditions and parameters
y_0 = 6.0
u_0 = -1.0
x_0 = 0.0
x_end = 1.0
h = 0.001
 
#solve the system and obtain values at each step
x_values, y_values, u_values = runge_kutta_solver(y_0, u_0, x_0, x_end, h)
 
#print the values at the end point
final_index = len(x_values) - 1
final_x = x_values[final_index]
final_y = y_values[final_index]
final_u = u_values[final_index]
print(f"At x = {final_x:.3f}: y = {final_y:.5f}, u = {final_u:.5f}")
