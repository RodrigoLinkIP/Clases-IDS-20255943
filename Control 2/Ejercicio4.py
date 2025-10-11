prom = 0
por = [0.15, 0.4, 0.25, 0.20, 0.05]
for i in range(0, 5):
    n = float(input())
    prom += n * por[i]
print(f"La nota final es: {prom:.2f}")
