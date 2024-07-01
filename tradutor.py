from tkinter import Tk, ttk, Text, Button
from googletrans import Translator
from ttkthemes import ThemedTk
from ttkbootstrap import Style

#utilizando o Gogole translator versao 4.0
# > pip install googletrans==4.0.0rc1

translator = Translator()

#criando a interface Tk default
# janela = Tk()
# janela.title('Programinha de tradução!!!')

#janela do ttkthemes
# > https://ttkthemes.readthedocs.io/en/latest/themes.html
# janela = ThemedTk(theme='equilux')


#janela do ttkbootstrap
# > https://ttkbootstrap.readthedocs.io/en/latest/themes/
style = Style(theme='minty')
janela = style.master


janela.title('Tradutor da Andrezza')
frame_geral = ttk.Frame()


def traduzir(evento=None):
    #'1.0' e 'end' mando o get pegar do primeira linha a ultima
    texto = entrada.get('1.0', 'end')
    src = combo_entrada.get()
    dest = combo_saida.get()
    resultado = translator.translate(
        text=texto,
        src=src,
        dest=dest
    )

    saida.configure(state='normal')
    saida.delete('1.0', 'end')
    saida.insert('1.0', resultado.text)
    saida.configure(state='disabled')



#linguagens que terão tradução
values = ['pt', 'es', 'en']


#opções de entrada
frame_entrada = ttk.Frame(frame_geral)

label_entrada = ttk.Label(
    frame_entrada, 
    text='Entrada',
    font=(None, 15)
    )

combo_entrada = ttk.Combobox(
    frame_entrada,
    values=values,
    font=(None, 20),
    state='readonly' # deixa somente leitura as opçoes de combobox
    )

combo_entrada.set('pt')

label_entrada.grid(row=0, column=0, padx=10, pady=10)
combo_entrada.grid(row=0, column=1, padx=10, pady=10)
frame_entrada.pack()

entrada = Text(
                frame_geral, 
                height=7, 
                width=30, 
                font=(None, 15))
entrada.pack(padx=10, pady=10, fill='both', expand='yes')


#opções de saida
frame_saida = ttk.Frame(frame_geral)

label_saida = ttk.Label(
    frame_saida, 
    text='Saída',
    font=(None, 15)
    )
combo_saida = ttk.Combobox(
    frame_saida,
    values=values,
    font=(None, 20),
    state='readonly' # deixa somente leitura as opçoes de combobox
    )
combo_saida.set('en')

label_saida.grid(row=0, column=0, padx=10, pady=10)
combo_saida.grid(row=0, column=1, padx=10, pady=10)
frame_saida.pack()

saida = Text(
            frame_geral,
            height=7, 
            width=30, 
            font=(None, 15),
            state='disabled'
             )

saida.pack(padx=10, pady=10, fill='both', expand='yes')

botao = ttk.Button(
    frame_geral,
    text='Traduzir!',
    # font=(None, 15),
    command=traduzir
)

botao.pack(fill='both', padx=5, pady=5)
frame_geral.pack()

janela.bind('<Return>', traduzir)

janela.mainloop()