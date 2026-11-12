from indice_invertido import construir_indice, buscar, buscar_e, buscar_ou


# Teste 1: exemplo do enunciado
texto = "Python e dados\nDados e algoritmos\nPython e algoritmos"
indice = construir_indice(texto)
assert indice["python"] == {1, 3}
assert indice["dados"] == {1, 2}
assert indice["algoritmos"] == {2, 3}
assert buscar(indice, "python") == [1, 3]
assert buscar(indice, "java") == []
assert buscar_e(indice, ["python", "dados"]) == [1]
assert buscar_ou(indice, ["python", "dados"]) == [1, 2, 3]

# Teste 2: letras, pontuação e repetições
indice = construir_indice("Python, PYTHON!\n\nDados; python?\n\nPython_python")
assert indice["python"] == {1, 3, 5}
assert buscar(indice, "PYTHON!") == [1, 3, 5]
assert buscar(indice, "dados") == [3]

# Teste 3: acentos diferentes
indice = construir_indice("café e cafe\nCAFÉ\nlogica e lógica")
assert buscar(indice, "café") == [1, 2]
assert buscar(indice, "cafe") == [1]
assert buscar(indice, "lógica") == [3]

# Teste 4: formas diferentes do mesmo acento
indice = construir_indice("cafe\u0301\nCAFÉ")
assert buscar(indice, "café") == [1, 2]

# Teste 5: três palavras e palavra inexistente
indice = construir_indice("python dados algoritmos\npython dados\ndados algoritmos\npython")
assert buscar_e(indice, ["python", "dados", "algoritmos"]) == [1]
assert buscar_ou(indice, ["python", "dados", "algoritmos"]) == [1, 2, 3, 4]
assert buscar_e(indice, ["python", "java"]) == []
assert buscar_ou(indice, ["java", "dados"]) == [1, 2, 3]

# Teste 6: texto vazio
assert construir_indice("") == {}
assert construir_indice("\n\n") == {}
assert buscar(construir_indice(""), "python") == []
assert buscar_e({}, []) == []
assert buscar_ou({}, []) == []

# Teste 7: o índice não pode mudar durante as consultas
indice = construir_indice("python dados\ndados algoritmos\npython")
original = {palavra: linhas.copy() for palavra, linhas in indice.items()}
buscar(indice, "python")
buscar_e(indice, ["python", "dados"])
buscar_ou(indice, ["python", "algoritmos"])
assert indice == original

print("7 grupos de testes passaram.")
