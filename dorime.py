letras = {
    'a': 'do', 'b': 'ri', 'c': 'me',
    'd': 'in', 'e': 'te', 'f': 'ri',
    'g': 'mo', 'h': 'ada', 'i': 'pa',
    'j': 're', 'k': 'la', 'l': 'ri',
    'm': 're', 'n': 'la', 'o': 'ti', 
    'p': 're', 'q': 'mo', 'r': 'do',
    's': 'ri', 't': 'me', 'u': 'a',
    'v': 'me', 'w': 'ni', 'x': 'o',
    'y': 'me', 'z': 'nare'
}

name = input('Digite seu nome para o lorde dorime: ').strip().lower()
save_name = name
lista = []

# Vai adicionar as letras do nome separamente em uma lista
for letra in name:
    lista.append(letra)
name = lista  # apenas pra renomear a lista

counter = 0
for letra in name:
    if letra == ' ':  # Basicamente nao muda nada
        name[counter] = name[counter].replace(letra, ' ')
    else:  # Vai substituir a letra do nome pelo valor do abc dorime
        name[counter] = name[counter].replace(letra, letras[letra])
    counter += 1

name = ''.join(name)  # Vai juntar todos os itens da lista em uma string
print(f'Nome antigo: {old_name}\nNovo nome: {name}')
print('ITERIMO ADAPARE!')
