from refatoramento import ListaDeConvidados

minha_lista_de_convidados = ListaDeConvidados()
minha_lista_de_convidados.add_guest()

show = input(" Escolha a Opcao:\n"
             "\n [ t ] - para imprimir todos"
             "\n [ m ] - para imprimir convidados homens"
             "\n [ w ] - para imprimir convidados mulheres"
             "\n Digite sua escolha: ")

mostrar = True

while mostrar:
  if show == 't':
    minha_lista_de_convidados.show_all_guests()
    break
  elif show == 'm':
    minha_lista_de_convidados.show_men_guests()
    break
  elif show == 'w':
    minha_lista_de_convidados.show_women_guests()
    break