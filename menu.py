import pygame_menu
import pygame
#import pliku z grą
import waz

def wlaczGre():
    waz.waz()
def zmienJablka(tekst,ilosc):
    waz.iloscJablek=ilosc;
def zmienKolorWaz1(kolor):
    waz.ustawKolorWaz1(kolor)
def zmienKolorWaz2(kolor):
    waz.ustawKolorWaz2(kolor)
def main():
    pygame.init()
    #utworzenie okna gry i okreslenie jego rozmiarów
    oknoGry=pygame.display.set_mode((600,600),0,32)
    #ustawiamy nazwę okienka
    pygame.display.set_caption("Wąż")
    menu=pygame_menu.Menu("Gra Wąż 3TIE",600,600,theme=pygame_menu.themes.THEME_ORANGE)
    menu.add.button('Uruchom grę',wlaczGre,background_color=(0,255,0))
    menu.add.selector("Wybierz ilośc jabłek",[('jedno',1),('dwa',2),('pięć',5),('dziesięć',10),('dwadzieścia',20)],onchange=zmienJablka)
    menu.add.color_input("Kolor pierwszego gracza:",'rgb',default=(100,100,100),onreturn=zmienKolorWaz1)
    menu.add.color_input("Kolor drugiego gracza:",'rgb',default=(100,100,100),onreturn=zmienKolorWaz2)
    menu.add.selector("Wybierz rozdzielczość gry", [('600x600',(600,600)),('900x900',(900,900)),('900x600',(900,600)),('1200x900',(1200,900))])
    menu.mainloop(oknoGry)
main()