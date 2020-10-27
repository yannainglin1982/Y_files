import pygame
pygame.init()

from pygame import mixer
mixer.init()

screen = pygame.display.set_mode((250, 250))
done = False
x=60
y=60

image=pygame.image.load(r'C:\Users\SK\Documents\My Documents\new.jpg')
screen.blit(image, (0, 0))


pygame.mixer.music.load(r'D:\YNL DATA\Music\MTLA.mp3')
pygame.mixer.music.play(-1)

while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pygame.draw.rect(screen, (0,255,0), pygame.Rect(x, y, 100, 50))
        
        pygame.display.flip()
