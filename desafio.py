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

# 3. Encontre a substring palindroma mais longa na sring abaixo:
# A ideia é buscar pelo menos 3 caracteres em toda string e verificar se é uma palavra palindroma, caso não encontre com 3, aumenta para 4 e assim por diante

palavra_desafio_3 = 'babad'
quantidade_caracteres = len(palavra_desafio_3)
encontrado = False
for i in range(3, quantidade_caracteres, 1):
    if encontrado == True:
        break
    
    for j in range(0, quantidade_caracteres, 1):
        teste_palavra_3_caracteres = palavra_desafio_3[j:i]
        
        if teste_palavra_3_caracteres == teste_palavra_3_caracteres[::-1]:
            solucao_desafio_3 = teste_palavra_3_caracteres
            print(solucao_desafio_3)
            encontrado = True
            break
        
        i = i+1
        
# 4. Coloque em maiúscula a primeira letra de cada frase na string:
frase_desafio_4 = "hello. how are you? i'm fine, thank you."
caracteres_maiusculo = ['.', '?', '!']
lista_palavras_desafio_4 = frase_desafio_4.split()
lista_palavras_desafio_4_solucionada = []


for index, palavra in enumerate(lista_palavras_desafio_4):
    if index == 0:
        lista_palavras_desafio_4_solucionada.append(palavra.capitalize())
        continue
    
    palavra_anterior = lista_palavras_desafio_4[index-1]
    ultimo_caracter_palavra_anterior = palavra_anterior[-1]
    
    if ultimo_caracter_palavra_anterior in caracteres_maiusculo:
        lista_palavras_desafio_4_solucionada.append(palavra.capitalize())
    else:
        lista_palavras_desafio_4_solucionada.append(palavra)
        
solucao_desafio_4 = ' '.join(lista_palavras_desafio_4_solucionada)
print(solucao_desafio_4)


# 5. Verifique se a string é um anagrama de um palíndromo:
palavra_desafio_5 = 'racecar'
lista_letras_desafio_5_invertido = []

for letra in palavra_desafio_5:
    lista_letras_desafio_5_invertido.insert(0, letra)

palavra_invertida_desafio_5 = ''.join(lista_letras_desafio_5_invertido)

if palavra_desafio_5 == palavra_invertida_desafio_5:
    solucao_desafio_5 = True
else:
    solucao_desafio_5 = False
    
print(solucao_desafio_5)