import datetime, time, porcentagem

at = (datetime.date.today(), datetime.date.today().year) #tupla com a importação datetime
d = {}
l = []
print(at[0]) #programa principal
print('Me chamo Isadora. Em que posso ajudar?')
x = int(input('Quantos cadastro de compra '))
for x in range (0,x):#ciclo de repetição determinada em quantos ciclos de repetição o usuário quer realizar
    print('='*50)
    d['Nome'] = input('Nome: ')
    d['Ano de nascimento'] = int(input('Nascimento '))
    id = at[1] - d['Ano de nascimento']
    print('Idade {} anos'.format(id))
    d['Sexo'] = input('Sexo ').strip().upper()[0]
    while d['Sexo'] not in 'MmFf':#ciclo de repetição que  irá validar o sexo
        print('Digite novamente')
        d['Sexo'] = input('Sexo ').strip().upper()[0]
    print(f'{d["Nome"]}, {id} anos, sexo {d["Sexo"]}')
    d['Valor'] = float(input('Sua compra ficou em R$ '))
    print('Processando....')
    time.sleep(0.5)
    print('='*50)
    print("""Forma de pagamento\n[0] a vista no  dinheiro/ débito\n[1] a vista no cartão crédito
[2] 2 vezes\n[3] 3 vezes\n[4] 4 vezes\n[5] 5 vezes - OBS:. até R$ 1.500.00\n[6] 6 vezes
[7] 7 vezes - OBS:. até R$ 3.000.00\n[8] 8 vezes\n[9] 9 vezes\n[10] 10 vezes - OBS:. de R$ 5.500.00 """)
    op = int(input('Qual opção ?'))
    if op == 0:porcentagem.desconto(d['Valor'], 90, 100)
    elif op == 1:porcentagem.desconto(d['Valor'], 95, 100)
    elif op == 2:porcentagem.acrescimoparcelado(d['Valor'], 100, 100, 2)
    elif op == 3:porcentagem.acrescimoparcelado(d['Valor'], 110, 100, 3)
    elif op == 4:porcentagem.acrescimoparcelado( d['Valor'] , 115, 100, 4)
    elif op == 5 and d['Valor'] >= 1500.00:porcentagem.acrescimoparcelado(d['Valor'], 120, 100, 5)
    elif op == 6:porcentagem.acrescimoparcelado(d['Valor'], 125, 100, 6)
    elif op == 7 and d['Valor'] >= 3000.00:porcentagem.acrescimoparcelado(d['Valor'], 130, 100, 7)
    elif op == 8:porcentagem.acrescimoparcelado(d['Valor'], 135, 100, 8)
    elif op == 9:porcentagem.acrescimoparcelado(d['Valor'], 140, 100, 9)
    elif op == 10 and d['Valor'] >= 5500.00:porcentagem.acrescimoparcelado(d['Valor'], 145, 100, 10)
    else:
        print('Opção Inoperante')
    l.append(d.copy())
    d.clear()
    time.sleep(0.5)
    print('Processando....')
print('Obrigado pela sua visita em nossa loja. Tenha um ótimo dia s2')
print('Aguardamos sua próxima visita a nossa loja ')
print('Próximo cadastro....')
print('='*50)
time.sleep(0.5)
print(l)

