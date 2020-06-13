import pygame
from button import Button

class Plop:
    def __init__(self):
        pygame.init();
        self.width = 400
        self.height = 400
        self.done = False
        self.window = pygame.display
        self.window.set_caption("Plop v1", "Plop")
        self.clock = pygame.time.Clock()

        
    def start(self):
        screen = self.window.set_mode((self.width, self.height))
        button = Button((255, 255, 255), 30, 30)
        button_2 = Button((255, 0, 255), 90, 30)

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
            pygame.draw.rect(screen, button.get_color(), button)
            pygame.draw.rect(screen, button_2.get_color(), button_2)
            # to refresh screen
            self.window.flip()
            self.clock.tick(60)

def main():
    plop = Plop()
    plop.start();
    
if __name__ == '__main__':
    main()
