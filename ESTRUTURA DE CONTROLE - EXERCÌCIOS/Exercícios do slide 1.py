#exercício 1
def verificar_maior_18(idade):
    if idade >= 18:
        print("Você tem 18 anos ou mais.")
    else:
        print("Você tem menos de 18 anos.")

idade = int(input("Digite sua idade: "))
verificar_maior_18(idade)

#exercício 2
def imprimir_quadrado_se_nao_negativo(numero):
    if numero >= 0:
        print(f"O quadrado de {numero} é {numero ** 2}.")
    else:
        print("Número negativo, não será calculado o quadrado.")

num = int(input("Digite um número: "))
imprimir_quadrado_se_nao_negativo(num)


#exercício 3
def mostrar_maior(a, b, c):
    if a >= b and a >= c:
        maior = a
    elif b >= a and b >= c:
        maior = b
    else:
        maior = c
    print(f"O maior número é {maior}.")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))
mostrar_maior(n1, n2, n3)


#exercício 4
def contar_idades_21(idade1, idade2, idade3, idade4, idade5):
    contador = 0
    if idade1 == 21:
        contador += 1
    if idade2 == 21:
        contador += 1
    if idade3 == 21:
        contador += 1
    if idade4 == 21:
        contador += 1
    if idade5 == 21:
        contador += 1
    print(f"Quantidade de pessoas com 21 anos: {contador}")

idade1 = int(input("Digite a idade da pessoa 1: "))
idade2 = int(input("Digite a idade da pessoa 2: "))
idade3 = int(input("Digite a idade da pessoa 3: "))
idade4 = int(input("Digite a idade da pessoa 4: "))
idade5 = int(input("Digite a idade da pessoa 5: "))

contar_idades_21(idade1, idade2, idade3, idade4, idade5)

#exercício 5
def media_pares(n1, n2, n3, n4):
    soma = 0
    quantidade = 0

    if n1 % 2 == 0:
        soma += n1
        quantidade += 1
    if n2 % 2 == 0:
        soma += n2
        quantidade += 1
    if n3 % 2 == 0:
        soma += n3
        quantidade += 1
    if n4 % 2 == 0:
        soma += n4
        quantidade += 1

    if quantidade > 0:
        media = soma / quantidade
        print(f"A média dos números pares é {media:.2f}.")
    else:
        print("Não há números pares para calcular a média.")


num1 = int(input("Digite o número 1: "))
num2 = int(input("Digite o número 2: "))
num3 = int(input("Digite o número 3: "))
num4 = int(input("Digite o número 4: "))

media_pares(num1, num2, num3, num4)

