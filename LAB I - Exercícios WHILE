# 1. faça um programa que leia valores de uma compra e pare quando o valor for diferente de 0
 
valor = float(input("digite um valor: "))
total = itens = media = maior = 0

while valor != 0:
  total += valor
  itens += 1
  if valor > maior:
     maior = valor
  valor = float(input("digite um valor: "))

if valor != 0:
    media = total/itens

print(f"sua compra ficou no total de R$ {total:.2f}, com {itens} itens")
print(f"a média foi de R${media:.2f}, o maior valor foi de R$ {maior}")

----------

# 2. Faça um código que leia uma nota mas só aceite valores acima ou igual a 0 e menores ou iguais a 10. Imprima "Valor Inválido" ou o valor

nota = float(input("digite uma nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print('valor inválido')
    nota = float(input("digite uma nota entre 0 e 10: "))

print('valor válido, sua nota é', nota)

----------

# 3. Faça um código que leia uma altura mas só aceite valores maiores que 0 e menores que 3. Imprima "Valor Inválido" ou o valor

altura = float(input("digite uma altura (em metros) maior que zero e menor que três: "))

while altura < 0 or altura > 3:
  print("altura inválida")
  altura = float(input("digite uma altura (em metros) maior que zero e menor que três: "))

print("altura válida, sua altura é", altura)

----------

# 4. Leia duas notas de um aluno, informe a sua média. Seu programa deve forçar ao usuário a digitar notas na faixa de 0 a 10, informando "Valor inválido" no caso de nota inválida.

nota1 = float(input("digite a primeira nota entre 0 e 10: "))

while nota1 < 0 or nota1 > 10:
    print("nota inválida")
    nota1 = float(input("digite a primeira nota entre 0 e 10: "))

nota2 = float(input("digite a segunda nota entre 0 e 10: "))

while nota2 < 0 or nota2 > 10:
    print("nota inválida")
    nota2 = float(input("digite a segunda nota entre 0 e 10: "))

media = (nota1 + nota2) // 2
print("a média das notas é de", media)

----------

# 5. Faça um código que leia valores até que seja digitado 0. Imprima quantos itens foram lidos e qual a média dos valores

c = total = 0

while True:
  nota = float(input("digite um valor: "))
  if nota == 0:
    break
  c += 1
  total += nota


media = total / c
print(f"foram lidos {c} valores e média é de {media: .2f}")

----------

# 6. Faça um código que leia valores até que seja digitado 0. Imprima o maior valor digitado

nota = float(input("digite um valor: "))
maior = nota

while nota != 0:
  if nota > maior:
    maior = nota
  nota = float(input("digite um valor: "))

print("a maior nota digitada é de", maior)



