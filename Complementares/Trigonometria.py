from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo desejado: '))
seno = sin(radians(angulo))
print('O ângulo de {} tem o Seno de {:.2f}'.format(angulo,seno))

coseno = cos(radians(angulo))
print('O ângulo de {} tem o Coseno de {:.2f}'.format(angulo,coseno))

tangente = tan(radians(angulo))
print('O ângulo de {} tem o Tangente de {:.2f}'.format(angulo,tangente))