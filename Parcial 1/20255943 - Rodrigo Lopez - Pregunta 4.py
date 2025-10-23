pl = input()

# Verificando si la palabra "pl" es palindroma
print(pl.lower() == pl.lower()[::-1])