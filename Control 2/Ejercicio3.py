c = input()
cc = c.count("@") == 1
print(f"Contiene exactamente un @: {cc}")
cc = c[0] != "@"
print(f"El @ no está ubicado al inicio del correo: {cc}")
cc = c[-1] != "@"
print(f"El @ no está ubicado al final del correo: {cc}")