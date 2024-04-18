# Filter
notas = [9.1, 8, 1, 5, 7, 10, 7.5]


def pessoas_aprovadas(notas):
    if notas >= 6:
        return True
    else:
        return False


aprovados = list(map(pessoas_aprovadas, notas))

print(*aprovados)