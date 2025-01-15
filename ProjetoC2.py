# 1. Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e
continue pedindo até que o usuário informe um valor válido.

nota = float(input("Digite sua nota entre 0 e 10: "))

while nota < 0 or nota > 10:
    print("Valor inválido, por favor insira novamente")
    nota = float(input("Digite sua nota com um valor válido (0 a 10): "))

print(f"Sua nota é: {nota}")

----------

# 2. Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem
de erro e voltando a pedir as informações.

nome_de_usuario = input("Digite o nome de usuário: ")
senha = input("Digite sua senha: ")

while senha == nome_de_usuario:
    print("ERRO! A senha não pode ser igual ao nome de usuário")

    senha = input("Digite uma nova senha: ")

print(f"Cadastro completo, seu usuário é '{nome_de_usuario}' e sua senha é '{senha}'")

----------

# 2.1 Agora modifique o programa para obrigar que o usuário
# tenha na senha uma letra, um número, um caracter especial e, pelo menos, tamanho 8.

def verificar(senha):
  letra = numero = especial = 0
  if senha == usuario:
    print("A senha nao pode ser igual ao usuario")
    return False
  if len(senha) < 8:
    print("A senha precisa ter no minimo 8 caracteres")
    return False

  for item in senha:
    if item.isdigit():
      numero += 1
    if item.isalpha():
      letra += 1
    if item in "!?&@$/(%{}[]^*+=#":
      especial += 1

  if letra == 0 or numero == 0 or especial == 0:
    print("A senha precisa de no minimo uma letra, um numero e um caractere especial")
    return False

usuario = input("Digite o usuario: ")

while True:
  senha = input("Digite a senha: ")

  while verificar(senha) == False:
    break
  else:
    break

print(f"Senha cadastrada com sucesso! Seu usuario é '{usuario}' e sua senha é '{senha}'")

----------

# 3. Pergunte aos clientes da academia o seu código, altura e peso. o final da digitação é dado quando o usuário digitar zero (0) no campo do código.
ao encerrar deve ser informados os códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais magro, além da média das alturas e dos pesos dos clientes.

print("Você está na lista da academia! para sair digite '0'")

codigo = input("Digite o código do aluno: ")
peso = float(input("Digite o peso do aluno: "))
altura = float(input("Digite a altura do aluno: "))


maior_peso = menor_peso = peso
aluno_mais_gordo = aluno_mais_magro = codigo

maior_altura = menor_altura = altura
aluno_mais_alto = aluno_mais_baixo = codigo

total_pesos = total_alturas = total_alunos = media_pesos = media_alturas = 0

while True:

    if codigo == str(0):
        break

    total_alunos += 1
    total_alturas += altura
    total_pesos += peso

    if total_alunos != 0:
        media_alturas = total_alturas / total_alunos
        media_pesos = total_pesos / total_alunos

    if peso > maior_peso:
        maior_peso = peso
        aluno_mais_gordo = codigo

    if peso < menor_peso:
        menor_peso = peso
        aluno_mais_magro = codigo

    if altura > maior_altura:
        maior_altura = altura
        aluno_mais_alto = codigo

    if altura < menor_altura:
        menor_altura = altura
        aluno_mais_baixo = codigo


    codigo = input("Digite o código do aluno: ")
    if codigo == str(0):
        break
    peso = float(input("Digite o peso do aluno: "))
    altura = float(input("Digite a altura do aluno: "))

print(f"Total de alunos: {total_alunos}")
print(f"Aluno mais gordo: {aluno_mais_gordo} com {maior_peso} quilos\nAluno mais magro: {aluno_mais_magro} com {menor_peso} quilos\nMedia de pesos: {media_pesos:.2f}")
print(f"Aluno mais alto: {aluno_mais_alto} com {maior_altura} metros\nAluno mais baixo: {aluno_mais_baixo} com {menor_altura} metros\nMedia de alturas: {media_alturas:.2f}")

----------

# 4. Faça um programa que leia uma lista de nomes de alunos suas respectivas notas e calcule a média da turma.
Utilize um loop while para ler os dados até que o usuário digite 0 no nome para sair.

print("Você entrou na lista de alunos! para sair digite '0'")

total_alunos = total_notas = 0
nomes_alunos = ''

while True:

    nome_aluno = input("Digite seu nome: ")
    if nome_aluno == str(0):
        break

    nota_aluno = float(input("Digite sua nota: "))

    total_alunos += 1
    total_notas += nota_aluno
    nomes_alunos += (nome_aluno + '; ')

if total_alunos != 0:
    media = total_notas / total_alunos
    print(f"Número de alunos: {total_alunos}\nNome dos alunos: {nomes_alunos}\nNota total da sala: {total_notas}\nA média da sala é: {media:.2f}")
else:
    print("Você não adicionou nenhum dado")
print("Você saiu da lista!")
