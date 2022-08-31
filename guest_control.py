#programa que cria uma lista com convidados
# 0 -> homem , 1-> mulher
convidados = [[],[]]


def show_guest():
    while True:
        show = str(input('Mostrar todos os convidados ?  [s/n]: '))
        if show == 's':
            print(convidados)
        else:
            showmen = str(input('mostrar convidados homens? [s/n]: '))
            if showmen == 's':
              for c in range(len(convidados[0])):
                print(f'{c} -> {convidados[0][c]}')
            else:
                showwomen = str(input('mostrar convidadas? [s/n]: '))
                if showwomen == 's':
                    for c in range(len(convidados[1])):
                        print(f'{c} -> {convidados[1][c]}')
        exit = input('exit?: ')
        if exit == 's':
            break

def add_guest():
    while True:
        guest = str(input('name: '))
        man_or_woman = str(input('woman or man?: '))
        if man_or_woman == 'woman':
            convidados[1].append(guest)
        else:
            convidados[0].append(guest)
        exit = input('exit?')
        if exit == 's':
            break


add_guest()
show_guest()