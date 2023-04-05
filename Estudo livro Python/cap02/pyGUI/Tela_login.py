from PySimpleGUI import PySimpleGUI as sg
#layout
sg.theme('black')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario', size = (20,1))],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*', size = (20,1))],
    [sg.Checkbox('Salvar o login?')],
    [sg.Button('Acessar')]
]
#janela
janela = sg.Window('Tela de Login', layout)

#ler os eventos
while True:
    eventos, valores = janela.read()
    if eventos == sg.WINDOW_CLOSED:
        break
    if eventos == 'Entrar':
        if valores['Usuário'] == 'juvito4i20' and valores['Senha'] == 'Caveira14':
            print('Bem vindo ao sistema do juvito')
