import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


#########################################################################################################################################
#########################################################################################################################################
######################################################## Simple Matriz stack ############################################################
#########################################################################################################################################
#########################################################################################################################################
class SimpleMatrixStack:
    
    def __init__(self, hola):
        self.hola = hola
        
    def matriz(self):
        hola = self.hola
        
        auto = np.zeros([4,4])
        i = 0
        for j in np.arange(1,4+1,1):
            auto[i,:] = np.linspace((j * hola),(j * hola) +12,4)
            i = i+1
    
        return auto


#########################################################################################################################################
#########################################################################################################################################
########################################################### Simple Class ################################################################
#########################################################################################################################################
#########################################################################################################################################
class SimpleClass():
    def __init__(self, x = any,y = any, title = 'test', xlabel = 'x', ylabel = 'y', color = (0,0,0)):
        self.x = x                                                      # Store x in the instance
        self.y = y                                                      # Store y in the instance
        self.title = title                                              # Store the title
        self.xlabel = xlabel                                            # Store the x label
        self.ylabel = ylabel                                            # Store the y label
        self.color = color

    def SimplePlot(self):
        x = self.x                                                      # Read x from the instance
        y = self.y                                                      # Read y from the instance
        title = self.title                                              # Read the title
        xlabel = self.xlabel                                            # Read the x label
        ylabel = self.ylabel                                            # Read the y label
        color = self.color


        fig, ax = plt.subplots(1,1, figsize = (15,6))                   # Create a figure with one subplot
        ax.plot(x,y, ls = '-', lw = 2, color = color, label = title)  # Draw the curve
        ax.set_title(title, color = (0,0,0), fontsize = 14)             # Add a title
        ax.set_xlabel(xlabel)                                           # Label the x axis
        ax.set_ylabel(ylabel)                                           # Label the y axis
        ax.set_xlim(np.min(x),np.max(x))                                # Axis limits computed from the data
        plt.show()                                                      # Render the figure