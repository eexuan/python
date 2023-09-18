#import necessary headers
import numpy as np
from scipy.integrate import trapz

#define the function to integrate
def f(x): 
    return ((x**4) + 1) / ((x**3) - (x**2) - 14*x + 24)

#define the integration interval [5,7] for various levels of subdivision
x1 = np.linspace(5, 7, 2) #x0, x1 -> 2 points
y1 = f(x1)
R00 = trapz(y1, x1)  

x2 = np.linspace(5, 7, 3) #x0, x1, x2 -> 3 points
y2 = f(x2)
R10 = trapz(y2, x2)
 
x3 = np.linspace(5, 7, 5) #x0, x1, ..., x4 -> 5 points
y3 = f(x3)
R20 = trapz(y3, x3)

x4 = np.linspace(5, 7, 9) #x0, x1, ..., x8 -> 9 points
y4 = f(x4)
R30 = trapz(y4, x4)

x5 = np.linspace(5, 7, 17) #x0, x1, ..., x16 -> 17 points
y5 = f(x5)
R40 = trapz(y5, x5)
 
#Richardson extrapolation for improved accuracy
R11 = R10 + (R10 - R00) / (4 ** 1 - 1)
R21 = R20 + (R20 - R10) / (4 ** 1 - 1)
R22 = R21 + (R21 - R11) / (4 ** 2 - 1)
R31 = R30 + (R30 - R20) / (4 ** 1 - 1)
R32 = R31 + (R31 - R21) / (4 ** 2 - 1)
R33 = R32 + (R32 - R22) / (4 ** 3 - 1)

#calculate R4,4 using Richardson extrapolation
R41 = R40 + (R40 - R30) / (4 ** 1 - 1)
R42 = R41 + (R41 - R31) / (4 ** 2 - 1)
R43 = R42 + (R42 - R32) / (4 ** 3 - 1)
R44 = R43 + (R43 - R33) / (4 ** 4 - 1)
 
#print the final result of R4,4
print("R4,4 =", R44)
