"""
Library for drawing and rendering "objects" onto the console.
Requires video system to be set up to work best.
Currently only supports Windows platforms with python installed.

MODULE DEPENDENCIES:
math, os, pygame, time, keyboard

Loosely based on _2dSystem library written for microcontrollers
https://github.com/DevNerdGR/_2dSystem/tree/main

Developed by DevNerdGR

BACKUP COPY, STABLE (ENOUGH)
"""
import math
import os
import pygame
import time
import keyboard

pygame.init()

#Video system
"""
Structure/use case for setting up video system:
1. Create a MAIN GAME LOOP
2. Create a function to house logic that will be called every frame
3. Inside the main game loop, call clear() followed by function that is to be called every frame then tick([fps])
4. Remember to add handling for quitting the game. To quit the game, simply call the quit() function

EXAMPLE:
fps = 60

def process(): #Function to be called every frame
    ...
    game logic
    ...

def loop():
    clear()
    process()
    tick(fps)
"""

def clear():
    if os.name == "nt":
        _ = os.system('cls')

def tick(fps):
    time.sleep(1 / fps)

def quit():
    exit()


#Abstracted systems for rendering things
class Point:
    def __init__(self, x : int, y : int):
        self. x = x
        self.y = y
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    def __str__(self):
        return f"Point @ ({self.x}, {self.y})"
    
    #Operators
    def __eq__(self, pt : "Point"):
        if self.x == pt.x and self.y == pt.y:
            return True
        else:
            return False
    
    def is_between(self, line : "Line"):
        if self.y == (line.m * self.x + line.c):
            return True
        else:
            return False
    
    #Functions
    def transform_by_vector(self, r : "Vector"):
        self.x += r.x
        self.y += r.y
    
    def move_to(self, x : int, y : int):
        self.x = x
        self.y = y
    
    def draw(self, texture : str):
        rep = ""
        for i in range(self.y):
            rep += "\n"
        rep += format(texture, f">{int(self.x)}s")
        print(rep)
    
    def draw_abs(self, texture : str):
        """
        EXPERIMENTAL
        """
        rep = ""
        for i in range(self.y):
            rep += "\n"
        rep += format(texture, f">{int(self.x * 2.5)}s")
        print(rep)

class Line:
    def __init__(self, pt1 : "Point", pt2 : "Point"):
        self.pt1 = pt1
        self.pt2 = pt2
        #y = mx + c
        self.m = (pt2.y - pt1.y) / (pt2.x - pt1.x)
        self.c = pt1.y - (self.m * pt1.x)
    
    def __str__(self):
        return f"Line from {self.pt1} to {self.pt2}"
    
    def __repr__(self):
        return f"Line from {self.pt1} to {self.pt2}"
    
    #Operators
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __eq__(self, ln : "Line"):
        if self.m == ln.m and self.c == ln.c:
            return True
        else:
            return False
    
    #Functions
    def draw(texture : str):
        pass
    
    
    
class Vector:
    x = 0
    y = 0
    
    def __init__(self, xPos : int = 0, yPos: int = 0):
        self.x = xPos
        self.y = yPos
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        return f"({self.x}, {self.y})"
    
    #constants
    def ZERO(self):
        self.x = 0
        self.y = 0
        
    def ONE(self):
        self.x = 1
        self.y = 1
        
    def LEFT(self):
        self.x = -1
        self.y = 0
        
    def RIGHT(self):
        self.x = 1
        self.y = 0
    
    def UP(self):
        self.x = 0
        self.y = -1
    
    def DOWN(self):
        self.x = 0
        self.y = 1
    
    #functions
    def abs(self):
        self.x = abs(self.x)
        self.y = abs(self.y)
        
    def angle_n(self, n : "Vector"):
        #prod = a*b
        #return math.asin(prod.abs() / 
        pass
        
    def bounce(self, n : "Vector"):
        #i = 
        pass
    
    def direction_to(self, to : "Vector"):
        return Vector(to.x - self.x, to.y - self.y)
    
    def distance_to(self, to : "Vector"):
        return ((to.x - self.y) ** 2 + (to.y - self.y) ** 2) ** 0.5
    
    def from_angle(self, angle : float):
        pass
    
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def move_toward(self, to : "Vector", delta : float):
        pass
    
    def normalized(self):
        if self.x != 0:
            self.x = self.x / abs(self.x)
        else:
            self.x = 0
        
        if self.y != 0:
            self.y = self.y / abs(self.y)
        else:
            self.y = 0
    
    #operators
    def __eq__(self, r : "Vector"):
        if self.x == r.x and self.y == r.y:
            return True
        else:
            return False
    
    def multiply_by_vector(self, r : "Vector"):
        self.x *= r.x
        self.y *= r.y
    
    def divide_by_vector(self, r : "Vector"):
        self.x //= r.x
        self.y //= r.y
    
    def add_by_vector(self, r : "Vector"):
        self.x += r.x
        self.y += r.y
    
    def subtract_by_vector(self, r : "Vector"):
        self.x -= r.x
        self.y -= r.y
    
    def multiply(self, n : int):
        self.x *= n
        self.y *= n
    
    def divide(self, n : int):
        self.x //= n
        self.y //= n
    
    def add(self, n : int):
        self.x += n
        self.y += n
    
    def subtract(self, n : int):
        self.x -= n
        self.y -= n



#DEMOSTRATION PROGRAM
"""
v0.1
Demo program that allows player to control a sprite and move it around using keyboard
> Directly uses pygame to handle inputs
"""
fps = 10 #set the fps
speed = Vector(2, 1)

character = Point(0, 0) #Initialising the player character as a (instance of) Point

vel = Vector(0, 0) #Variable for storing 'velocity' of player

def process(): #Function to be called every frame
    """ Pygame method to receive inputs, currently problematic
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_q]: #Handling exit logic
        quit()
    
    vel.x += (int(keys[pygame.K_RIGHT]) - int(keys[pygame.K_LEFT]))
    vel.y += (int(keys[pygame.K_DOWN]) - int(keys[pygame.K_UP]))
    """
    
    character.draw("(*_*)")
    
    
    #Bad implementation of input handling, you MUST press enter for character to move
    vel.ZERO()
    i = input()
    time.sleep(0.001)
    keyboard.press_and_release("enter") #Temporary solution to automatically press enter, but VERY BAD as it messes up frame rate calculations
    if i == "w":
        vel.UP()
    elif i == "s":
        vel.DOWN()
    elif i == "a":
        vel.LEFT()
    elif i == "d":
        vel.RIGHT()
    elif i == "q": #Quit handling
        quit()
    
    vel.multiply_by_vector(speed) 
    character.transform_by_vector(vel)
    

def loop(): #Main game loop
    while True:
        clear()
        process()
        tick(fps)

loop()