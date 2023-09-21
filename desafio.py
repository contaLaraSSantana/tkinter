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

texto1= tk.CTkLabel(janela,text="Maior ou menor", text_color="White",font=("Arial",18),justify="center")
texto1.grid(row=4,column=6)

texto2= tk.CTkLabel(janela,text="Insira o primeiro número", text_color="White",font=("Arial",18),justify="center")
texto2.grid(row=5,column=6)
caixa1= tk.CTkEntry(janela,placeholder_text="",width=200,height=30)
caixa1.grid(row=6,column=6)

texto3= tk.CTkLabel(janela,text="Insira o segundo número", text_color="White",font=("Arial",18),justify="center")
texto3.grid(row=7,column=6)
caixa2= tk.CTkEntry(janela,placeholder_text="",width=200,height=30)
caixa2.grid(row=8,column=6)
def clique():
    texto3.configure(text="")
    numero1=int(caixa1.get())
    numero2 = int(caixa2.get())
    if numero1>numero2:
        texto1.configure(text="O maoir número")
        texto2.configure(text=f"é: {numero1}")
    elif numero2>numero1:
        texto1.configure(text="O maior número")
        texto2.configure(text=f"é: {numero2}")
    else:
        texto1.configure(text="Os números são iguais")
        texto2.configure(text="")

bnt1= tk.CTkButton(janela,text="Clique para o resultado", command=clique,width=50,height=30)
bnt1.grid(row=9,column=6)

janela.mainloop()#repetir infinitamente e ficar na tela
#tudo a cima do cima do main loop