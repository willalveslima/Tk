from tkinter import Tk, Label, RAISED

raiz = Tk()


	

labels = [['1', '2', '3'],      # textos de label do teclado


	

          ['4', '5', '6'],      # organizados em uma grade


	

          ['7', '8', '9'],


	

          ['*', '0', '#']]


	

 


	

for r in range(4):      # para cada linha r = 0, 1, 2, 3


	

    for c in range(3):      # para cada coluna c = 0, 1, 2


	

        # cria label para linha r e coluna c


	

        label = Label(raiz,


	

                      relief=RAISED,      # borda elevada


	

                      padx=10,            # torna label largo


	

                      text=labels[r][c])  # texto do label


	

        # coloca label na linha r e coluna c


	

        label.grid(row=r, column=c)


	

 


	

raiz.mainloop()