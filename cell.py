from tkinter import Button
import random

from scipy import rand
class Cell:
    all=[]
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object=None
        self.x=x
        self.y=y
        Cell.all.append(self)
    def create_button(self,location):
        btn=Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )    
        btn.bind('<Button-1>',self.left_click)
        self.cell_btn_object=btn
        


    def left_click(self,event):
        print(event)

    def right_click(self,event):
        print(event)
    
    @staticmethod
    def random_mines():
        picked_cells=random.sample(
            Cell.all,
            9
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine=True


    def __repr__(self):
        return f'Cell({self.x},{self.y})'