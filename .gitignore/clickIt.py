from tkinter import Tk, Button
from time import strftime, localtime
from tkinter.messagebox import showinfo
def clicked():
    'exibe informação de dia e hora'
    time = strftime('Dia: %d %b %Y\nHora: %H:%M:%S %p\n',localtime())
    showinfo(message=time)
raiz = Tk()
# cria botão rotulado com ‘Clique aqui’ e manipulador de evento clicked()
button = Button(raiz,
                text='Clique aqui',     # texto do botão
                command=clicked)     # manipulador do evento clique
button.pack()                         # do botão
raiz.mainloop()