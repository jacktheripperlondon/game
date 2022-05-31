from tkinter import Button

class Cell:
    def __init__(self):
        self.is_mine=False
        self.cell_btn_object=None
    def create_button(self,location):
        btn=Button(
            location,
            width=12,
            height=4,
            text='cell-1'
        )    
        btn.bind('<Button-1>',self.left_click)
        self.cell_btn_object=btn
        


    def left_click(self,event):
        print(event)

    def right_click(self,event):
        print(event)
    
