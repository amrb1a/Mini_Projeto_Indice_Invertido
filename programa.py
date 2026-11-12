from pathlib import Path
import sys

from indice_invertido import construir_indice, buscar, buscar_e, buscar_ou


def main():
    if len(sys.argv) > 1:
        arquivo = Path(sys.argv[1])
    else:
        arquivo = Path(__file__).with_name("texto_exemplo.txt")

    try:
        texto = arquivo.read_text(encoding="utf-8")
    except OSError:
        print("Não foi possível abrir o arquivo de texto.")
        return

    indice = construir_indice(texto)
    print("Arquivo:", arquivo.name)

    while True:
        print("\n1 - Buscar uma palavra")
        print("2 - Buscar com E")
        print("3 - Buscar com OU")
        print("0 - Sair")
        opcao = input("Escolha: ").strip()

        if opcao == "0":
            break
        if opcao not in ("1", "2", "3"):
            print("Opção inválida.")
            continue

        palavras = input("Digite as palavras separadas por espaço: ").split()
        if opcao == "1":
            if len(palavras) != 1:
                print("Digite somente uma palavra.")
                continue
            linhas = buscar(indice, palavras[0])
        else:
            if len(palavras) < 2:
                print("Digite duas ou mais palavras.")
                continue
            if opcao == "2":
                linhas = buscar_e(indice, palavras)
            else:
                linhas = buscar_ou(indice, palavras)

        print("Linhas encontradas:", linhas)


if __name__ == "__main__":
    main()
