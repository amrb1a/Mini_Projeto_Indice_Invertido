import unicodedata


def separar_palavras(texto):
    texto = unicodedata.normalize("NFC", texto.lower())
    palavras = []
    palavra = ""

    for letra in texto:
        if letra.isalnum():
            palavra += letra
        elif palavra:
            palavras.append(palavra)
            palavra = ""

    if palavra:
        palavras.append(palavra)
    return palavras


def preparar_palavra(palavra):
    palavras = separar_palavras(palavra)
    if len(palavras) == 1:
        return palavras[0]
    return ""


def construir_indice(texto):
    indice = {}
    for numero, linha in enumerate(texto.splitlines(), 1):
        for palavra in separar_palavras(linha):
            if palavra not in indice:
                indice[palavra] = set()
            indice[palavra].add(numero)
    return indice


def buscar(indice, palavra):
    palavra = preparar_palavra(palavra)
    return sorted(indice.get(palavra, set()))


def buscar_e(indice, palavras):
    if not palavras:
        return []

    resultado = None
    for palavra in palavras:
        palavra = preparar_palavra(palavra)
        linhas = indice.get(palavra, set())
        if resultado is None:
            resultado = linhas.copy()
        else:
            resultado = resultado & linhas

    return sorted(resultado)


def buscar_ou(indice, palavras):
    resultado = set()
    for palavra in palavras:
        palavra = preparar_palavra(palavra)
        linhas = indice.get(palavra, set())
        resultado = resultado | linhas
    return sorted(resultado)
