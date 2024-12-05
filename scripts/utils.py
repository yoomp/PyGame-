import os 
import pygame

BASE_IMG_PATH = "data/images/" #this is where all the images are stored and is now assigned to a variable  

def load_image(path):#This converts the image into a format that makes it easier for pygame to render, improving performance and also makes it transparent 
    img = pygame.image.load(BASE_IMG_PATH + path).convert() 
    img.set_colorkey((0,0,0))
    return img

def load_images(path):
    images = []
    for img_name in os.listdir(BASE_IMG_PATH + path) : #takes a path and gives all files in that path, good way to load multiple images
        images.append(load_image(path + "/" + img_name)) #loads image
    return images
        
