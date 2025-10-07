# plotting graph using newtons law of gravitation and randomizing values with pyplot and matplotlib in python with IDLE
# chapter 02 -- math with python
# programmer - Atharva Puranik

import matplotlib.pyplot as plt, savefig
import random


# Drawing Graph
def draw_graph(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel('Distancce in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    filename = 'plotting_with_newtons_law_of_gravitation_and_randomizing_values.png'
    plt.savefig('plotting with newtons law of gravitation and randomizing values.png')
    print("file",filename,"successfully created")
    plt.show()

# Generating values for r
def generate_gravitational_force_F_r():
    r = range(100, 1001, 50)
    gravitational_force_F = []

    # Constant G
    gravitational_constant_G = 6.674*(10**-11)

    # Random two masses between given ranges (in kg)
    mass_1 = random.uniform(0.1, 0.5)
    mass_2 = random.uniform(0.1, 0.5)

    print(f"Random Mass 1: {mass_1:.2f} kg")
    print(f"Random Mass 2: {mass_2:.2f} kg")

    # Calculate force and add it to list, gravitational_force_F
    for dist in r:
        force = gravitational_constant_G*(mass_1*mass_2)/(dist**2)
        gravitational_force_F.append(force)

    # Plotting the graph
    draw_graph(r, gravitational_force_F)

if __name__ == '__main__':
    generate_gravitational_force_F_r()

    

   
    
    

