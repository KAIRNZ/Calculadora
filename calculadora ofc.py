from tkinter import *
from tkinter import ttk
from math import *

#cores
cor1 = "#383130" #Cinza
cor2= "#FCFCFC" #Vermelho
cor3= "#A09290" #meio marron
cor4= "#999896" #display

janela= Tk()
janela.title("Calculadora") #titulo
janela.geometry("300x380") #dimensões da calculdora
janela.resizable(False,False) #não deixa o usuario mexer nas dimensões
janela.config(bg=cor1)

#frames
frame_tela= Frame(janela, width=300, height=80, bg=cor4)
frame_tela.grid(row=0, column=0) 

frame_corpo= Frame(janela, width=300, height=300)
frame_corpo.grid(row=1, column=0)


#variavel todos valores 

todos_valores = ''

#criando label
valor_texto = StringVar()

#criando funcao

def entrar_valores(event):
    global todos_valores
    todos_valores= todos_valores + str(event)
    
    
    #passando valor para tela
    valor_texto.set(todos_valores)

#funcao para calcular
def calcular():
    global todos_valores
    resultado = eval(todos_valores)
    valor_texto.set(str(resultado))



def limpar():
    global todos_valores
    todos_valores= ''
    valor_texto.set("")



#tela

app_label= Label(frame_tela, textvariable= valor_texto, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=("Ivy 19 bold"), bg=cor4)
app_label.place(x=50,y=10)

#botões
b_1 = Button(frame_corpo,command= limpar, text="C", width=20, height=3, bg=cor2)
b_1.place(x=0, y=0)
b_2= Button(frame_corpo, command= lambda: entrar_valores("%"), text= "%", width=10, height=3, bg=cor2)
b_2.place(x=140, y=0)
b_3= Button(frame_corpo,command= lambda: entrar_valores("/"), text= "/", width=10, height=3, bg=cor2)
b_3.place(x=220,y=0)
b_4= Button(frame_corpo,command= lambda: entrar_valores("7"), text="7", width=10, height=3, bg=cor3)
b_4.place(x=0.1, y=56.2)
b_5= Button(frame_corpo,command= lambda: entrar_valores("8"), text="8", width=10, height=3, bg=cor3)
b_5.place(x=80.8, y=56.2)
b_6= Button(frame_corpo,command= lambda: entrar_valores("9"), text="9", width=10, height=3, bg=cor3)
b_6.place(x=161.8, y=56.2)
b_7= Button(frame_corpo,command= lambda: entrar_valores("4"),text="4", width=10, height=3, bg=cor3)
b_7.place(x=0.1,y=113)
b_8= Button(frame_corpo,command= lambda: entrar_valores("5"),text="5", width=10, height=3, bg=cor3)
b_8.place(x=80.8,y=113)
b_9= Button(frame_corpo,command= lambda: entrar_valores("6"),text="6", width=10, height=3, bg=cor3)
b_9.place(x=161.8,y=113)
b_10= Button(frame_corpo,command= lambda: entrar_valores("1"),text="1", width=10, height=3, bg=cor3)
b_10.place(x=0.1,y=170)
b_11= Button(frame_corpo,command= lambda: entrar_valores("2"),text="2", width=10, height=3, bg=cor3)
b_11.place(x=80.8,y=170)
b_12= Button(frame_corpo,command= lambda: entrar_valores("3"),text="3", width=10, height=3, bg=cor3)
b_12.place(x=161.8,y=170)
b_13= Button(frame_corpo,command= lambda: entrar_valores("+"), text="+", width=7, height=3, bg=cor2)
b_13.place(x=242,y=56)
b_14= Button(frame_corpo,command= lambda: entrar_valores("-"), text="-", width=7, height=3, bg=cor2)
b_14.place(x=242,y=113)
b_15= Button(frame_corpo,command= lambda: entrar_valores("*"), text="*", width=7, height=3, bg=cor2)
b_15.place(x=242,y=170)
b_16 = Button(frame_corpo,command= lambda: entrar_valores("0"), text="0", width=18, height=4, bg=cor2)
b_16.place(x=3, y=227)  
b_17 = Button(frame_corpo,command=calcular, text="=", width=10, height=4, bg=cor2)
b_17.place(x=219, y=227)
b_17 = Button(frame_corpo,command= lambda: entrar_valores("√"), text="√", width=10, height=4, bg=cor2)
b_17.place(x=139, y=227)





janela.mainloop()