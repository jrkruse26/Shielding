import pygame,random

WHITE = (255,255,255)
RED = (255,0,0)
BLUE = (0,0,255)
BLACK = (0,0,0)
size = [1,1]
rads = []

class Rad:
    def create(self, number, surface):
        for x in range(number):
            loc = [70, random.randint(235,264)]
            vel = [1,0]
            pygame.draw.rect(surface, BLACK, loc + size)
            rad = [loc,vel]
            rads.append(rad)
    def move(self, surface):
        for n,rad in enumerate(rads):
            loc = rad[0]
            vel = rad[1]
            pygame.draw.rect(surface, WHITE, loc + size)
            loc = [loc[0]+vel[0],loc[1]+vel[1]]
            if loc[0] > 500:
                del rads[n]
            else:
                pygame.draw.rect(surface, BLACK, loc + size)
                rads[n] = [loc,vel]

def main():

    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    pygame.display.set_caption('Shielding')

    background = pygame.Surface(screen.get_size()).convert()
    background.fill((250, 250, 250))
    screen.blit(background, (0, 0))
    rect = (0,230,70,40)
    pygame.draw.rect(screen, RED, rect, 0)

    run = True
    r = Rad()
    clock = pygame.time.Clock()
    while run:
        r.create(2,screen)
        r.move(screen)
        pygame.display.flip()
        clock.tick(60)
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
                run = False
main()
pygame.quit()