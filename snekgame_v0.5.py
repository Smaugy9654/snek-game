import pygame

pygame.init()
window = pygame.display.set_mode((800, 600))
#the title?
pygame.display.set_caption("i love chicken")
#player thingys
player = pygame.surface.Surface((100, 200))
player.fill((0, 5, 0))
player_x = 0
player_y = 0
player_vel_x = 0
player_vel_y = 0

while True:
    #take input
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         pygame.quit()
         quit()

   #output
   window.fill((0, 0, 0))
   window.blit(player, (player_x, player_y))
   pygame.display.flip()
