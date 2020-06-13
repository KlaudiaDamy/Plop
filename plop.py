import pygame
from button import Button
from utils import *

class Plop:
    def __init__(self):
        pygame.init();
        self.width = 360
        self.height = 360
        self.done = False
        self.window = pygame.display
        self.window.set_caption("Plop v1", "Plop")
        self.clock = pygame.time.Clock()

        
    def start(self):
        x = 30
        y = 30
        screen = self.window.set_mode((self.width, self.height))
        button_list = [[], [], [], [], []]

        for i in range(5):
            for j in range(5):
                if i == 0 and j == 0:
                    button_list[i].append(Button(get_random_color(), x, y))
                    x += 60
                else:
                    button_list[i].append(Button(get_random_color(), x, y))
                    x += 60
            x = 30
            y += 60

        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.collidepoint(event.pos):
                        print (button.get_color())
                    if button_2.collidepoint(event.pos):
                        print (button_2.get_color())

            # Draw things before line #24
            screen.fill((0, 0, 0))
            for i in range(5):
                for j in range(5):
                    button = button_list[i][j]
                    pygame.draw.rect(screen, button.get_color(), button)
            
            # to refresh screen
            self.window.flip()
            self.clock.tick(60)

def main():
    plop = Plop()
    plop.start();
    print ("tld heidy")
    
if __name__ == '__main__':
    main()
