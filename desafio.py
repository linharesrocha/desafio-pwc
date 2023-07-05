# 1. Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:
frase_desafio_1 = 'Hello, World! OpenAI is amazing.'

frase_desafio_1_split = frase_desafio_1.split()
lista_palavras_desafio_1 = []
for palavra in frase_desafio_1_split:
    lista_palavras_desafio_1.insert(0, palavra)
    
solucao_desafio_1 = ' '.join(lista_palavras_desafio_1)
print(solucao_desafio_1)

# 2. Remova todos os caracteres duplicados da string abaixo:
frase_desafio_2 = 'Hello, World!'
lista_letras_desafio_2 = []

for letra in frase_desafio_2:
    if letra not in lista_letras_desafio_2:
        lista_letras_desafio_2.append(letra)
        
solucao_desafio_2 = ''.join(lista_letras_desafio_2)
print(solucao_desafio_2)