import PySimpleGUI as sg
from sudoku import solve

input_rows = [[sg.Input(default_text=0,
                        size=(4,1),
                        pad=(0,0),
                        justification='center') for col in range(9)] for row in range(9)]
control_row = [[sg.Button('Solve')]]
output_row = [[sg.Output(size=(36, 15), key='_output_')]]

layout = input_rows + control_row + output_row
window = sg.Window('Sudoku Solver', layout)

def print_board(puzzle):
    for i in range(10):
        print()
        if i % 3 == 0:
            print("- " * 16)
            if i == 9:
                break
        print("| ", end="")
        for j in range(9):
            print(puzzle[i][j], end=" " if j % 3 != 2 else " | ")

while True:
    event, values = window.read()
    results = list(values.values())
    int_results = [int(i) for i in results]
    puzzle = [int_results[i:i+9] for i in range(0, len(int_results), 9)]

    if event == sg.WINDOW_CLOSED:
        break
    if event == 'Solve':
        window['_output_']('')
        solve(puzzle)
        print_board(puzzle)

window.close()
