"""
Faça um algoritmo que leia um valor para saque em Reais,
e diga quantas notas de cada são necessárias para
para formar o valor lido.
Considerar notas de 200, 100, 50, 20, 10, 5 e 2 Reais.

Exemplo:
Digite o valor em Reais: 380
Para esse valor precisamos de:
1 nota de 200
1 nota de 100
1 nota de 50
1 nota de 20
1 nota de 10
"""

valor = int(input("Digite o valor do saque: "))

notas200 = 0
notas100 = 0
notas50 = 0
notas20 = 0
notas10 = 0
notas5 = 0
notas2 = 0


while valor != 1 and valor != 0:

 if valor >= 200:
    notas200 += 1
    valor -= 200
 else:
     if valor >= 100:
         notas100 += 1
         valor -= 100
     else:
         if valor >= 50:
             notas50 += 1
             valor -= 50
         else:
             if valor >= 20:
                 notas20 += 1
                 valor -= 20
             else:
                 if valor >= 10:
                     notas10 += 1
                     valor -= 10
                 else:
                     if valor >= 5:
                         notas5 += 1
                         valor -= 5
                     else:
                         if valor >= 2:
                             notas2 += 1
                             valor -= 2

print("Notas para valor digitado: ")
if notas200 != 0 :
    print(notas200,"nota(s) de $200")
if notas100 != 0 :
    print(notas100,"nota(s) de $100")
if notas50 != 0 :
    print(notas50,"nota(s) de $50")
if notas20 != 0 :
    print(notas20,"nota(s) de $20")
if notas10 != 0 :
    print(notas10,"nota(s) de $10")   
if notas5 != 0 :
    print(notas5,"nota(s) de $5")
if notas2 != 0 :
    print(notas2,"nota(s) de $2")