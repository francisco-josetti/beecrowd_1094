n = int(input())
c = 0
r = 0
s = 0
for i in range(n):
    n2 = input()
    lista = n2.split()
    if lista[1] == 'C':
        c = c + int(lista[0])
    if lista[1] == 'R':
        r = r + int(lista[0])
    if lista[1] == 'S':
        s = s + int(lista[0])
print(f'Total: {c + r + s} cobaias')
print(f'Total de coelhos: {c}')
print(f'Total de ratos: {r}')
print(f'Total de sapos: {s}')
print(f'Percentual de coelhos: {(c / (c + r + s)) * 100:.2f} %')
print(f'Percentual de ratos: {(r / (c + r + s)) * 100:.2f} %')
print(f'Percentual de sapos: {(s / (c + r + s)) * 100:.2f} %')
