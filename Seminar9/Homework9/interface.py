from tkinter import *
import xogame

buttons = []
player = 1

def mouse_click(button): # Действие нажатия на кнопку игрового поля
    global player
    global btn_reset

    if xogame.Is_exists(buttons[button]): return
    
    else: buttons[button]['text'] = 'X' if player == 1 else 'O'

    if xogame.Is_won(buttons):
        info['text'] = f'Победа игрока {player}!!!'
        for button in buttons:
            button['state'] = DISABLED

    if player == 1: player = 2
    else: player = 1

    return

def mouse_reset(): # Действие нажатия на кнопку сброса
    global buttons
    global player

    player = 1

    for button in buttons:
        button['text'] = ''
        button['state'] = NORMAL
    
    info['text'] = 'Нажмите на кнопку игрового поля'

    return
        

#__________________________________________________________________________________________

win = Tk()
win.title('XO game')
win.geometry('485x500')

win.columnconfigure([0, 1, 2], weight=1, minsize=100)
win.rowconfigure([0, 1, 2, 3], weight=1, minsize=100)

#__________________________________________________________________________________________


frame_label = Frame(win, relief = RAISED, borderwidth = 1, padx = 5, pady = 5, width=80, height=4) # Задание строки состояния
frame_label.grid(row=0, columnspan=3)
info = Label(frame_label, text='Нажмите на кнопку игрового поля', font='Timesnewroman 15', fg='black', bg='SlateGray3', width=80, height=4)
info.pack()

cell_num = 0 # Задание кнопок игрового поля
for row_num in range(1, 4):
    for col_num in range(3):
        frame = Frame(win, relief = RAISED, borderwidth = 1, padx = 5, pady = 5)
        frame.grid(row=row_num, column=col_num)
        btn = Button(frame, text='', font='Arial 30', fg='black', bg='SlateGray1', width=20, height=10, command=lambda i = cell_num: mouse_click(i))
        btn.pack()
        buttons.append(btn)
        cell_num += 1

frame_reset = Frame(win, relief = RAISED, borderwidth = 1, padx = 5, pady = 5, width=80, height=4) # Задание кнопки сброса
frame_reset.grid(row=4, columnspan=3)
btn_reset = Button(frame_reset, text='Сброс', font='Arial 20',  fg='black', bg='SlateGray1', width=80, height=2, command=mouse_reset)
btn_reset.pack()


#__________________________________________________________________________________________


win.mainloop()