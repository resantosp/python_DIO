#Aula Conjuntos

#conjunto.add()
#conjunto.discard()

conjunto1 = {1, 2, 3, 4}
conjunto2 = {3, 4, 5, 6}

uniao = conjunto1.union(conjunto2)
print('A união dos conjuntos é: {}'.format(uniao))
interseccao = conjunto1.intersection(conjunto2)
print('A intersecção dos conjuntos é: {}'.format(interseccao))
dif1 = conjunto1.difference(conjunto2)
print('A diferença entre 1 e 2 é: {}'.format(dif1))
dif2 = conjunto2.difference(conjunto1)
print('A diferença entre 2 e 1 é: {}'.format(dif2))
dif_sim = conjunto1.symmetric_difference(conjunto2)
print('A diferença simétrica entre 1 e 2 é: {}'.format(dif_sim))

conjA = {1, 2, 3}
conjB = {1, 2, 3, 4, 5}

subconj = conjA.issubset(conjB)
if subconj == True:
    print('O conjunto a É SIM subconjunto do conjunto b.')
else:
    print('O conjunto a NÃO É subconjunto do conjunto b.')

superconj = conjA.issuperset(conjB)
if superconj == True:
    print('O conjunto a É SIM um superconjunto do conjunto b.')
else:
    print('O conjunto a NÃO É um superconjunto do conjunto b.')

#Transformando lista em conjunto e vice-versa... essa é uma forma simples de remover as duplicidades de uma lista (convertendo em conjunto e depois reconvertendo em lista)
lista = ['Morango', 'Morango', 'Uva', 'Goiaba', 'Goiaba']
print(lista)
conjunto_frutas = set(lista)
print(conjunto_frutas)
lista_frutas = list(conjunto_frutas)
print(lista_frutas)
