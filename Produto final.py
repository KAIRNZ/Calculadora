import tkinter as tk
from math import sqrt

# Paleta de cores moderna
COR_FUNDO = "#F5F5F5"          # Fundo branco suave
COR_TECLAS = "#FFFFFF"         # Teclas brancas
COR_TECLAS_OPER = "#4285F4"    # Azul Google (operações)
COR_TEXTO = "#333333"          # Texto cinza escuro
COR_TEXTO_OPER = "#FFFFFF"     # Texto branco para botões coloridos
COR_DESTAQUE = "#EA4335"       # Vermelho Google (limpar)
COR_SECUNDARIA = "#34A853"     # Verde Google (porcentagem/raiz)

def adicionar():
    try:
        resultado = float(entrada1.get()) + float(entrada2.get())
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def subtrair():
    try:
        resultado = float(entrada1.get()) - float(entrada2.get())
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def multiplicar():
    try:
        resultado = float(entrada1.get()) * float(entrada2.get())
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def dividir():
    try:
        resultado = float(entrada1.get()) / float(entrada2.get())
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def raiz_quadrada():
    try:
        numero = float(entrada1.get())
        resultado = sqrt(numero)
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def porcentagem():
    try:
        numero = float(entrada1.get())
        resultado = numero / 100
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def inserir_numero(numero):
    if janela.focus_get() == entrada1:
        entrada1.insert(tk.END, str(numero))
    elif janela.focus_get() == entrada2:
        entrada2.insert(tk.END, str(numero))

def limpar_tudo():
    entrada1.delete(0, tk.END)
    entrada2.delete(0, tk.END)
    resultado_label.config(text="Resultado:", fg=COR_TEXTO)

def apagar_digito():
    if janela.focus_get() == entrada1:
        posicao = entrada1.index(tk.INSERT)
        if posicao > 0:
            entrada1.delete(posicao-1)
    elif janela.focus_get() == entrada2:
        posicao = entrada2.index(tk.INSERT)
        if posicao > 0:
            entrada2.delete(posicao-1)

# Configuração da janela
janela = tk.Tk()
janela.title("Calculadora!")
janela.configure(bg=COR_FUNDO)
janela.geometry("320x500")

# Estilos
estilo_botao = {
    'width': 6,'height': 2,'font': ('Arial', 12),'borderwidth': 0,'relief': 'flat','bg': COR_TECLAS,'fg': COR_TEXTO,'activebackground': "#EEEEEE"
}

estilo_operacao = {
    'width': 6,'height': 2,'font': ('Arial', 12),'borderwidth': 0,'relief': 'flat','bg': COR_TECLAS_OPER,'fg': COR_TEXTO_OPER,'activebackground': "#3367D6"
}

estilo_especial = {
    'width': 6,'height': 2,'font': ('Arial', 12),'borderwidth': 0,'relief': 'flat','bg': COR_SECUNDARIA,'fg': COR_TEXTO_OPER,'activebackground': "#2D9144"
}

estilo_limpar = {
    'width': 6,'height': 2,'font': ('Arial', 12),'borderwidth': 0,'relief': 'flat','bg': COR_DESTAQUE,'fg': COR_TEXTO_OPER,'activebackground': "#D33426"
}

# Campos de entrada
frame_entradas = tk.Frame(janela, bg=COR_FUNDO)
frame_entradas.pack(pady=15)

tk.Label(frame_entradas, text="Número 1:", bg=COR_FUNDO, fg=COR_TEXTO, font=('Arial', 10)).grid(row=0, column=0, padx=5)
entrada1 = tk.Entry(frame_entradas, bg=COR_TECLAS, fg=COR_TEXTO, font=('Arial', 12), 
                   insertbackground=COR_TEXTO, borderwidth=1, relief='solid')
entrada1.grid(row=0, column=1, padx=5, ipady=5)

tk.Label(frame_entradas, text="Número 2:", bg=COR_FUNDO, fg=COR_TEXTO, font=('Arial', 10)).grid(row=1, column=0, padx=5)
entrada2 = tk.Entry(frame_entradas, bg=COR_TECLAS, fg=COR_TEXTO, font=('Arial', 12),
                   insertbackground=COR_TEXTO, borderwidth=1, relief='solid')
entrada2.grid(row=1, column=1, padx=5, ipady=5)

# Frame para botões de operações
frame_operacoes = tk.Frame(janela, bg=COR_FUNDO)
frame_operacoes.pack(pady=10)

# Primeira linha de operações
tk.Button(frame_operacoes, text="+", command=adicionar, **estilo_operacao).grid(row=0, column=0, padx=3, pady=3)
tk.Button(frame_operacoes, text="-", command=subtrair, **estilo_operacao).grid(row=0, column=1, padx=3, pady=3)
tk.Button(frame_operacoes, text="×", command=multiplicar, **estilo_operacao).grid(row=0, column=2, padx=3, pady=3)
tk.Button(frame_operacoes, text="÷", command=dividir, **estilo_operacao).grid(row=0, column=3, padx=3, pady=3)

# Segunda linha de operações
tk.Button(frame_operacoes, text="√", command=raiz_quadrada, **estilo_especial).grid(row=1, column=0, padx=3, pady=3)
tk.Button(frame_operacoes, text="%", command=porcentagem, **estilo_especial).grid(row=1, column=1, padx=3, pady=3)
tk.Button(frame_operacoes, text="C", command=limpar_tudo, **estilo_limpar).grid(row=1, column=2, padx=3, pady=3)
tk.Button(frame_operacoes, text="⌫", command=apagar_digito, **estilo_botao).grid(row=1, column=3, padx=3, pady=3)

# Frame para botões numéricos
frame_numeros = tk.Frame(janela, bg=COR_FUNDO)
frame_numeros.pack(pady=10)

# Botões de 1-9
for i in range(1, 10):
    tk.Button(frame_numeros, text=str(i), command=lambda i=i: inserir_numero(i), **estilo_botao).grid(
        row=(i-1)//3, column=(i-1)%3, padx=3, pady=3)

# Botão 0
tk.Button(frame_numeros, text="0", command=lambda: inserir_numero(0), width=12, height=2,**{k:v for k,v in estilo_botao.items() if k not in ['width', 'height']}
          ).grid(row=3, column=0, columnspan=2, padx=3, pady=3, sticky="we")

# Botão . (ponto decimal)
tk.Button(frame_numeros, text=".", command=lambda: inserir_numero('.'), **estilo_botao).grid(
    row=3, column=2, padx=3, pady=3)

# Label de resultado
resultado_label = tk.Label(janela, text="Resultado:", bg=COR_FUNDO, fg=COR_TEXTO, font=('Arial', 14))
resultado_label.pack(pady=5)

janela.mainloop()