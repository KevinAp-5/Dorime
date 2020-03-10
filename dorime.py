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
newname = [x for x in name]  # Add as letras do nome em uma lista

for x in range(0, len(name)):
    if name[x] != ' ':  # substitui a letra atual pela caractere do dicionario
        newname[x] = newname[x].replace(name[x], letras[name[x]])

newname = ''.join(newname)  # Junta todos os intens da lista em uma string
print(f"Seu nome: {name}\nSeu nome em Dorime: {newname}")
