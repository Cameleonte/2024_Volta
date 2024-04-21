from math import pi

raggio = float(input('Inserire il raggio del cerchio per qui vuoi calculare l\'area: '))
area = pi * raggio ** 2
circonferenza = 2 * pi * raggio

print(f'{area:.2f}')
print(f'{circonferenza:.2f}')
