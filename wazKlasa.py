import pygame


class WazKlas():
    #konstruktor klasy - uruchamia się podczas tworzenia obiektu
    def __init__(self):
        self.pozycje=[(300,300)]
        self.dlugosc=1
        self.kierunek=[0,1]
        self.punkty=0
    #ustalanie kierunku węża
    def setDirection(self, direction):
        self.kierunek=direction
        #dodawanie punktow
    def addScore(self):
        self.punkty=self.punkty+1
        #zerowanie punktow
    def clearScore(self):
        self.punkty=0
        #dodawanie dlugosci
    def addLenght(self):
        self.dlugosc+=1
    #pobieranie współrzednych głowy węża
    def getHeadPosition(self):
        return self.pozycje[-1]
    #wykonanie ruchu przez węża
    def snakeMove(self):
        #pobranie ostatnie pozycji glowy węża
        ostatniaPozycja=self.getHeadPosition()
        #ustalenie nowej pozycji węża
        zmiennaX=ostatniaPozycja[0]+self.kierunek[0]*30;
        zmiennaY=ostatniaPozycja[1]+self.kierunek[1]*30;
        #sprawdzenie położenia weża względem krawędzi
        noweWspolrzedne=self.checkBorder(zmiennaX,zmiennaY)
        #dodanie pozycji węża do listy
        self.pozycje.append(noweWspolrzedne)
        #sprawdzenie czy wąż nie jest za długi
        if len(self.pozycje)>self.dlugosc:
            del self.pozycje[0]
    
    #sprawdzanie krawędzi okna
    def checkBorder(self,zmiennaX,zmiennaY):
         #sprawdzanie krawędzi
        if zmiennaX>=600:
            zmiennaX=0
        if zmiennaX<0:
            zmiennaX=600-30
        if zmiennaY>=600:
            zmiennaY=0
        if zmiennaY<0:
            zmiennaY=600-30
        return (zmiennaX,zmiennaY)
    #rysowanie węża
    def snakeDraw(self,oknoGry):
        for poz in self.pozycje[::-1]:
        #definiujemy kształ węża
            ksztaltWaz=pygame.Rect((poz[0],poz[1]),(30,30))
            #dodanie kształtu do okienka
            pygame.draw.rect(oknoGry,(100,100,100),ksztaltWaz)