'''nasty.py
'''

from math import cos  

t = 0.0
x = 0.0
dx = 0.0
print("%15.8f %15.8f %15.8f" % (t, x, dx))
dt = 18.84955592153876 / 10
for i in range(10):
    xold = x
    dxold = dx

    x += dt * dxold
    dx += dt * (cos(0.5*t) - xold - 0.5*dxold)
    t += dt
    print("{0:>15.8f} {1:>15.8f} {2:>15.8f}".format(t, x, dx))
print()

t = 0.0
x = 0.0
dx = 0.0
print("%15.8f %15.8f %15.8f" % (t, x, dx))
dt = 18.84955592153876 / 20
for i in range(20):
    xold = x
    dxold = dx

    x += dt * dxold
    dx += dt * (cos(0.5*t) - xold - 0.5*dxold)
    t += dt
    print("{:15.8f} {:15.8f} {:15.8f}".format(t, x, dx))
print()

t = 0.0
x = 0.0
dx = 0.0
print("%15.8f %15.8f %15.8f" % (t, x, dx))
dt = 18.84955592153876 / 40
for i in range(40):
    xold = x
    dxold = dx

    x += dt * dxold
    dx += dt * (cos(0.5*t) - xold - 0.5*dxold)
    t += dt
    print("{:15.8f} {:15.8f} {:15.8f}".format(t, x, dx))
print()


t = 0.0
x = 0.0
dx = 0.0
print("%15.8f %15.8f %15.8f" % (t, x, dx))
dt = 18.84955592153876 / 10
for i in range(10):
    xold = x
    dxold = dx

    x += dt * dxold
    dx += dt * (cos(2.0*t) - xold - 0.5*dxold)
    t += dt
    print("{0:>15.8f} {1:>15.8f} {2:>15.8f}".format(t, x, dx))
print()

t = 0.0
x = 0.0
dx = 0.0
print("%15.8f %15.8f %15.8f" % (t, x, dx))
dt = 18.84955592153876 / 20
for i in range(20):
    xold = x
    dxold = dx

    x += dt * dxold
    dx += dt * (cos(2.0*t) - xold - 0.5*dxold)
    t += dt
    print("{:15.8f} {:15.8f} {:15.8f}".format(t, x, dx))
print()

t = 0.0
x = 0.0
dx = 0.0
print("%15.8f %15.8f %15.8f" % (t, x, dx))
dt = 18.84955592153876 / 40
for i in range(40):
    xold = x
    dxold = dx

    x += dt * dxold
    dx += dt * (cos(2.0*t) - xold - 0.5*dxold)
    t += dt
    print("{:15.8f} {:15.8f} {:15.8f}".format(t, x, dx))
print()

