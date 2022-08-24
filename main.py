import datetime, time
hj, at = datetime.date.today(), datetime.date.today().year
print(hj)
print('Me chamo Isadora. Em que posso ajudar?')
x = int(input('Quantos cadastro de compra '))
for x in range (0,x):
    print('Processando....')
    time.sleep(0.5)
    print('='*50)
    n = input('Nome: ')
    nasc = int(input('Nascimento '))
    id = at - nasc
    print('Idade {} anos'.format(id))
    s = input('Sexo ').strip().upper()[0]
    while s not in 'MmFf':
        print('Digite novamente')
        s = input('Sexo ').strip().upper()[0]
    print('{}, {} anos, sexo {}'.format(n,id,s))
    v = float(input('Sua compra ficou em R$ '))
    print('Processando....')
    time.sleep(0.5)
    print('='*50)
    print("""Forma de pagamento\n[0] a vista no  dinheiro/ débito\n[1] a vista no cartão crédito
[2] 2 vezes\n[3] 3 vezes\n[4] 4 vezes\n[5] 5 vezes - OBS:. até R$ 1.500.00\n[6] 6 vezes
[7] 7 vezes - OBS:. até R$ 3.000.00\n[8] 8 vezes\n[9] 9 vezes\n[10] 10 vezes - OBS:. de R$ 5.500.00 """)
    op = int(input('Qual opção ?'))
    if op == 0:
        d = v * 90 / 100
        print('A vista no dinheiro ou débito o valor fica R$ {:.0f}'.format(d))
    elif op == 1:
        d = v * 95 / 100
        print('A vista no cartão de crédito fica R$ {:.0f}'.format(d))
    elif op == 2:
        pa = v / 2
        print('O valor parcelado não sofrerá acréscimo ficou R$ {:.0f}'.format(pa))
    elif op == 3:
        ac = v / 115 * 100
        pa = ac / 3
        print('O valor parcelado sofrerá um acréscimo de 15% e ficou R$ {:.0f} '.format(pa))
    elif op == 4:
        ac = v * 115 / 100
        pa = ac / 4
        print('O valor parcelado terá um acréscimo de 15% e ficará no valor de R$ {:.0f}'.format(pa))
    elif op == 5 and v >= 1500.00:
        ac = v * 120 / 100
        pa = ac / 5
        print('Valor parcelado em 5x com acréscimo de 20% no valor de R$ {:.0f}'.format(pa))
    elif op == 6:
        ac = v * 120 / 100
        pa = ac / 6
        print('Valor parcelado em 6x com acréscimo de 20% no valor de R$ {:.0f}'.format(pa))
    elif op == 7 and v >= 3000.00:
        ac = v * 125 / 100
        pa = ac / 7
        print('Valor parcelado em 7x com acréscimo de 25% no valor de R$ {:.0f}'.format(pa))
    elif op == 8:
        ac = v * 125 / 100
        pa = ac / 8
        print('Valor parcelado em 8x com acréscimo de 25% no valor de R$ {:.0ff}'.format(pa))
    elif op == 9:
        ac = v * 130 / 100
        pa = ac / 9
        print('Valor parcelado em 9x com acréscimo de 30% no valor de R$ {:.0f}'.format(pa))
    elif op == 10 and v >= 5500.00:
        ac = v * 130 / 100
        pa = ac / 10
        print('Valor parcelado em 10x com acréscimo de 30% no valor de R$ {:.2f}'.format(pa))
    else:
        print('Opção Inoperante')
        time.sleep(0.5)
    print('Processando....')
print('Obrigado pela sua visita em nossa loja. Tenha um ótimo dia s2')
print('Aguardamos sua próxima visita a nosta loja ')
print('Próximo cadastro....')
print('='*50)
time.sleep(0.5)

