from math import cos

TWO_PI = 18.84955592153876  #1 oscillation period
COS_MOD = 0.5
DRAG_COEF = 0.5

num_steps = int
freq_mod = float

def simulate_motion(num_steps, freq_modifier):
    t, x, dx = 0.0, 0.0, 0.0
    dt = TWO_PI / num_steps
    
    #getting assistance from my friends for equation
    print(f"{t:15.8f} {x:15.8f} {dx:15.8f}")
    for i in range(num_steps):
        xold, dxold = x, dx
        x += dt * dxold
        dx += dt * (cos(freq_modifier * t) - xold - DRAG_COEF * dxold)
        t += dt
        print(f"{t:15.8f} {x:15.8f} {dx:15.8f}")
    print()

def main():
    #simulate different step and frequency modifiers
    for steps in [10, 20, 40]:
        simulate_motion(steps, COS_MOD)
    for steps in [10, 20, 40]:
        simulate_motion(steps, 2.0)

if __name__ == "__main__":
    main()
