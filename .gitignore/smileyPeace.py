from tkinter import Tk,Label,PhotoImage,BOTTOM,LEFT,RIGHT,RIDGE
# GUI ilustra opções de construtor de widget e método pack()
raiz = Tk()
# label com texto "A paz começa com um sorriso.
texto = Label(raiz,
            font = ('Helvetica', 16, 'bold italic'),
            foreground='white',   # cor da letra
            background='black',   # cor do fundo
            padx=25,  # expande label 25 pixels para esquerda e direita
            pady=10,  # amplia label 10 pixels acima e abaixo
            text='A paz começa com um sorriso.')
texto.pack(side=BOTTOM)              # empurra label para baixo
# label com imagem de símbolo da paz
peace = PhotoImage(file='peace.png')
peaceLabel = Label(raiz,
                   borderwidth=3, # largura da borda do label
                   relief=RIDGE,  # estilo da borda do label
                   image=peace)
peaceLabel.pack(side=LEFT)           # empurra label para esquerda
# label com imagem da carinha sorridente
smiley = PhotoImage(file='smiley.png')
smileyLabel = Label(raiz,
                   image=smiley)
smileyLabel.pack(side=RIGHT)         # empurra label para direita
raiz.mainloop()