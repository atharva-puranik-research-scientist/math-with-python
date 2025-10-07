# plotting trajectory by using projectile motion and randomizing values with pyplot and matplotlib in python with IDLE
# chapter 02 -- math with python
# programmer - Atharva Puranik

from matplotlib import pyplot as plt
import math
import random


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

    # Random color for each plot
    color = random.choice(['red', 'green', 'blue', 'orange', 'purple'])

    # Graph creation
    draw_graph(x, y)

if __name__ == '__main__':

    # Random initla velocity (between 10 and 50m/s)
    u = random.uniform(10, 50)

    # Random angle (between 20 and 80 degree)
    theta = random.uniform(20, 80)

    print(f"randomized initial velocity: {u:.2f} m/s")
    print(f"Randomized angle: {theta:.2f}°")

    draw_trajectory(u, theta)
    plt.show()

