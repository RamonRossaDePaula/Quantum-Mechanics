
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

# Calculando a área do resultado da integral fundamental:

def fe(a, ep):
    return sqrt(pi/ep) * exp((-a**2)/(4*ep))

    
# Código para o gráfico:

a = np.arange(-10, 10, 0.01)

plt.title("Área")
plt.xlabel('α')
plt.ylabel('fe(α)')
plt.grid()
plt.legend(['ε = 0.1', 'ε = 0.5', 'ε = 1', 
            'ε = 1.5', 'ε = 2', 'ε = 5', 
            'ε = 10', 'ε = 20', 'ε = 50', 'ε = 100', ], loc=1)

plt.plot(a, fe(a, 0.1))   # Largura proporcional a ε e altura proporcional a 1/ε.
plt.plot(a, fe(a, 0.5))
plt.plot(a, fe(a, 1))
plt.plot(a, fe(a, 1.5))
plt.plot(a, fe(a, 2))
plt.plot(a, fe(a, 5))
plt.plot(a, fe(a, 10))
plt.plot(a, fe(a, 20))
plt.plot(a, fe(a, 50))
plt.plot(a, fe(a, 100))

plt.show()


