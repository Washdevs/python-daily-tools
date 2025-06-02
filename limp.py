import unicodedata

def limpar_palavra(palavra):
    # Remove acentos
    palavra = ''.join(
        c for c in unicodedata.normalize('NFD', palavra)
        if unicodedata.category(c) != 'Mn'
    )

    # Remove primeiro caractere se não for letra
    if palavra and not palavra[0].isalpha():
        palavra = palavra[1:]

    # Remove último caractere se não for letra
    if palavra and not palavra[-1].isalpha():
        palavra = palavra[:-1]

    return palavra.strip()

def processar_arquivo(entrada, saida):
    with open(entrada, 'r', encoding='utf-8') as f:
        palavras = set(l.strip() for l in f if l.strip())

    palavras_limpas = set()
    for p in palavras:
        limpa = limpar_palavra(p)
        if limpa:  # evita linhas vazias
            palavras_limpas.add(limpa)

    with open(saida, 'w', encoding='utf-8') as f:
        for palavra in sorted(palavras_limpas):
            f.write(palavra + '\n')

# Exemplo de uso
processar_arquivo('nvcompleto.txt', 'limpo.txt')
