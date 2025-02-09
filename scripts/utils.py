import numpy as np
import os 
import pygame

BASE_IMG_PATH = 'data/images/'

def load_image(path):
  img = pygame.image.load(BASE_IMG_PATH + path).convert()
  img.set_colorkey((0, 0, 0))
  return img 

def load_images(path):
  images = []
  for img_name in sorted(os.listdir(BASE_IMG_PATH + path)):
    images.append(load_image(path + '/' + img_name))
    
  return images

def normalize_vector(vector):
  magnitude = np.linalg.norm(vector)
  return vector / magnitude

# Use for display text
def draw_text(text, font, color, display , position):
  text_object = font.render(text,1,color)
  text_rect = text_object.get_rect()
  text_rect.topleft = position
  display.blit(text_object, text_rect)
  
class Particle:
  def __init__(self, location , veloticy, duration):
    self.loc = location
    self.vel = veloticy
    self.dur = duration
    
