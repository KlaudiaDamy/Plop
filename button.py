import pygame

class Button (pygame.Rect):
    def __init__(self, color, pos_x, pos_y):
        self.width = 60
        self.height = 60
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = color
        super().__init__(self.pos_x, self.pos_y, self.width, self.height)

    def get_color(self):
        return self.color
