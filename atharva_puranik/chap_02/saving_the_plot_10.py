# saving the plots in pyplot and matplotlib in python with IDLE
# chapter 02 pg-no.45 -- math with python
# programmer - Atharva Puranik

import matplotlib.pyplot as plt, savefig

def create_graph():
    x_numbers_list = [1, 2, 3]
    y_numbers_list = [2, 4, 6]

    plt.plot(x_numbers_list, y_numbers_list)
    # plt.show()
    filename = 'mygraph_10.png'
    plt.savefig(filename)
    print("file",filename,"successfully created")

if __name__ == '__main__':
    create_graph()
    
    

