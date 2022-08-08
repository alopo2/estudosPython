#Exemplo de listas

cachorros = ['Dori','Boni','Diana','Ema']
print(cachorros[:3])
#Conseguimos pegar Dori, Boni e Diana
print(cachorros[:])
#exibe toda a lista, sem intervalo

#Usando o pop para remover elementos
nome_removido = cachorros.pop(3)
print(cachorros)
print(nome_removido)
#remove a posição 3, que é Ema. 

#remove a posição 1, que é Boni
nome_removido = cachorros.pop(1)
print(cachorros)
print(nome_removido)