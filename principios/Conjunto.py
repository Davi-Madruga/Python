#Conjuntos(set)
numerospares = {2,4,6,8}
numerosimpares = {1,3,5,7}

numerospares.add(10)
numerosimpares.add(9)

numerosinteiros =   (numerosimpares | numerospares)
print(numerosimpares | numerospares)
print(numerosimpares & numerospares)
print(numerosimpares - numerospares)
print(numerosimpares ^ numerospares)