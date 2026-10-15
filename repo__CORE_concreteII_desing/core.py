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
    def __init__(self, x = any,y = any, title = 'test', xlabel = 'x', ylabel = 'y', color = (0,0,0), grid_direction = 'x'):
        self.x = x                                                      # Store x in the instance
        self.y = y                                                      # Store y in the instance
        self.title = title                                              # Store the title
        self.xlabel = xlabel                                            # Store the x label
        self.ylabel = ylabel                                            # Store the y label
        self.color = color
        self.grid_direction = grid_direction

    def SimplePlot(self):
        x = self.x                                                      # Read x from the instance
        y = self.y                                                      # Read y from the instance
        title = self.title                                              # Read the title
        xlabel = self.xlabel                                            # Read the x label
        ylabel = self.ylabel                                            # Read the y label
        color = self.color
        grid_direction = self.grid_direction


        fig, ax = plt.subplots(1,1, figsize = (15,6))                   # Create a figure with one subplot
        ax.plot(x,y, ls = '-', lw = 2, color = color, label = title)  # Draw the curve
        ax.set_title(title, color = (0,0,0), fontsize = 14)             # Add a title
        ax.set_xlabel(xlabel)                                           # Label the x axis
        ax.set_ylabel(ylabel)                                           # Label the y axis
        ax.set_xlim(np.min(x),np.max(x))                                # Axis limits computed from the data
        ax.grid(which='both', axis=grid_direction, alpha=0.5)
        plt.show()                                                      # Render the figure

#########################################################################################################################################
#########################################################################################################################################
########################################################### As, Asmin, fiMn #############################################################
#########################################################################################################################################
#########################################################################################################################################
class SimpleFlexuralCapacity():
    def __init__(self, fc = 280, fy = 4200, bw = 100, H = 30, rec = 2.5,fi = 0.9, diF = 1.2, Mu = 2.3*1e5):
        self.fc = fc
        self.fy = fy
        self.bw = bw
        self.H = H
        self.rec = rec
        self.fi = fi
        self.diF = diF
        self.Mu = Mu

    def as_asmin(self):
        fc = self.fc
        fy = self.fy
        bw = self.bw
        H = self.H
        rec = self.rec
        fi = self.fi
        diF = self.diF
        Mu = self.Mu

        d = H-rec-diF/2
        As = 1/ fi* (0.85*fc*bw/fy * (d - np.sqrt(d**(2) - 2*Mu/(0.85*fc*bw))))
        Asmin = 0.0018*bw*H

        if As > Asmin:
            Asexc = As - Asmin
            numvar_exc = np.ceil(Asexc / (np.pi * diF**(2) / 4))
            Asexc = numvar_exc * (np.pi * diF**(2) / 4)
            S_exc = bw / numvar_exc
            fiMnexc = fi*(Asexc*fy*(d - Asexc*fy/(1.70*fc*bw)))

            numvar_min = np.ceil(Asmin / (np.pi * diF**(2) / 4))
            Asmin = numvar_min * (np.pi * diF**(2) / 4)
            S_min = bw / numvar_min
            fiMnmin = fi*(Asmin*fy*(d - Asmin*fy/(1.70*fc*bw)))

            fiMn = fiMnexc + fiMnmin

            if fiMn >= Mu:
                mensaje = 'ok'
            else:
                mensaje = 'mal'

            print('='*120)
            print('.'*90)
            print(f'Mu = {Mu/1e5:.2f} T-m')
            print(f'H = {H:.2f} cm')
            print(f'd = {d:.2f} cm')
            print('.'*90)
            print('Requeried extra Reinforcement')
            print(f'Asexc = {Asexc:.3f} cm2')
            print(f'1 Φ {diF*10:.0f} @ {S_exc:.0f} / cant = {numvar_exc:.0f} --> bw = {bw:.0f} cm')
            print(f'Asmin = {Asmin:.3f} cm2')
            print(f'1 Φ {diF*10:.0f} @ {S_min:.0f} / cant = {numvar_min:.0f} --> bw = {bw:.0f} cm')
            print(f'ΦMn = {fiMn/1e5:.2f} T-m , Mu = {Mu/1e5:.2f} T-m, check = {mensaje}, DCR = {Mu/fiMn * 100:.0f} %')
            print('='*120)
        else:
            Asexc = 0
            S_exc = 0
            numvar_exc = 0
            numvar_min = np.ceil(Asmin / (np.pi * diF**(2) / 4))
            Asmin = numvar_min * (np.pi * diF**(2) / 4)
            S_min = bw / numvar_min
            fiMnmin = fi*(Asmin*fy*(d - Asmin*fy/(1.70*fc*bw)))

            fiMn = fiMnmin
            
            if fiMn >= Mu:
                mensaje = 'ok'
            else:
                mensaje = 'mal'

            print('='*120)
            print('.'*90)
            print(f'Mu = {Mu/1e5:.2f} T-m')
            print(f'H = {H:.2f} cm')
            print(f'd = {d:.2f} cm')
            print('.'*90)
            print('Does not requeried extra Reinforcement')
            print(f'Asmin = {Asmin:.3f} cm2')
            print(f'1 Φ {diF*10:.0f} @ {S_min:.0f} / cant = {numvar_min:.0f} --> bw = {bw:.0f} cm')
            print(f'ΦMn = {fiMn/1e5:.2f} T-m , Mu = {Mu/1e5:.2f} T-m, check = {mensaje}, DCR = {Mu/fiMn * 100:.0f} %')
            print('='*120)
    
        return Asexc, Asmin, S_exc, S_min, numvar_exc, numvar_min, fiMn, Mu 

#########################################################################################################################################
#########################################################################################################################################
############################################################ fiVc slab ##################################################################
#########################################################################################################################################
#########################################################################################################################################
class SimpleShearSlab():
    def __init__(self, fc = 280, fy = 4200, bw = 100, H = 30, rec = 2.5,fi = 0.75, diC = 1.0, Vu = 2000, lamda = 1,
                 tc = 30, tl = 40, alfas = 40):
            self.fc = fc
            self.fy = fy
            self.bw = bw
            self.H = H
            self.rec = rec
            self.fi = fi
            self.diC = diC
            self.Vu = Vu
            self.lamda = lamda   
            self.tc = tc
            self.tl = tl
            self.alfas = alfas

    def Vc_Slab(self):
        fc = self.fc 
        fy = self.fy
        bw = self.bw
        H = self.H
        rec = self.rec
        fi = self.fi
        diC = self.diC
        Vu = self.Vu 
        lamda = self.lamda   
        tc = self.tc
        tl = self.tl
        alfas = self.alfas

        d = H-rec        
        lamdas = np.sqrt(2 / (1 + 0.04*d)) 
        if lamdas <= 1:
            lamdas = lamdas
        else:
            lamdas = 1 
        beta = tl/tc

        match alfas:
            case 40:
                bo = 2*(d+tc) + 2*(d+tl)
            case 30:
                bo = (d+tc) + 2*(d/2 + tl)
            case 20:
                bo = (d/2+tc) + (d/2 + tl)
            case _:
                raise ValueError("alfas debe ser 40, 30 o 20")
        
        #-------ΦVc (a)[ACI 22.6.5.2]-------# 
        FiVc_a = fi*(1.1*lamdas*lamda*np.sqrt(fc)*bw*d)
        #-------ΦVc (b)[ACI 22.6.5.2]-------# 
        FiVc_b = fi*(0.53*(1 + 2/beta)*lamdas*lamda*np.sqrt(fc)*bw*d)
        #-------ΦVc (c)[ACI 22.6.5.2]-------# 
        FiVc_c = fi*(0.27*(2 + alfas * d/bo)*lamdas*lamda*np.sqrt(fc)*bw*d)