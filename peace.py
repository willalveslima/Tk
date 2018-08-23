from tkinter import Tk, Label, PhotoImage 
print("App running ...")
raiz = Tk() # a janela 
# transforma GIF em formato que tkinter pode exibir 
foto= PhotoImage(file='peace.png') 
 
peace= Label(master=raiz, 
				image=foto, 
				width=300, # largura do label, em pixels 
				height=180) # altura do label, em pixels 
peace.pack() 
raiz.mainloop()
