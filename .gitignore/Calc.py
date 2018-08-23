from tkinter import Tk, Button, Entry, Label, END,Frame,RAISED,Entry,RIDGE
from math import sqrt 
from time import strptime, strftime
from tkinter.messagebox import showinfo
class Calc(Frame):

	'aplicação que calcula o dia da semana correspondente a uma data'
	def __init__(self, parent=None):
		Frame.__init__(self, parent)
		self.pack()
		self.memory = ''                  # memória
		self.expr = ''                    # expressão atual
		self.startOfNextOperand = True    # início do novo operando
		# rótulos de botão de calculadora em uma lista 2D
		buttons = [['MC',     'M+',      'M-',  'MR'],
           ['C' , '\u221a', 'x\u00b2',  '+' ],
           ['7' ,     '8' ,      '9' ,  '-' ],
           ['4' ,     '5' ,      '6' ,  '*' ],
           ['1' ,     '2' ,      '3' ,  '/' ],
           ['0' ,     '.' ,      '+-',  '=' ]]
		# cria e posiciona botões em linha e coluna apropriadas
		# usa o widget Entry para exibição
		self.entry = Entry(self, relief=RIDGE, borderwidth=3,
						width=20, bg='gray',
						font=('Helvetica', 18))
		self.entry.grid(row=0, column=0, columnspan=5)
		
		# cria e coloca botões na linha e coluna apropriada
		for r in range(6):
			for c in range(4):
				# função cmd() é definida, de modo que, quando chamada
				# sem um argumento de entrada, executa
				# self.click(buttons[r][c])
				def cmd(x=buttons[r][c]):
					self.click(x)
				b = Button(self,       # botão para símbolo buttons[r][c]
                   text=buttons[r][c],
                   width=3,
                   relief=RAISED,
                   command=cmd)           # cmd() é o manipulador
				b.grid(row=r+1, column=c)         # entrada é na linha 0
	def click(self,key):
		'manipulador para evento de pressionar tecla rotulada do botão'
		if key == '=':
			# avalia a expressão, incluindo o valor
			# exibido na entrada e o resultado apresentado
			try:
				result = eval(self.expr + self.entry.get())
				self.entry.delete(0, END)
				self.entry.insert(END, result)
				self.expr = ''
			except:
				self.entry.delete(0, END)
				self.entry.insert(END, 'Error')
		elif key in '+*-/':
			# acrescenta operador exibido na entrada e tecla de operador
			# à expressão e prepara novo operando
			self.expr += self.entry.get()
			self.expr += key
			self.startOfNextOperand = True
			# os casos quando key é '\u221a', 'x\u00b2', 'C',
			# 'M+', 'M-', 'MR', 'MC' são deixados como exercício
		elif key == '+-':
			# troca entrada de positiva para negativa ou vice-versa
			# se não houver valor na entrada, não faz nada
			try:
				if self.entry.get()[0] == '-':
					self.entry.delete(0)
				else:
					self.entry.insert(0, '-')
			except IndexError:
				pass

		elif key == '\u221a':
			# calcula e exibe raiz quadrada da entrada
			result = sqrt(eval(self.entry.get()))
			self.entry.delete(0, END)
			self.entry.insert(END, result)
		elif key == 'x\u00b2':
			# calcula e exibe o quadrado da entrada
			result = eval(self.entry.get())**2
			self.entry.delete(0, END)
			self.entry.insert(END, result)
		elif key == 'C':                # limpa a entrada
			self.entry.delete(0, END)
		elif key in {'M+', 'M-'}:
			# soma ou subtrai da memória o valor da entrada
			self.memory=str(eval('self.memory + key[1] + self.entry.get()'))
		elif key == 'MR':
			# substitui valor na entrada pelo valor armazenado na memória
			self.entry.delete(0, END)
			self.entry.insert(END, self.memory)
		elif key == 'MC':               # apaga a memória
			self.memory = ''
		else:
			# insere dígito ao final da entrada, ou como primeiro
			# dígito, se início do próximo operando
			if self.startOfNextOperand:
				self.entry.delete(0, END)
				self.startOfNextOperand = False
			self.entry.insert(END, key)
def main():
	raiz = Tk()
	calc = Calc(raiz)
	calc.pack()
	raiz.mainloop()
    
if __name__ == "__main__":
    main()