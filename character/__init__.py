import numeros


def char(char):
    while True:
        try:
            char = input(char)
        except (KeyboardInterrupt):
            print('\n\033[31mInterrompido pelo usuário\033[m')
            break
        else:
            return char

def line():
    print('='*50)


def menu(msg):
    print(msg)


def items(opcao):
    menu('Forma de pagamento')
    c=0
    for item in opcao:
        print(f'[{c}] {item}')
        c+=1
    op = numeros.leiaint('Opção desejada ')
    return op