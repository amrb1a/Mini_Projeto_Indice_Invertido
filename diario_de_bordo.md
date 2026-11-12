# Diário de bordo – Perguntas feitas à IA

**1. Como faço para numerar as linhas começando do 1?**

**Resposta da IA:** Dá para usar enumerate(texto.splitlines(), 1). Assim o for percorre as linhas e já entrega o número de cada uma.

**2. Se tiver uma linha em branco, ela conta também?**

**Resposta da IA:** Sim. Mesmo sem guardar nenhuma palavra daquela linha, o número dela precisa ser considerado. Não pode apagar as linhas vazias antes da contagem.

**3. Qual é o jeito mais fácil de não diferenciar Python de PYTHON?**

**Resposta da IA:** Transforme as letras em minúsculas antes de guardar e antes de pesquisar. O método lower() resolve essa parte.

**4. Como tirar vírgulas e pontos sem perder as letras com acento?**

**Resposta da IA:** Uma opção é usar re.findall para separar só as palavras, ignorando a pontuação e mantendo as letras acentuadas.

**Aplicação no código:** Para separar as palavras, usamos `isalnum()` dentro da função `separar_palavras`, sem precisar de `re.findall()`. Também usamos `unicodedata.normalize("NFC", ...)` para tratar corretamente formas diferentes de escrever a mesma letra acentuada.

**5. Quando encontro uma palavra nova, como coloco ela no dicionário?**

**Resposta da IA:** Primeiro veja se a palavra já existe. Se não existir, crie um set vazio para ela. Depois coloque o número da linha nesse conjunto.

**6. Se a palavra aparecer duas vezes na mesma linha, vai repetir o número?**

**Resposta da IA:** Não. O método add() coloca o valor no conjunto, mas set não guarda dois valores iguais.

**7. Na busca simples, como faço para não dar erro com uma palavra inexistente?**

**Resposta da IA:** Use indice.get(palavra, set()). Se não encontrar a palavra, o resultado é um conjunto vazio e a função devolve uma lista vazia.

**8. Por que colocar sorted() no resultado da busca?**

**Resposta da IA:** Porque os valores ficam guardados em conjuntos, que não garantem a ordem. sorted() devolve os números das linhas em ordem crescente.

**9. Como fazer a busca E funcionar com duas ou mais palavras?**

**Resposta da IA:** Comece pelas linhas da primeira palavra e faça uma interseção (&) com as linhas de cada palavra seguinte. Assim só ficam as linhas que aparecem em todas.

**10. E a busca OU? O código é parecido?**

**Resposta da IA:** É parecido, mas começa com set() vazio e usa união (|). Desse jeito entram as linhas de qualquer uma das palavras.

**11. Como faço a busca E sem mexer no conjunto que está no dicionário?**

**Resposta da IA:** Use copy() no primeiro conjunto antes de começar a combinar as linhas. Depois a interseção fica no resultado da busca, não no índice original.

**12. Se uma palavra não existe, o que acontece na busca E e na OU?**

**Resposta da IA:** Na busca E, o resultado fica vazio, porque aquela palavra não tem linhas. Na busca OU, as outras palavras ainda podem encontrar linhas.

**13. No menu, como separar as palavras digitadas para mandar às funções?**

**Resposta da IA:** Você pode usar input().split(). Isso separa a entrada pelos espaços. Depois, confira se a busca simples recebeu uma palavra e se E/OU receberam pelo menos duas.

**14. Como comparar com uma busca que não usa o índice?**

**Resposta da IA:** Faça outra função que percorra as linhas e procure a palavra em cada uma delas. Rode as mesmas consultas nas duas formas de busca para comparar de maneira justa.

**15. Como medir os tempos sem contar a leitura do arquivo?**

**Resposta da IA:** Use time.perf_counter() antes e depois de cada parte. Meça a construção e as buscas separadas, repita três vezes e use a mediana. Para comparar o custo completo do índice, some construção e buscas.

## Verificação das orientações

Conferimos as funções com `python testes.py`, incluindo os casos de pontuação, acentos, palavras repetidas, linhas vazias e busca E/OU com palavras inexistentes. No experimento, o programa compara as mesmas consultas por varredura e pelo índice, com três medições para cada quantidade, registrando a mediana em `resultados.json`.
