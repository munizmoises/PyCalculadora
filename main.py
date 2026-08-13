import tkinter

# Funções da calculadora

def inserir_texto(texto):
    # Ele vai pegar o texto que já está digitado no visor
    conteudo_atual = visor.get()

    # Limpa o visor do índice 0 até o final (tkinter.END)
    visor.delete(0, tkinter.END)

    # Reescreve o conteúdo antigo juntamente com o novo caractere clicado
    visor.insert(0, conteudo_atual + texto)

def limpar_visor():
    # Apaga absolutamente tudo do visor
    visor.delete(0, tkinter.END)

def calcular_resultado():
    try:
        # Pega a expressão em texto (por exemplo, "7+5*2")
        expressao = visor.get()
        
        # A função eval() lê o texto e resolve a conta matemática
        resultado = eval(expressao)
        
        # Limpa o visor e exibe o resultado final convertido em texto
        visor.delete(0, tkinter.END)
        visor.insert(0, str(resultado))
    except Exception:
        # Se o usuário tentar uma operação inválida (ex: 5// ou dividir por 0)
        visor.delete(0, tkinter.END)
        visor.insert(0, "Erro")

# Janela do tkinter

janela = tkinter.Tk() # Cria a janela principal
janela.title('Calculadora 0.2.0-alpha') # Titulo da janela
janela.resizable(False, False) # Não ter como maximizar a tela

# Visor da janela

visor = tkinter.Entry(janela, width=16, font=('Arial', 24), justify='right')

# O visor fica na Linha 0, Coluna 0, e ocupa a largura de 4 colunas (columnspan=4)
visor.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# BOTÕES
# Linha 1 (row=1)

btn_7 = tkinter.Button(janela, text='7', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('7'))
btn_7.grid(row=1, column=0, padx=3, pady=3)

btn_8 = tkinter.Button(janela, text='8', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('8'))
btn_8.grid(row=1, column=1, padx=3, pady=3)

btn_9 = tkinter.Button(janela, text='9', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('9'))
btn_9.grid(row=1, column=2, padx=3, pady=3)

# Linha 2 (row=2)

btn_4 = tkinter.Button(janela, text='4', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('4'))
btn_4.grid(row=2, column=0, padx=3, pady=3)

btn_5 = tkinter.Button(janela, text='5', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('5'))
btn_5.grid(row=2, column=1, padx=3, pady=3)

btn_6 = tkinter.Button(janela, text='6', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('6'))
btn_6.grid(row=2, column=2, padx=3, pady=3)

# Linha 3 (row=3)

btn_1 = tkinter.Button(janela, text='1', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('1'))
btn_1.grid(row=3, column=0, padx=3, pady=3)

btn_2 = tkinter.Button(janela, text='2', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('2'))
btn_2.grid(row=3, column=1, padx=3, pady=3)

btn_3 = tkinter.Button(janela, text='3', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('3'))
btn_3.grid(row=3, column=2, padx=3, pady=3)

# Linha 4 (row=4)

btn_limpar = tkinter.Button(janela, text='C', width=5, height=2, font=('Arial', 14), command=limpar_visor)
btn_limpar.grid(row=4, column=0, padx=3, pady=3)

btn_0 = tkinter.Button(janela, text='0', width=5, height=2, font=('Arial', 14), command=lambda: inserir_texto('0'))
btn_0.grid(row=4, column=1, padx=3, pady=3)

btn_igual = tkinter.Button(janela, text="=", width=5, height=2, font=("Arial", 14), command=calcular_resultado)
btn_igual.grid(row=4, column=2, padx=3, pady=3)

btn_somar = tkinter.Button(janela, text="+", width=5, height=2, font=("Arial", 14), command=lambda: inserir_texto("+"))
btn_somar.grid(row=4, column=3, padx=3, pady=3)



janela.mainloop() # Executa a janela