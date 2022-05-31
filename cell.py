from tkinter import Button

class Cell:
    def __init__(self,x,y,is_mine=False):
        self.is_mine=is_mine
        self.cell_btn_object=None
        self.x=x
        self.y=y
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
    
