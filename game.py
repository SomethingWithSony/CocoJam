import pygame
from scripts.utils import load_image, draw_text
from scripts.entities import Player

class Game:
  def __init__(self):
    pygame.init()
    
    pygame.display.set_caption("Poison")

    self.screen = pygame.display.set_mode((640,480))
    self.display = pygame.Surface((320,240))
    
    self.clock = pygame.time.Clock()
    
    self.assets = {
      'player': load_image('entities/player.png')
    }
    
    self.fonts = {
      'default': pygame.font.SysFont(None, 20)
    }
    
    self.game_state = 'game_loop'
    self.running = True
    
    # Mouse position
    self.mx = 0
    self.my = 0
    
    self.x = 0
    
    self.movement = [0, 0]
    
    # Spawn player
    self.player = Player(self,'player', (50,50), (8,8))
    
    # Last key pressed 
    # Used for movement system
    self.last_pressed_left = False
    self.last_pressed_up = False
  
  def screen_state_manager(self):
    while self.running:
      match self.game_state:
        case 'main_menu':
          self.main_menu()
        case 'game_loop':
          self.game_loop()
        case 'game_over':
          self.game_over()
        case 'victory':
          self.victory()
          
    pygame.quit() # Closes pygame
  
  def victory(self):
    pass

  def main_menu(self):
    pass
        
  def game_over(self):
    self.display.fill((0,0,0))
    
    draw_text('Game Over',self.fonts['default'],(255,255,255),self.display,(160,120))
    
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        
      if event.type == pygame.KEYDOWN:      
        if event.key == pygame.K_l:
          self.game_state = 'game_loop'
    
    self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()) , (0, 0))
    pygame.display.update() 
    self.clock.tick(60) # Force the game to run at 60fps

  def game_loop(self):
    self.display.fill((0,0,0))
    self.x += 1
    if self.x == 60:
      self.x = 0
      self.player.add_progress()
      
      
      
    draw_text('teste',self.fonts['default'],(255,255,255),self.display,(100,100))
    self.player.render()
    # Get Mouse Position
    self.mx, self.my = pygame.mouse.get_pos()
    
    # Diving by 2 becayse of to the screen scale
    self.mx = self.mx / 2
    self.my = self.my / 2
    
    
    
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        self.running = False
        
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_a:
          self.movement[0] = -1
          self.last_pressed_left = True
        if event.key == pygame.K_d:
          self.movement[0] = 1
          self.last_pressed_left = False
        if event.key == pygame.K_w:
          self.movement[1] = -1
          self.last_pressed_up = True
        if event.key == pygame.K_s:
          self.movement[1] = 1
          self.last_pressed_up = False
          
        if event.key == pygame.K_l:
          self.game_state = 'game_over'
      
      if event.type == pygame.KEYUP:
        # Basic Movement
        if event.key == pygame.K_a and self.last_pressed_left:
          self.movement[0] = 0
        if event.key == pygame.K_d and not self.last_pressed_left:
          self.movement[0] = 0
        if event.key == pygame.K_w and self.last_pressed_up:
          self.movement[1] = 0
        if event.key == pygame.K_s and not self.last_pressed_up:
          self.movement[1] = 0
    self.player.update(self.movement)
    
    self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()) , (0, 0))
    pygame.display.update() 
    self.clock.tick(60) # Force the game to run at 60fps
    
    # dt = self.clock.tick / 1000 
    # dt * movement = Constant movement indepent of fps
      
  
 


Game().screen_state_manager()
