#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar  6 16:04:28 2024

@author: bishopibrahim
"""

import pygame
import numpy
import math
import copy
from numpy.polynomial import Polynomial

def newtonsMethod(x0, f, n):
    derivative = f.deriv()
    
    for i in range(n):
        x0 = x0 - (f(x0) / derivative(x0))
    
    return x0

w, h = 720, 720
windowDimensions = (w, h)
scalingFactor = 1
rootsLastFrame = []
roots = []
rootCoords = []
rootColor = {}
colorStack = ["red", "green", "blue", "purple", "orange", "cyan", "blue4", "deeppink"]
red = (255, 0, 0)


# pygame setup
pygame.init()
screen = pygame.display.set_mode(windowDimensions)
pygame.display.set_caption("Newton's Fractal")
clock = pygame.time.Clock()
surface = pygame.Surface(windowDimensions)
running = True
screen.fill("black")


while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN: #Set a new zero
                # Check if the left mouse button is clicked
                if event.button == 1:  # Left click
                    # Get the mouse position
                    x, y = event.pos
                    rootCoords.append((x,y))
                    
                    #Draw point to represent complex zero
                    
                    
                    
                    
                    imaginaryCoords = ((x - w/2)/scalingFactor, (-(y - h/2)/scalingFactor))
                    z = complex(imaginaryCoords[0], imaginaryCoords[1])

                    roots.append(z)
                    print(roots)
                    rootColor[z] = colorStack.pop(0)
        
             

    # flip() the display to put your work on screen
    
    
    if rootsLastFrame != roots:
        print("crunching")
        p = Polynomial.fromroots(roots)
        for i in range(windowDimensions[0]):
            for j in range(windowDimensions[1]):
                imagCoords =  (math.floor((i - w/2)/scalingFactor), math.floor((-(j - h/2)/scalingFactor)))
                z0 = complex(imagCoords[0], imagCoords[1])
                z1 = newtonsMethod(z0, p, 10)
            
                closestRoot = None
                closestDistance = windowDimensions[0] + 50
                for z2 in roots:
                    distance = abs(z1 -  z2)
                    if  distance < closestDistance:
                        closestDistance = distance
                        closestRoot = z2
                
                if closestRoot != None:            
                    screen.set_at((i, j), rootColor[closestRoot])
        rootsLastFrame = copy.copy(roots)
  
        
        
        
  

                    
    # fill the screen with a color to wipe away anything from last frame
    
    
                    
            
    
    
    #Draw axes
    for point in rootCoords:
        pygame.draw.circle(screen, "white", point, 5)
    pygame.draw.line(screen, color ="white", start_pos = (w/2,0), end_pos = (w/2,h), width = 1)
    pygame.draw.line(screen, color ="white", start_pos = (0,h/2), end_pos = (w,h/2), width = 1)
   
    pygame.display.flip()     

    clock.tick(60)  # limits FPS to 60

pygame.quit()