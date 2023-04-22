class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    def set_width(self,newWidth):
        self.width=newWidth
    def set_height(self,newHeight):
        self.height=newHeight
    def get_area(self):
        area=self.width * self.height
        return area
    def get_perimeter(self):
        perimeter=2 * self.width + 2 * self.height
        return perimeter
    def get_diagonal(self):
        diagonal=(self.width ** 2 + self.height ** 2) ** .5
        return diagonal
    def get_picture(self):
        Output=""
        if self.width>50 or self.height>50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                Output+=self.width*"*" + "\n"
            return Output
    def get_amount_inside(self,shape):
        return int(self.get_area()//shape.get_area())
        



class Square(Rectangle):
    def __init__(self,side):
        self.width=side
        self.height=side
    def __str__(self):
        return f"Square(side={self.width})"
    def set_side(self,NewSide):
        self.width=NewSide
        self.height=NewSide
    
    
