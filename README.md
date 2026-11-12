# Mini-projeto de Estruturas de Dados – Índice invertido

**IFAL – Campus Maceió**  
**Curso:** Sistemas de Informação  
**Professor:** Ricardo Nunes  
**Integrantes:** Gabriel França e Alicia Barros

## O que o programa faz

O programa lê um texto e guarda em quais linhas cada palavra aparece. Depois, dá para pesquisar uma palavra ou combinar várias palavras com E (todas devem aparecer) e OU (pelo menos uma deve aparecer).

O índice é um dicionário: a chave é a palavra e o valor é um conjunto com os números das linhas. As buscas devolvem listas em ordem crescente.

## Arquivos do projeto

- `indice_invertido.py` – quatro funções pedidas no enunciado.
- `programa.py` – menu para fazer buscas.
- `texto_exemplo.txt` – texto para testar o menu.
- `testes.py` – sete grupos de testes com assert.
- `experimentos.py` – comparação com uma busca por varredura.
- `resultados.json` – resultados das medições feitas.
- `relatorio.pdf` – capa, descrição do projeto, tabelas e análise dos experimentos.
- `relatorio.docx` – versão editável do relatório.
- `diario_de_bordo.md` – perguntas e respostas sobre o código.

## Como executar

É preciso ter Python 3 instalado. Não é necessário instalar pacotes extras.

Abra o terminal na pasta do projeto e execute:

```bash
python programa.py
```

No Windows, se `python` não funcionar, experimente `py programa.py`.

O menu tem quatro opções: 1 (uma palavra), 2 (E), 3 (OU) e 0 (sair). Para consultar outro arquivo de texto, salve esse arquivo em UTF-8 e use:

```bash
python programa.py meu_texto.txt
```

Para conferir as funções, execute:

```bash
python testes.py
```

Para refazer a comparação dos tempos, execute:

```bash
python experimentos.py
```

Esse último comando gera outro `resultados.json`. Os tempos dependem do computador. Foram usadas 3.600 linhas, as mesmas palavras nas duas buscas e três execuções em cada quantidade (1, 2, 10, 100 e 1.000 buscas). O resultado apresentado é a mediana.


## Repositório do projeto

O mini-projeto foi desenvolvido para a disciplina de
Estruturas de Dados do IFAL – Campus Maceió.

O código-fonte, os testes, os experimentos e o relatório
estão disponíveis neste repositório.

## Atualizações do projeto

As alterações são registradas utilizando Git e GitHub.

O histórico de commits permite acompanhar as correções
e melhorias feitas no projeto.

O programa pode ser executado pelo VS Code ou pelo
terminal, desde que o Python 3 esteja instalado.
  
