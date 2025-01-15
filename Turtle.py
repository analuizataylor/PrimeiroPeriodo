# aula inicial sobre programação, utilizando a biblioteca turtle em python para aprender sobre comandos básicos
# desenho de formas geométricas com base no número de lados e cor 

import turtle
t = turtle.Turtle()

lados = int(input('Informe o número de lados:'))
cor = str(input('Informe a cor: '))
angulo = 360/lados

t.begin_fill()
t.fillcolor(cor)
t.speed(1)  

for i in range(lados):
  i = int(i)
  t.forward(angulo)
  t.left(angulo)

t.end_fill()
t.screen.mainloop()
