def remover_segunda_palavra_em_arquivo(entrada, saida):
    with open(entrada, 'r', encoding='utf-8') as file:
        linhas = file.readlines()

    nomes_tratados = []
    for linha in linhas:
        partes = linha.strip().split()
        if len(partes) >= 2:
            nomes_tratados.append(partes[0] + '\n')
        elif len(partes) == 1:
            nomes_tratados.append(partes[0] + '\n')

    with open(saida, 'w', encoding='utf-8') as file:
        file.writelines(nomes_tratados)

# Exemplo de uso:
remover_segunda_palavra_em_arquivo('nvcompleto.txt', 'nomes_tratados.txt')
