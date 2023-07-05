# 1. Reverta a ordem das palavras nas frases, mantendo a ordem das palavras:
frase_desafio_1 = 'Hello, World! OpenAI is amazing.'

frase_desafio_1_split = frase_desafio_1.split()
lista_palavras_desafio_1 = []
for palavra in frase_desafio_1_split:
    lista_palavras_desafio_1.insert(0, palavra)
    
solucao_desafio_1 = ' '.join(lista_palavras_desafio_1)
print(solucao_desafio_1)