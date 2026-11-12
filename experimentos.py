import json
import time
from pathlib import Path
from statistics import median

from indice_invertido import construir_indice, buscar, separar_palavras, preparar_palavra


FRASES = [
    "Python é utilizado no estudo de estruturas de dados.",
    "O algoritmo percorre a lista e encontra os elementos.",
    "Dicionários permitem buscar dados por uma chave.",
    "A tabela hash organiza informações para consulta.",
    "Conjuntos não guardam elementos repetidos.",
    "O programa realiza buscas em linhas de texto.",
    "A linguagem Python possui recursos para programação.",
    "Os estudantes estudam algoritmos e estruturas.",
    "Uma busca indexada utiliza um dicionário.",
    "O teste compara tempo de execução das consultas.",
    "A análise de desempenho utiliza medições repetidas.",
    "Cada palavra pode aparecer em diferentes linhas.",
]
PALAVRAS = ["python", "dados", "algoritmo", "estruturas", "programação",
            "conjuntos", "hash", "estudantes", "análise", "inexistente"]


def buscar_varredura(linhas, palavra):
    palavra = preparar_palavra(palavra)
    encontradas = []
    for numero, linha in enumerate(linhas, 1):
        if palavra in separar_palavras(linha):
            encontradas.append(numero)
    return encontradas


def medir(texto, linhas, consultas):
    inicio = time.perf_counter()
    indice = construir_indice(texto)
    tempo_construcao = (time.perf_counter() - inicio) * 1000

    inicio = time.perf_counter()
    for palavra in consultas:
        buscar_varredura(linhas, palavra)
    tempo_varredura = (time.perf_counter() - inicio) * 1000

    inicio = time.perf_counter()
    for palavra in consultas:
        buscar(indice, palavra)
    tempo_indice = (time.perf_counter() - inicio) * 1000

    return [tempo_construcao, tempo_varredura, tempo_indice]


def main():
    texto = "\n".join(FRASES * 300)  # 3.600 linhas
    linhas = texto.splitlines()
    consultas = PALAVRAS * 100  # 1.000 consultas

    indice = construir_indice(texto)
    for palavra in PALAVRAS:
        assert buscar_varredura(linhas, palavra) == buscar(indice, palavra)

    resultados = {}
    for quantidade in (1, 2, 10, 100, 1000):
        tempos = [medir(texto, linhas, consultas[:quantidade]) for _ in range(3)]
        construcao = median(t[0] for t in tempos)
        varredura = median(t[1] for t in tempos)
        buscas_indice = median(t[2] for t in tempos)
        # Mediana do custo total obtido em cada repetição.
        total_indice = median(t[0] + t[2] for t in tempos)
        resultados[str(quantidade)] = {
            "construcao_ms": round(construcao, 3),
            "varredura_ms": round(varredura, 3),
            "buscas_indice_ms": round(buscas_indice, 3),
            "construcao_e_buscas_ms": round(total_indice, 3),
        }
        print(quantidade, "consultas:", round(varredura, 2), "ms (varredura) /",
              round(total_indice, 2), "ms (índice + construção)")

    dados = {"linhas": len(linhas), "repeticoes": 3,
             "consultas_base": PALAVRAS, "resultados": resultados}
    Path(__file__).with_name("resultados.json").write_text(
        json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
