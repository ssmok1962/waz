#pobranie biblioteki pygame
import random
import pygame

#utworzenie funkcji waz
def waz():
    #inicjalizacja biblioteki
    pygame.init()
    #utworzenie okna gry i okreslenie jego rozmiarów
    oknoGry=pygame.display.set_mode((600,600),0,32)
    #ustawiamy nazwę okienka
    pygame.display.set_caption("Gra Wąż")
    #tworzymy zmienną, która przechowuje informacje czy gra jest uruchomiona
    run=True
    #pozyvje startowe węża
    zmiennaX=300
    zmiennaY=300
    #stworzenie listy z pozycjami dla weza
    pozycjaWaz=[(zmiennaX,zmiennaY)]
    #dlugosc weza
    dlugoscWaz=1
    #pozycja startowa jabłka
    jablkoX=random.randint(0,19)*30
    jablkoY=random.randint(0,19)*30
    #liczba punktów
    punkty=0
    #kierunek początkowy węża
    #[1,0] - ruch w prawo
    #[0,1] - ruch w dół
    #[-1,0] - ruch w lewo
    #[0,-1] - ruch w górę
    kierunek=[1,0]
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
                    kierunek=[1,0]
                elif zdarzenia.key==pygame.K_LEFT:
                    kierunek=[-1,0]
                elif zdarzenia.key==pygame.K_UP:
                    kierunek=[0,-1]
                elif zdarzenia.key==pygame.K_DOWN:
                    kierunek=[0,1]
        #ustalenie nowej pozycji węża
        zmiennaX=zmiennaX+kierunek[0]*30;
        zmiennaY=zmiennaY+kierunek[1]*30;
             
        #sprawdzanie krawędzi
        if zmiennaX>=600:
            zmiennaX=0
        if zmiennaX<0:
            zmiennaX=600-30
        if zmiennaY>=600:
            zmiennaY=0
        if zmiennaY<0:
            zmiennaY=600-30
        #dodanie nowej pozycji wezado listy
        pozycjaWaz.append((zmiennaX,zmiennaY))   

        #dodanie kształtu do okienka
        #zjadanie jabłka
        if zmiennaX==jablkoX and zmiennaY == jablkoY:
            jablkoX=random.randint(0,19)*30
            jablkoY=random.randint(0,19)*30
            punkty+=1 #punkty=punkty+1
            dlugoscWaz=dlugoscWaz+1

        #rysowanie jabłka
        pygame.draw.circle(oknoGry,(255,0,0),(jablkoX+15,jablkoY+15),15)

        #rysowanie węża
        if len(pozycjaWaz)>dlugoscWaz:
            del pozycjaWaz[0]
            #petla rysujaca weza
        for poz in pozycjaWaz[::-1]:
        #definiujemy kształ węża
            ksztaltWaz=pygame.Rect((poz[0],poz[1]),(30,30))
            #dodanie ksztaltu do okienka
            pygame.draw.rect(oknoGry,(100,100,100),ksztaltWaz)
        #napisy na ekranie
        czcionka=pygame.font.SysFont('arial',25)
        tekst=czcionka.render("Zdobyłeś punkty: {0}".format(punkty),1,(51,51,255))
        oknoGry.blit(tekst,(10,10))
        #aktualizowanie zawartości okna gry
        pygame.display.update()

#wywołanie funkcji, pozwala na uruchomienie gry
waz()