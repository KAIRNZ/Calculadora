"""
CALCULADORA COM INTERFACE GRÁFICA
Código completo com comentários explicativos linha por linha
"""

# Importa a biblioteca tkinter para criar a interface gráfica
import tkinter as tk
# Importa a função sqrt (raiz quadrada) da biblioteca math
from math import sqrt

# ==============================================
# DEFINIÇÃO DAS CORES (PALETA GOOGLE)
# ==============================================
COR_FUNDO = "#F5F5F5"          # Cor de fundo principal (cinza claro)
COR_TECLAS = "#FFFFFF"         # Cor dos botões numéricos (branco)
COR_TECLAS_OPER = "#4285F4"    # Cor dos botões de operação (azul)
COR_TEXTO = "#333333"          # Cor do texto principal (cinza escuro)
COR_TEXTO_OPER = "#FFFFFF"     # Cor do texto nos botões coloridos (branco)
COR_DESTAQUE = "#EA4335"       # Cor de destaque (vermelho - botão limpar)
COR_SECUNDARIA = "#34A853"     # Cor secundária (verde - botões especiais)

# ==============================================
# FUNÇÕES MATEMÁTICAS
# ==============================================

def adicionar():
    """Realiza a soma dos números nas entradas 1 e 2"""
    try:
        # Converte os valores para float e soma
        resultado = float(entrada1.get()) + float(entrada2.get())
        # Atualiza o label com o resultado
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        # Em caso de erro, mostra mensagem em vermelho
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def subtrair():
    """Realiza a subtração do número 1 pelo número 2"""
    try:
        resultado = float(entrada1.get()) - float(entrada2.get())
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def multiplicar():
    """Realiza a multiplicação dos dois números"""
    try:
        resultado = float(entrada1.get()) * float(entrada2.get())
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def dividir():
    """Realiza a divisão do número 1 pelo número 2"""
    try:
        resultado = float(entrada1.get()) / float(entrada2.get())
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def raiz_quadrada():
    """Calcula a raiz quadrada do número na entrada 1"""
    try:
        numero = float(entrada1.get())
        resultado = sqrt(numero)
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

def porcentagem():
    """Converte o número na entrada 1 para porcentagem (divide por 100)"""
    try:
        numero = float(entrada1.get())
        resultado = numero / 100
        resultado_label.config(text=f"Resultado: {resultado}", fg=COR_TEXTO)
    except:
        resultado_label.config(text="Erro!", fg=COR_DESTAQUE)

# ==============================================
# FUNÇÕES DE INTERFACE
# ==============================================

def inserir_numero(numero):
    """Insere um dígito no campo de entrada ativo"""
    # Verifica qual campo está com foco
    if janela.focus_get() == entrada1:
        entrada1.insert(tk.END, str(numero))  # Insere no final do texto
    elif janela.focus_get() == entrada2:
        entrada2.insert(tk.END, str(numero))

def limpar_tudo():
    """Limpa todos os campos de entrada e o resultado"""
    entrada1.delete(0, tk.END)  # Apaga do início ao fim
    entrada2.delete(0, tk.END)
    resultado_label.config(text="Resultado:", fg=COR_TEXTO)  # Reseta o label

def apagar_digito():
    """Remove o último dígito do campo ativo (backspace)"""
    if janela.focus_get() == entrada1:
        posicao = entrada1.index(tk.INSERT)  # Pega posição do cursor
        if posicao > 0:  # Se não estiver no início
            entrada1.delete(posicao-1)  # Apaga caractere anterior
    elif janela.focus_get() == entrada2:
        posicao = entrada2.index(tk.INSERT)
        if posicao > 0:
            entrada2.delete(posicao-1)

# ==============================================
# CONFIGURAÇÃO DA JANELA PRINCIPAL
# ==============================================
janela = tk.Tk()  # Cria a janela principal
janela.title("Calculadora!")  # Define o título
janela.configure(bg=COR_FUNDO)  # Configura cor de fundo
janela.geometry("320x500")  # Define largura x altura

# ==============================================
# ESTILOS DOS BOTÕES (DICIONÁRIOS DE CONFIGURAÇÃO)
# ==============================================

# Estilo base para botões numéricos
estilo_botao = {
    'width': 6,  # Largura em caracteres
    'height': 2,  # Altura em linhas
    'font': ('Arial', 12),  # Fonte e tamanho
    'borderwidth': 0,  # Remove borda
    'relief': 'flat',  # Estilo plano
    'bg': COR_TECLAS,  # Cor de fundo
    'fg': COR_TEXTO,  # Cor do texto
    'activebackground': "#EEEEEE"  # Cor quando pressionado
}

# Estilo para botões de operações (azuis)
estilo_operacao = {
    'width': 6,
    'height': 2,
    'font': ('Arial', 12),
    'borderwidth': 0,
    'relief': 'flat',
    'bg': COR_TECLAS_OPER,  # Azul
    'fg': COR_TEXTO_OPER,  # Texto branco
    'activebackground': "#3367D6"  # Azul mais escuro
}

# Estilo para botões especiais (verdes)
estilo_especial = {
    'width': 6,
    'height': 2,
    'font': ('Arial', 12),
    'borderwidth': 0,
    'relief': 'flat',
    'bg': COR_SECUNDARIA,  # Verde
    'fg': COR_TEXTO_OPER,  # Texto branco
    'activebackground': "#2D9144"  # Verde mais escuro
}

# Estilo para botão de limpar (vermelho)
estilo_limpar = {
    'width': 6,
    'height': 2,
    'font': ('Arial', 12),
    'borderwidth': 0,
    'relief': 'flat',
    'bg': COR_DESTAQUE,  # Vermelho
    'fg': COR_TEXTO_OPER,  # Texto branco
    'activebackground': "#D33426"  # Vermelho mais escuro
}

# ==============================================
# CONSTRUÇÃO DA INTERFACE
# ==============================================

# Frame para os campos de entrada
frame_entradas = tk.Frame(janela, bg=COR_FUNDO)
frame_entradas.pack(pady=15)  # Empacota com espaçamento

# Rótulo e campo para o primeiro número
tk.Label(frame_entradas, 
        text="Número 1:", 
        bg=COR_FUNDO, 
        fg=COR_TEXTO, 
        font=('Arial', 10)
        ).grid(row=0, column=0, padx=5)  # Posiciona na grade

entrada1 = tk.Entry(frame_entradas,  # Campo de entrada
                   bg=COR_TECLAS,  # Cor de fundo
                   fg=COR_TEXTO,  # Cor do texto
                   font=('Arial', 12),  # Fonte
                   insertbackground=COR_TEXTO,  # Cor do cursor
                   borderwidth=1,  # Borda fina
                   relief='solid')  # Estilo da borda
entrada1.grid(row=0, column=1, padx=5, ipady=5)  # ipady = altura interna

# Rótulo e campo para o segundo número
tk.Label(frame_entradas, 
        text="Número 2:", 
        bg=COR_FUNDO, 
        fg=COR_TEXTO, 
        font=('Arial', 10)
        ).grid(row=1, column=0, padx=5)

entrada2 = tk.Entry(frame_entradas, 
                   bg=COR_TECLAS, 
                   fg=COR_TEXTO, 
                   font=('Arial', 12),
                   insertbackground=COR_TEXTO, 
                   borderwidth=1, 
                   relief='solid')
entrada2.grid(row=1, column=1, padx=5, ipady=5)

# Frame para os botões de operações
frame_operacoes = tk.Frame(janela, bg=COR_FUNDO)
frame_operacoes.pack(pady=10)

# Primeira linha de operações (+, -, ×, ÷)
tk.Button(frame_operacoes, text="+", command=adicionar, **estilo_operacao
         ).grid(row=0, column=0, padx=3, pady=3)
tk.Button(frame_operacoes, text="-", command=subtrair, **estilo_operacao
         ).grid(row=0, column=1, padx=3, pady=3)
tk.Button(frame_operacoes, text="×", command=multiplicar, **estilo_operacao
         ).grid(row=0, column=2, padx=3, pady=3)
tk.Button(frame_operacoes, text="÷", command=dividir, **estilo_operacao
         ).grid(row=0, column=3, padx=3, pady=3)

# Segunda linha de operações (√, %, C, ⌫)
tk.Button(frame_operacoes, text="√", command=raiz_quadrada, **estilo_especial
         ).grid(row=1, column=0, padx=3, pady=3)
tk.Button(frame_operacoes, text="%", command=porcentagem, **estilo_especial
         ).grid(row=1, column=1, padx=3, pady=3)
tk.Button(frame_operacoes, text="C", command=limpar_tudo, **estilo_limpar
         ).grid(row=1, column=2, padx=3, pady=3)
tk.Button(frame_operacoes, text="⌫", command=apagar_digito, **estilo_botao
         ).grid(row=1, column=3, padx=3, pady=3)

# Frame para os botões numéricos
frame_numeros = tk.Frame(janela, bg=COR_FUNDO)
frame_numeros.pack(pady=10)

# Cria botões de 1-9 em layout 3x3
for i in range(1, 10):
    # Posiciona na grade: row = (i-1)//3, column = (i-1)%3
    tk.Button(frame_numeros, 
             text=str(i), 
             command=lambda i=i: inserir_numero(i), 
             **estilo_botao
             ).grid(row=(i-1)//3, column=(i-1)%3, padx=3, pady=3)

# Botão 0 (mais largo)
tk.Button(frame_numeros, 
         text="0", 
         command=lambda: inserir_numero(0), 
         width=12,  # Largura dobrada
         height=2,
         **{k:v for k,v in estilo_botao.items() if k not in ['width', 'height']}
         ).grid(row=3, column=0, columnspan=2, padx=3, pady=3, sticky="we")

# Botão de ponto decimal
tk.Button(frame_numeros, 
         text=".", 
         command=lambda: inserir_numero('.'), 
         **estilo_botao
         ).grid(row=3, column=2, padx=3, pady=3)

# Label para exibir o resultado
resultado_label = tk.Label(janela, 
                         text="Resultado:", 
                         bg=COR_FUNDO, 
                         fg=COR_TEXTO, 
                         font=('Arial', 14))
resultado_label.pack(pady=5)

# Inicia o loop principal da aplicação
janela.mainloop()
