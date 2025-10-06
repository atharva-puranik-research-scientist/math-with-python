# plotting trajectory by using projectile motion with pyplot and matplotlib in python with IDLE
# chapter 02 pg-no.48 -- math with python
# programmer - Atharva Puranik

from matplotlib import pyplot as plt
import math

# Drawing Graph
def draw_graph(x, y):
    plt.plot(x, y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')
    filename = 'plotting_trajectory_by_using_projectile_motion_12.png'
    plt.savefig('plotting trajectory using projectile motion 12.png')
    print("file",filename,"successfully created")

# Generating equally spaced floating point numbers
def f_range(start, final, interval):
    numbers = []
    while start < final:
        numbers.append(start)
        start = start + interval
    return numbers

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    acceleration_due_to_gravity_g = 9.8

    # Time of flight
    time_of_flight = 2*u*math.sin(theta)/acceleration_due_to_gravity_g

    # Finding time intervals
    time_intervals = f_range(0, time_of_flight, 0.001)

    # Listing x and y coordinates
    x = []
    y = []

    for t in time_intervals:
        x.append(u*math.cos(theta)*t)
        y.append(u*math.sin(theta)*t - 0.5*acceleration_due_to_gravity_g*t*t)

    # Graph creation
    draw_graph(x, y)

if __name__ == '__main__':
    try:
        u = float(input('Enter the initial velocity (m/s): '))
        theta = float(input('Enter the angle of projection (degrees): '))
    except ValueError:
        print('You entered an invalid output')
    else:
        draw_trajectory(u, theta)
        plt.show()
