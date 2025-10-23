pl = input()
lt = input()

# Verificando si la palabra "pl" contiene la letra "lt"

print(pl.lower().count(lt.lower()) > 0)