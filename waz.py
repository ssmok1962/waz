#pobranie biblioteki pygame
import random
import pygame
#import kodu z klasą wąż
import wazKlasa

#importujemy kod z pliku jablko
import jablko

#tworzenie obiektu wąż
obiektWaz1=wazKlasa.WazKlas()

#utowrzenie obiektów jabłek
#określenie ile będzie jabłek
iloscJablek=10


#utworzenie funkcji waz
def waz():
    #tworzenie obiektu do przechowywania jablek
    obiektJablko=[]
    for nrJablko in range(0,iloscJablek):
        obiektJablko.append(jablko.Jablko())

    #inicjalizacja biblioteki
    pygame.init()
    #utworzenie okna gry i okreslenie jego rozmiarów
    oknoGry=pygame.display.set_mode((600,600),0,32)
    #ustawiamy nazwę okienka
    pygame.display.set_caption("Gra Wąż")
    #tworzymy zmienną, która przechowuje informacje czy gra jest uruchomiona
    run=True
   

  
    #pętla while sprawdza czy warunek w zmiennej run jest prawdziwy, jak jest nieprawdziwy kończy swoje działanie
    while(run):
        #Wypełnienie okna kolorem
        oknoGry.fill((0,0,0))
        #ustawienie opóźnienia odświeżania gry
        pygame.time.delay(200)
        #sprawdzanie czy istnieją jakieś zdarzenia i zapisanie ich do zmiennej "zdarzenia"
        for zdarzenia in pygame.event.get():
            #jeżeli zmienna "zdarzenia" przechowuje naciśniecie przycisku zamknij to zmieniamy wartosć zmiennej "run"
            if zdarzenia.type==pygame.QUIT:
                run=False
                #obsługa zdarzeń klawiatury i zmiana pozycji węża
            elif zdarzenia.type==pygame.KEYDOWN:
                if zdarzenia.key==pygame.K_RIGHT:
                    obiektWaz1.setDirection([1,0])
                elif zdarzenia.key==pygame.K_LEFT:
                    obiektWaz1.setDirection([-1,0])
                elif zdarzenia.key==pygame.K_UP:
                    obiektWaz1.setDirection([0,-1])
                elif zdarzenia.key==pygame.K_DOWN:
                    obiektWaz1.setDirection([0,1])
        #ustalenie nowej pozycji węża

        obiektWaz1.snakeMove()
                
       
        #pozycja głowy weza
        glowa=obiektWaz1.getHeadPosition()
        #pobieranie pozycji jablka
        for nrJablka in obiektJablko[::]:
            pozycjaJablka=nrJablka.getCoordinates()
            #zjadanie jabłka
            if glowa[0]==pozycjaJablka[0] and glowa[1] == pozycjaJablka[1]:
                nrJablka.randomPosition()
                obiektWaz1.addScore()
                obiektWaz1.addLenght()

            #rysowanie jabłka
            nrJablka.drawApple(oknoGry) 
        #rysowanie węża
        obiektWaz1.snakeDraw(oknoGry)
       
        #napisy na ekranie
        czcionka=pygame.font.SysFont('arial',25)
        tekst=czcionka.render("Zdobyłeś punkty: {0}".format(obiektWaz1.getPunkty()),1,(51,51,255))
        oknoGry.blit(tekst,(10,10))
        #aktualizowanie zawartości okna gry
        pygame.display.update()

#wywołanie funkcji, pozwala na uruchomienie gry
waz()