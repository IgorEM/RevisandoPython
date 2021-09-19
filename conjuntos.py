# conjunto = {3,6,1,4,9,1,2,3,6,7,8,11,0}
# conjunto.add(5)
# conjunto.discard(0)
# print(conjunto) #set(conjunto) imprime sempre ordenado e não há duplicidade
# print(type(conjunto)) #set - conjunto

conjunto1 = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
print('Conjunto 1: {}'.format(conjunto1))
print('Conjunto 2: {}'.format(conjunto2))

conjunto_uniao = conjunto1.union(conjunto2)
print('União: {}'.format(conjunto_uniao))

conjunto_intersecao = conjunto1.intersection(conjunto2)
print('Intersecção: {}'.format(conjunto_intersecao))

conjunto_diferenca1 = conjunto1.difference(conjunto2)
conjunto_diferenca2 = conjunto2.difference(conjunto1)
print('Diferença entre 1 e 2: {}'.format(conjunto_diferenca1))
print('Diferença entre 2 e 1: {}: '.format(conjunto_diferenca2))

conjunto_diff_simetrica = conjunto1.symmetric_difference(conjunto2)
print('Diferença simétrica: {}: '.format(conjunto_diff_simetrica))
#imprime tudo que tem tem diferente entre um e outro

a = {1,2,3}
b = {1,2,3,4,5}
conjunto_subset = a.issubset(b)
conjunto_subset1 = b.issubset(a)

print(conjunto_subset) # True a está dentro de b
print(conjunto_subset1) #false, b não está em a

conjunto_superset = b.issuperset(a)
print(conjunto_superset) #True , b é um superset de  a , b inclue a dentro dele



