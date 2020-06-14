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
        self.button_list = [[], [], [], [], []]

    def init_game(self):
        x = 30
        y = 30

        for i in range(5):
            for j in range(5):
                if i == 0 and j == 0:
                    self.button_list[i].append(Button(get_random_color(), x, y))
                    x += 60
                else:
                    self.button_list[i].append(Button(get_random_color(), x, y))
                    x += 60
            x = 30
            y += 60

    def draw_board(self, screen, button_list):
        for i in range(5):
            for j in range(5):
                button = button_list[i][j]
                pygame.draw.rect(screen, button.get_color(), button)


    def start(self):
        screen = self.window.set_mode((self.width, self.height))

        # Build up the board
        self.init_game()

        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if button.collidepoint(event.pos):
                        print (button.get_color())
                    if button_2.collidepoint(event.pos):
                        print (button_2.get_color())

            screen.fill((0, 0, 0))
            self.draw_board(screen, self.button_list)
            # draw before this line 
            # to refresh screen
            self.window.flip()
            self.clock.tick(60)

def main():
    plop = Plop()
    plop.start();
    print ("tld heidy")
    
if __name__ == '__main__':
    main()
