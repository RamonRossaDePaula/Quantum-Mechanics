
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

# Calculando a transformada de Fourier

def psi(x):
    r = (2*np.pi)**-0.25*np.exp(-x**2/4)
    return complex(r*np.cos(np.pi/3*x),r*np.sin(np.pi/3*x))

def prob_dens(x):
    z = psi(x)
    return z.real**2 + z.imag**2

x_arr = np.arange(-5,5,0.1)

pp=[]

for x in x_arr:
    pp.append(prob_dens(x))


def A(k):
    def integrando1(x):
        z = psi(x)
        return z.real*np.cos(k*x)-z.imag*np.sin(-k*x)
    def integrando2(x):
        z = psi(x)
        return z.real*np.sin(-k*x)+z.imag*np.cos(k*x)    
    A1,err1 = integrate.quad(integrando1,-np.inf,np.inf)
    A2,err2 = integrate.quad(integrando2,-np.inf,np.inf) 
    return complex(A1/(np.sqrt(2*np.pi)),A2/(np.sqrt(2*np.pi)))

def prob_dens_fourier(k):
    z = A(k)
    return (z.real**2 + z.imag**2)
dk = 0.1
k_arr = np.arange(-5,5,0.1)
pp_fourier=[]
for k in k_arr:
    pp_fourier.append(prob_dens_fourier(k))
plt.plot(k_arr,pp_fourier)
plt.title('Densidade de Probabilidade k')
plt.xlabel('k')
plt.ylabel('$|A(k)|^2$')
area = np.sum(pp_fourier)*dk
kmean = np.sum(k_arr*pp_fourier)*dk
k2mean = np.sum(k_arr**2*pp_fourier)*dk
delta_k = np.sqrt(k2mean-kmean**2)
print ('area = {:.3f}'.format(area))
print ('média = {:.3f}'.format(kmean))
print ('desvio padrão = {:.3f}'.format(math.sqrt(k2mean-kmean**2)))

# ____________________________________________________________________________________


## Atividade 3:  Mostrar com exemplos que Δx Δk ≥ 0.5

fig, axs = plt.subplots(1,2)

axs[0].plot(x_arr,pp)
axs[1].plot(k_arr,pp_fourier)
axs[0].set(xlabel='x', ylabel='$|\Psi(x)|^2$')
axs[1].set(xlabel='k', ylabel='$|A(k)|^2$')
fig.tight_layout(pad=1.0)
plt.show()
print('Dx Dk = {:.3f}'.format(delta_x*delta_k))