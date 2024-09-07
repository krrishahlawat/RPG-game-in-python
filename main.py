import pygame,sys
from settings import *
from level import *
class Game:
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode((Width,Height))
        pygame.display.set_caption("Zelda")
        self.clock = pygame.time.Clock()
        self.level = Level()
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()


            self.screen.fill('black')
            self.level.run()
            pygame.display.update()
            self.clock.tick(fps)

if __name__ == '__main__':
    game = Game()
    game.run()
