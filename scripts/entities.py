import pygame
import random
from scripts.utils import normalize_vector, Particle

class PhysicsEntity:
  def __init__(self, game, e_type, pos, size):
    self.game = game
    self.type = e_type
    self.pos = list(pos) # Ensure that it's not a reference
    
    self.velocity = 2
    self.size = size

    self.action = '' # Usar action atacking em vez d bool

    self.set_action('idle')

    self.entity = pygame.transform.rotate(self.game.assets[e_type], -90 )

  def update(self,movement):
    if movement[0]!= 0 and movement[1] != 0:
      movement = normalize_vector(movement)

    movement = (movement[0] * self.velocity, movement[1] * self.velocity)

    self.pos[0] += movement[0]
    self.pos[1] += movement[1]

  def render(self,):
      entity_rect = self.entity.get_rect(center = (self.pos[0], self.pos[1]))
      self.game.display.blit(self.entity,entity_rect)
      
  def set_pivot_to_center(self):
    return self.entity.get_rect(center = (self.pos[0], self.pos[1] ))

  def set_action(self, action):
    if action != self.action:
      self.action = action

class Player(PhysicsEntity):
  def __init__(self, game, e_type, pos, size):
    super().__init__(game, e_type, pos, size)
    
    self.entity = pygame.transform.rotate(self.game.assets[e_type], -90 )
    
    self.health = 100
    
    self.infection_bar_length = 220
    self.infection_max_progress = 60 * 5 # Time in seconds in wich the infection would get to 100%
    self.infection_curr_progress = 1
    self.infection_ratio = self.infection_max_progress / self.infection_bar_length
    
    
    # Low
    self.low_antidote_usage_count = 1
    # Medium
    self.low_antidote_usage_count = 1
    # High
    self.low_antidote_usage_count = 1

  def render(self):
    self.entity = pygame.transform.rotate(self.game.assets[self.type], -90 )
    entity_rect = self.set_pivot_to_center()
    pygame.draw.rect(self.game.display, (255,0,0), entity_rect, 1)
    
    
    self.draw_collision_area()
    self.game.display.blit(self.entity,entity_rect)
    self.infection_bar()
    
  def draw_collision_area(self):
    pygame.draw.circle(self.game.display, (200,0,0,), (self.pos[0], self.pos[1]) ,50,50)
    
  def detect_collisions(self, object):
    pass
    
  def add_progress(self):
    if self.infection_curr_progress < self.infection_max_progress:
      self.infection_curr_progress += 100 / self.infection_max_progress 
    else:
      self.infection_curr_progress = self.infection_max_progress
      self.game.game_state = 'game_over'
    
  def slowdown_progress(self, antidote_lvl):
    match antidote_lvl:
      case 'low':
        self.infection_curr_progress -= 60 / self.low_antidote_usage_count
        self.low_antidote_usage_count += 1
      case 'medium':
        self.infection_curr_progress -= 60 * 2.5  / self.medium_antidote_usage_count
        self.medium_antidote_usage_count += 1
      case 'high':
        self.infection_curr_progress -= 60 * 4 / self.high_antidote_usage_count
        self.high_antidote_usage_count += 1
      case 'cure':
        self.game.game_state = 'victory'
        print("You won the game you're cured")
    
  def infection_bar(self):
    pygame.draw.rect(self.game.display, (100,255,10), (10,10, 8, self.infection_curr_progress / self.infection_ratio ))
    pygame.draw.rect(self.game.display, (200,200,200), (10,10, 8, self.infection_bar_length ), 1)

  
class Item:
  def __init__(self):
    pass
      
 

    