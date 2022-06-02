from itertools import count
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
            
        )    
        btn.bind('<Button-1>',self.left_click)
        self.cell_btn_object=btn
        


    def left_click(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()    


    def right_click(self,event):
        print(event)

    
    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell 

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
    @property
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y -1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        
        cells=[cell for cell in cells if cell is not None]
        return cells
    @property
    def surrounded_cells_mines(self):
        counter=0
        for cell in self.surrounded_cells:
            if cell.is_mine:
                counter+=1
        return counter        

    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounded_cells_mines)
    
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