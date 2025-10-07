def somar_valores(**kwargs):
    soma = 0
    for valor in kwargs.values():
            soma += valor
    return soma

print(somar_valores(a=1, b=2, c=7, d= 6))

###########################################################################
dicio = {
      "Nicole" : 10,
      "Carlos" : 5
}

print(sum(dicio.values()))


