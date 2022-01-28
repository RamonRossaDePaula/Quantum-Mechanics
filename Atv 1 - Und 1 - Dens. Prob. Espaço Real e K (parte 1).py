
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

# Atividade 1 - Função densidade de probabilidade


    # Função Ψ(x):

def psi0(x):                                                                                     
    return (sqrt(0.02*log(12))/pi)*5*exp(-0.02*log(12)*(x-2.311)**2) + 0.0527
    

     # Código para o gráfico:

x = np.arange(-8,11,0.1)
plt.plot(x,psi0(x)**2)
plt.title('Densidade de Probabilidade')
plt.xlabel('x')
plt.ylabel('$|\Psi(x)|^2$')
plt.show()


     # Probabilidade, <x> e <x²>:

probabilidade,err = integrate.quad(lambda x :psi0(x)**2,-np.inf,np.inf)
media_x,err = integrate.quad(lambda x :x*psi0(x)**2,-np.inf,np.inf)
media_x_quad,err = integrate.quad(lambda x :x**2*psi0(x)**2,-np.inf,np.inf)


     # Probabilidade, Média e Desvio Padrão:

print ('Área = {:.3f}'.format(probabilidade))                                             # Probabilidade = Integral de -∞ a +∞ de |Ψ(x)|² = 1
print ('Média = {:.3f}'.format(media_x))                                                  # <x> = Integral de -∞ a +∞ de (x * |Ψ(x)|²)
print ('Desvio Padrão = {:.3f}'.format(math.sqrt(media_x_quad-media_x**2)))               # σ² = <x²> - <x>²
