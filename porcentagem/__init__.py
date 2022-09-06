def acrescimoparcelado(v, d, tot, par):
    acresc= v*d/tot
    pac = d - tot
    xs = acresc/par
    print(f'Valor parcelado em {par} vezes terá acréscimo de {pac}% fica em R$ {(float(xs)):.2f}')


def desconto (v, d, total):
    desc= v*d/total
    pdesc = total -d # porcentagem do desconto
    print(f'O valor R$ {(float(v)):.2f} com desconto de {pdesc}% é R$ {(float(desc)):.2f} ')