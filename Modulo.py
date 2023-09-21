import customtkinter as tk

def CriarJanelaP(Titulo,Tamanho,Tipo,Redimensionar=False):
    if Tipo ==1:
        janela = tk.CTk()
    elif Tipo ==2:
        janela = tk.CTkToplevel()
    elif Tipo ==3:
        janela = tk.CTkInputDialog()
    janela.title(Titulo)
    janela.geometry(Tamanho)
    if Redimensionar !=False:
        janela.resizable(width=True, height=True)
    else:
        janela.resizable(width=False, height=False)
    colunas = list(range(13))
    linhas = list(range(13))
    janela.grid_columnconfigure(colunas, weight=1)
    janela.grid_rowconfigure(linhas, weight=1)
    return janela

def CriarLabel(Local,Texto,Linha,Coluna):
    label = tk.CTkLabel(Local,text=Texto)
    label.grid(row=Linha, column = Coluna)
    return label

def CriarCaixaTexto(Local,Largura,Altura,Linha,Coluna,Texto="nada"):
    caixa = tk.CTkEntry(Local,width=Largura,height=Altura)
    caixa.grid(row=Linha, column=Coluna)
    if Texto!="nada":
        caixa.configure(placeholder_text=Texto)
    return caixa

def CriarBotao(Local,Texto,Comando,Largura,Altura,Linha,Coluna):
    btn = tk.CTkButton(Local,text=Texto,command=Comando,width=Largura,height=Altura)
    btn.grid(row=Linha,column=Coluna)
    return btn

def CriarCheckBox(Local,Texto,Linha,Coluna):
    check1 = tk.CTkCheckBox(Local, text=Texto)
    check1.grid(row=Linha, column=Coluna)
    return check1

def CriarSwitch (Local,Texto,Linha,Coluna):
    switch = tk.CTkSwitch(Local, text=Texto)
    switch.grid(row=Linha, column=Coluna)


def CriarComboBox(Local,Valores,Largura,Altura,Linha,Coluna):
    combo = tk.CTkComboBox(Local, width=Largura, height=Altura, values=Valores, state="readonly")
    combo.grid(row=Linha, column=Coluna)
    combo.set("Selecione")
    return combo

def CriarProgressBar(Local,Largura,Altura,Linha,Coluna):
    progress = tk.CTkProgressBar(Local, width=Largura, height=Altura)
    progress.grid(row=Linha, column=Coluna)
    progress.set(0)

def CriarSlider(Local,Largura,Altura,Linha,Coluna):
    slider = tk.CTkSlider(Local, width=Largura, height=Altura)
    slider.grid(row=Linha, column=Coluna)
    slider.get()