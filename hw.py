import pygame

pygame.init()

screen = pygame.display.set_mode((640, 480))

pygame.display.set_caption("My first game screen")

WHITE = (255, 255, 255)
BLUE = (0, 128, 255) 


running = True
while running:
    screen.fill(WHITE) 
       
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.draw.rect(screen,(0,125,255),pygame.Rect(30,30,60,25))  
    pygame.display.flip() 


pygame.quit()


