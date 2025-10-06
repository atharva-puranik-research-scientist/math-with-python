# plotting using formulas with pyplot and matplotlib in python with IDLE
# chapter 02 pg-no.46 -- math with python
# programmer - Atharva Puranik

# Newton's Law of Universal Gravitation

import matplotlib.pyplot as plt, savefig

# Drawing Graph
def draw_graph(x, y):
    plt.plot(x, y, marker = 'o')
    plt.xlabel('Distancce in meters')
    plt.ylabel('Gravitational force in newtons')
    plt.title('Gravitational force and distance')
    filename = 'plotting_with_newtons_law_of_gravitation.png'
    plt.savefig('plotting with newtons law of gravitation.png')
    print("file",filename,"successfully created")
    plt.show()

# Generating values for r
def generate_gravitational_force_F_r():
    r = range(100, 1001, 50)
    gravitational_force_F = []

    # Constant G
    gravitational_constant_G = 6.674*(10**-11)

    # Two masses
    mass_1 = 0.5
    mass_2 = 1.5

    # Calculate force and add it to list, gravitational_force_F
    for dist in r:
        force = gravitational_constant_G*(mass_1*mass_2)/(dist**2)
        gravitational_force_F.append(force)

    # Calling the draw_grpah function
    draw_graph(r, gravitational_force_F)

if __name__ == '__main__':
    generate_gravitational_force_F_r()

    

   
    
    

