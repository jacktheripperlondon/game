from re import T
from tkinter import *
from turtle import left
import settings
import utils 
from cell import Cell





root=Tk()
root.title('game fo the year')
root.geometry(f'{settings.WIDTH}x{settings.HEIGHT}')
root.resizable(False,False)
root.configure(bg='black')

top_frame=Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utils.height_perct(25)
    )
top_frame.place(x=0,y=0)    

game_title=Label(
    top_frame,
    bg='black',
    fg='white',
    text='Minesweeper game',
    font=("",30)
)
game_title.place(
    x=utils.width_perct(25),
    y=0
)
left_frame=Frame(
    root,
    bg='black',
    width=utils.width_perct(25),
    height=utils.height_perct(75)
)
left_frame.place(x=0,y=utils.height_perct(25))

centre_frame=Frame(
    root,
    bg='black',
    width=utils.width_perct(75),
    height=utils.height_perct(75)
)
centre_frame.place(x=utils.width_perct(25),y=utils.height_perct(25))



for x in range(settings.GRIDSIZE):
    for y in range(settings.GRIDSIZE):
        c=Cell(x,y)
        c.create_button(centre_frame)
        c.cell_btn_object.grid(
            column=x,
            row=y
        )
Cell.random_mines()

Cell.cell_count(left_frame)
Cell.cell_count_label.place(x=0,y=0)
root.mainloop()