from refatoramento import ListaDeConvidados

lista = ListaDeConvidados()
lista.add_guest()

show = input(" Escolha a Opcao:\n"
             "\n [ t ] - para imprimir todos"
             "\n [ m ] - para imprimir convidados homens"
             "\n [ w ] - para imprimir convidados mulheres"
             "\n Digite sua escolha: ")

mostrar = True

while mostrar:
  if show == 't':
    lista.show_all_guests()
    break
  elif show == 'm':
    lista.show_men_guests()
    break
  elif show == 'w':
    lista.show_women_guests()
    break