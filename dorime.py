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

nome = input('Seu nome: ').strip().lower()
nome_dorime = ''.join([letras.get(x) for x in list(nome)])
print(f'Seu nome em Dorime: {nome_dorime}')
