class ListaDeConvidados():
  
  def __init__(self):
    self.convidados = [[], []]   
    self.men = {}
    self.women = {}

  def add_guest(self):
    INSERT = True
    while INSERT:
      guest = str(input('Insert Name: '))
      man_or_woman = str(input('for woman or man press (w/m)?: '))
    
      if man_or_woman == 'm':
        self.men[guest] = 'confirmado'
      else:
        self.women[guest] = 'confirmado'
    
      exit = input('Press (s) to Exit: ')
      if exit == 's': INSERT = False
  
    for key in self.men.keys(): self.convidados[0].append(key)
    for key in self.women.keys(): self.convidados[1].append(key)

  def show_all_guests(self):
    print([item for value in self.convidados for item in value])

  def show_men_guests(self):
    for key in range(len(self.men.keys())):
      print(f'{key} -> {self.convidados[0][key]}')

  def show_women_guests(self):
    for key in range(len(self.women.keys())):
      print(f'{key} -> {self.convidados[1][key]}')
