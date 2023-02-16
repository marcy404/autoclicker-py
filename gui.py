from PySimpleGUI import PySimpleGUI as PGU

PGU.theme('DarkTeal3')
daora = PGU.Window('Exemplo', [[PGU.Text('this is a window'), PGU.Input(key='usuario')]])


daora