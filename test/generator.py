import random

# Parametri
n = 10
delta = 1.5

# Generazione casuale delle coordinate
coordX = {i: random.randint(0, 100) for i in range(n + 1)}
coordY = {i: random.randint(0, 100) for i in range(n + 1)}

# Scrittura nel file AMPL
with open(f'pedalbus_{n}.dat', 'w') as f:
    f.write('param n := {}\n;\n\n'.format(n))
    f.write('param delta := {}\n;\n\n'.format(delta))
    f.write('param coordX :=\n')
    for i in range(n + 1):
        f.write('{:<2}  {:>2}\n'.format(i, coordX[i]))
    f.write(';\n\n')
    f.write('param coordY :=\n')
    for i in range(n + 1):
        f.write('{:<2}  {:>2}\n'.format(i, coordY[i]))
    f.write(';\n')
