# Burger Catch! A game made by Evan Lisby for CS 120


import pygame, random, simpleGE


class Ketchup(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Ketchup.png")
        self.setSize(100, 100)
        self.reset()
        
    def reset(self):
        self.y = 10
        self.x = random.randint(20, 620)
        self.dy = random.randint(5, 10)
        
    def checkBounds(self):
        if self.bottom > 650:
            self.reset()


class BurgerLad(simpleGE.Sprite):
    def __init__(self, scene):
        super().__init__(scene)
        self.setImage("Burger Lad w Spatula.png")
        self.setSize(150, 150)
        self.position = (320, 400)
        self.movespeed = 10
        
    def process(self):
        if self.isKeyPressed(pygame.K_LEFT):
            self.x -= self.movespeed
        if self.isKeyPressed(pygame.K_RIGHT):
            self.x += self.movespeed


class Game(simpleGE.Scene):
    def __init__(self):
        super().__init__()
        self.setImage("wood panel background.jpg")
        self.BurgerLad = BurgerLad(self)
        self.Ketchup = Ketchup(self)
        self.sprites = [self.BurgerLad, self.Ketchup]
        
    def process(self):
        if self.BurgerLad.collidesWith(self.Ketchup):
            self.Ketchup.reset()

        
        
        
def main():
    game = Game()
    game.start()
    
if __name__ == "__main__":
    main()