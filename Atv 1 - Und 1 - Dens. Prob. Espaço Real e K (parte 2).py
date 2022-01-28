
# Disciplina: Mecânica Quântica (FIS01210)
# Aluno: Ramon Rossa de Paula (00243967)

# "Este trabalho foi produzido em Python, utilizando a IDE Visual Studio Code, exclusivamente por mim. Nenhuma parte deste trabalho (texto e fórmulas) foi copiada digitalmente de outras fontes"





# ____________________________________________________________________________________

# Importações

import math
import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
from scipy import integrate
from numpy import sqrt, exp, log, pi, abs

# ____________________________________________________________________________________

# Atividade 2 - O mesmo para psi complexo

def psi(x):
    r = (5*np.pi)**-0.38*np.exp(-x**2/41.9)
    return complex(r*np.cos(np.pi/3*x),r*np.sin(np.pi/3*x))

def prob_dens(x):
    z = psi(x)
    return z.real**2 + z.imag**2

x_arr = np.arange(-15,15,0.1)

pp=[]

for x in x_arr:
    pp.append(prob_dens(x))

plt.plot(x_arr,pp)
plt.title('Densidade de Probabilidade')
plt.xlabel('x')
plt.ylabel('$|\Psi(x)|^2$')
plt.show()

probabilidade,err = integrate.quad(lambda x :prob_dens(x),-np.inf,np.inf)
media_x,err = integrate.quad(lambda x :x*prob_dens(x),-np.inf,np.inf)
media_x_quad,err = integrate.quad(lambda x :x**2*prob_dens(x),-np.inf,np.inf)
delta_x = np.sqrt(media_x_quad-media_x**2)
print ('Área = {:.3f}'.format(probabilidade))
print ('Média = {:.3f}'.format(media_x))
print ('Desvio Padrão = {:.3f}'.format(delta_x))