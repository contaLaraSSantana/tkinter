import customtkinter as tk
from Modulo import *

def clique():
    check1.get()
    if check1.get() == 1:
        label1.configure(text='Marcado')
    elif check1.get() == 0:
        label1.configure(text="Desmarcado")


janela=CriarJanelaP("JanelaPrincipal","400x400",1)

label1=CriarLabel(janela," ",5,6)

btn= CriarBotao(janela,"Clique aqui ", Comando=clique, Largura=50, Altura=30, Linha=3,Coluna=6 )
check1=CriarCheckBox(janela,"Clique para marcar",4,6)
check1.get()

switch=CriarSwitch(janela," ",7,6)

Lista= ['1','2','3','4','5']
combo =CriarComboBox(janela,Lista,200,30,8,6)

progress=CriarProgressBar(janela,200,10,10,6)

slider = CriarSlider(janela,200,10,11,6)

janela.mainloop()