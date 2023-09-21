import customtkinter as tk

tk.set_appearance_mode("Dark")
#ligth
#dark
#System

janela= tk.CTk() #instanciando classe para um objeto
#janela principal
janela.title("Janela principal") #propriedade
janela.geometry("400x350")#tamanho
janela.configure(fg_color="DodgerBlue")#muda a cor
janela.resizable(width=False, height=False) #desabilita a mudança de tamanho manual
colunas= list(range(13))
linhas=list(range(13))
janela.grid_columnconfigure(colunas,weight=1)
janela.grid_rowconfigure(linhas,weight=1)

texto1= tk.CTkLabel(janela,text="clicar primeiro")
#primeiro parametro,obrigatorio ser onde vai estar(janela)
texto1.grid(row=6,column=6)

texto2= tk.CTkLabel(janela,text="Você precisa", text_color="White",font=("Arial",18),justify="center")
texto2.grid(row=4,column=6)

def clique():
    texto1.configure(text="Clicou")
    texto2.configure(text="Você já")


bnt1= tk.CTkButton(janela,text="Clique aqui", command=clique,width=50,height=30)
bnt1.grid(row=8,column=6)

caixa1= tk.CTkEntry(janela,placeholder_text="Digite o porque obedeceu",width=200,height=30)
caixa1.grid(row=10,column=6)


janela.mainloop()#repetir infinitamente e ficar na tela
#tudo a cima do cima do main loop