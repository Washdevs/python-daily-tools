def remover_palavras_duplicadas(entrada, saida):
    palavras_unicas = set()
    resultado = []

    with open(entrada, 'r', encoding='utf-8') as file:
        for linha in file:
            palavra = linha.strip()
            if palavra not in palavras_unicas:
                palavras_unicas.add(palavra)
                resultado.append(palavra + '\n')

    with open(saida, 'w', encoding='utf-8') as file:
        file.writelines(resultado)

# Exemplo de uso:
remover_palavras_duplicadas('nomes_tratados.txt', 'nomes_unicos.txt')
