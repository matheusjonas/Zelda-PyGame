import pygame, sys
from settings import *
from level import Level

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Zelda")
        self.isFullscreen = False
        self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        self.CLOCK = pygame.time.Clock()
        self.LEVEL = Level()
        MAIN_SOUND = pygame.mixer.Sound("../audio/main.ogg")
        MAIN_SOUND.set_volume(0.5)
        MAIN_SOUND.play(loops = -1)

    def run(self):
        while True:
            self.SCREEN.fill(WATER_COLOR)
            self.LEVEL.run()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        self.LEVEL.toggleMenu()
                    elif event.key == pygame.K_ESCAPE:
                        self.quit_game()
                    elif event.key == pygame.K_RETURN:
                        mods = pygame.key.get_mods()
                        if mods & pygame.KMOD_ALT:
                            self.isFullscreen = not self.isFullscreen
                            if self.isFullscreen:
                                # Tuple (0,0) to target the user's native monitor resolution
                                self.SCREEN = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
                            else:
                                # Switch back to Windowed mode
                                self.SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
            pygame.display.update()
            self.CLOCK.tick(FPS)

    def quit_game(self):
        print("QUIT!")
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    game = Game()
    game.run()
