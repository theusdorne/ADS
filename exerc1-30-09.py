'''''
# Altere o exercício anterior para informar quantos números
# pares no intervalo entre 10 e 30, ou no intervalo entre
# 50 e 70, foram digitados.
#
# Mostre também o percentual de números ímpares que foram
# digitados no intervalo entre 25 e 60.



# Altere o exercício anterior para informar quantos números
# pares no intervalo entre 10 e 30, ou no intervalo entre
# 50 e 70, foram digitados.
#
# Mostre também o percentual de números ímpares que foram
# digitados no intervalo entre 25 e 60.


list1 = 10 a 30
list2 = 50 a 70
list3 = 25 a 60
'''
list1 = []
list2 = []
list3 = []

list3_imp = []
len_imp = 0

porcen_imp = 0

while True:
    n1 = int(input("Digite um número inteiro: "))

    if n1 == 0:
        break
    if n1 >= 10 and n1 <= 30 and n1%2 == 0:
        list1.append(n1)
    elif n1 >= 50 and n1 <=70 and n1%2 == 0:
        list2.append(n1)
    if n1 >= 25 and n1 <= 60:
        list3.append(n1)



    if (n1%2) == 0:
     txt = ("Par")
    else:
     txt =("Ímpar")

    if n1 >= 0:
        txt += " Positivo"
    else:
        txt += " Negativo"

    print("O número digitado é",txt)

print("No intervalo de 10 a 30 foram digitados ",len(list1),"números pares.")
print(list1)
print("No intervalo de 50 a 70 foram digitados ", len(list2), "números pares.")
print(list2)



for num in list3:
        if num % 2 != 0:
            len_imp += 1
            list3_imp.append(num)

if sum(list3_imp) != 0:
    porcen_imp = (len_imp * 100)/len(list3)

print("No intervalo de 25 a 60, %",porcen_imp, "dos números são impares.")
print(list3)



