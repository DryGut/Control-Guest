from tkinter import *

class App():

  def __init__(self, master=None, child=None):

    self.convidados = [[], []]
    self.men = {}
    self.women = {}

    self.fonte = ("Verdana", "10")
    
    self.master = Frame(master)
    self.master['padx'] = 20
    self.master['pady'] = 15
    self.master.pack()

  def main_layout(self):
  
    self.title = Label(self.master, text='Convidados')
    self.title['pady'] = 5
    self.title['font'] = ('Calibre', '10', 'bold')
    self.title.pack()
  
  def form_layout(self):
    
    self.lblnome = Label(self.master, text='Nome:', font=self.fonte, width=10)
    self.lblnome.pack()
    self.txtnome = Entry(self.master)
    self.txtnome['width'] = 25
    self.txtnome['font'] = self.fonte
    self.txtnome.pack()

    self.lblgenero = Label(self.master, text='Genero:(M/F)', font=self.fonte, width=10)
    self.lblgenero.pack()
    self.txtgenero = Entry(self.master)
    self.txtgenero['width'] = 5
    self.txtgenero['font'] = self.fonte
    self.txtgenero.pack()
    
    
    self.btnInserir = Button(self.master, text='Inserir', font=self.fonte, width=10)
    self.btnInserir['command'] = self.add_guest
    self.btnInserir.pack()
    
    self.btnTodos = Button(self.master, text='Buscar Todos', font=self.fonte, width=10)
    self.btnTodos['command'] = self.show_invited_ppl
    self.btnTodos.pack()

    self.btnMen = Button(self.master, text='Homens Convidados', font=self.fonte, width=15)
    self.btnMen['command'] = self.show_invited_men
    self.btnMen.pack()

    self.btnWomen = Button(self.master, text='Mulheres Convidadas', font=self.fonte, width=15)
    self.btnWomen['command'] = self.show_invited_women
    self.btnWomen.pack()
    
  def add_guest(self):
    
    chave = self.txtnome.get()    #### Gerando entradas duplicadas buscando entender porquê ####
    self.txtnome.delete(0, END)   #### resolver a limpeza do buffer ####
    
    if self.txtgenero.get() == 'm':
      self.men[chave] = 'confirmado'
    
    elif self.txtgenero.get() == 'f':
      self.women[chave] = 'confirmado'

    self.txtgenero.delete(0, END)
    
    for key in self.men.keys(): self.convidados[0].append(key)
    for key in self.women.keys(): self.convidados[1].append(key)
      
  def show_invited_ppl(self):

    top = Toplevel()
    top.title('Convidados')
    top.geometry('350x300')

    label = Label(top, text=' '.join(item for value in self.convidados for item in value))
    label.pack()

  def show_invited_men(self):

    top = Toplevel()
    top.title('Homens Convidados')
    top.geometry('350x300')

    for key in range(len(self.men.keys())):
      label = Label(top, text=f'{key} -> {self.convidados[0][key]}')
      label.pack()

  def show_invited_women(self):

    top = Toplevel()
    top.title('Mulheres Convidados')
    top.geometry('350x300')

    for key in range(len(self.women.keys())):
      label = Label(top, text=f'{key} -> {self.convidados[1][key]}')
      label.pack()


root = Tk()
app = App(root)
root.title("Convidados")
root.geometry('450x290')


menu = Menu(root)
root.config(menu=menu)

filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Open', command=app.form_layout)


filemenu.add_separator()
filemenu.add_command(label='Sair', command=root.quit)

helpmenu = Menu(menu, tearoff=0)
menu.add_cascade(label='Help', menu=helpmenu)
helpmenu.add_command(label='About')


root.mainloop()