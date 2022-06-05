from itertools import count
from tkinter import Button, Label
import random
import settings
from scipy import rand
import ctypes
import sys
class Cell:
    all=[]

    cell_count_label=None
    cell_numbers=settings.no_of_cells

    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object=None
        self.mine_candidate=False
        self.is_open=False
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
        btn.bind('<Button-3>',self.right_click)
        self.cell_btn_object=btn
        


    def left_click(self,event):
        if self.is_mine:
            self.show_mine()
        else:
            if self.surrounded_cells_mines==0:
                for cell_obj in self.surrounded_cells:
                    cell_obj.show_cell()
            self.show_cell()  
            if Cell.cell_numbers==9:
                ctypes.windll.user32.MessageBoxW(0,'Congratulations','game won',0)

        self.cell_btn_object.unbind('<Button-1>')
        self.cell_btn_object.unbind('<Button-3>')      
    @staticmethod
    def cell_count(location):
        lbl=Label(
            location,
            bg='black',
            fg='white',
            text=f"Cells Left:{Cell.cell_numbers}",
            width=12,
            height=4,
            font=("",30)
        )
        Cell.cell_count_label=lbl

    def right_click(self,event):
        if not self.mine_candidate:
            self.cell_btn_object.configure(
                bg='orange'
            )
            self.mine_candidate=True

        else:
            self.cell_btn_object.configure(
                bg='SystemButtonFace'
            )    
            self.mine_candidate=False
    def get_cell_by_axis(self,x,y):
        for cell in Cell.all:
            if cell.x==x and cell.y==y:
                return cell 

    def show_mine(self):
        self.cell_btn_object.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0,'you clicked on a mine','game over',0)
        sys.exit()



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
        if not self.is_open:
            Cell.cell_numbers-=1
            self.cell_btn_object.configure(text=self.surrounded_cells_mines)

        if Cell.cell_count_label:
            Cell.cell_count_label.config(
                text=f"Cells left:{Cell.cell_numbers}"
                )
        self.cell_btn_object.configure(
            bg='SystemButtonFace'
        )
        self.is_open=True        

    
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