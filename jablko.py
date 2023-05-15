import random
import waz
import pygame

class Jablko():
    #konstruktor klasy
    def __init__(self):
        self.pozycjaJablka=[(1,1)]
        self.randomPosition()
    #losowanie pozycji jabłka i zapisanie nowej pozycji do zmiennej pozycjaJablka
    def randomPosition(self):
        jablkoX=random.randint(0,waz.rozdzielczosc)*30
        jablkoY=random.randint(0,waz.rozdzielczosc)*30
        self.setCoordinates(jablkoX,jablkoY)

    #pobranie pozycji jabłka
    def getCoordinates(self):
        return self.pozycjaJablka[-1]

    #ustawienie pozycji jabłka
    def setCoordinates(self,x,y):
        self.pozycjaJablka[0]=(x,y)

    #rysowanie jabłka
    def drawApple(self, oknoGry):
        pygame.draw.circle(oknoGry,(255,0,0),(self.pozycjaJablka[0][0]+15,self.pozycjaJablka[0][1]+15),15)