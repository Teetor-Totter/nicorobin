import pygame

pygame.init()

GENISLIK_YUKSEKLIK=1360,700
pencere=pygame.display.set_mode(GENISLIK_YUKSEKLIK)
altekran=pygame.image.load("yeşil ekran.png")
altekran_koordinat=altekran.get_rect()
altekran_koordinat.topleft=(0,350)
üstekran=pygame.image.load("üst ekran.png")
üstekran_koordinat=üstekran.get_rect()
üstekran_koordinat.topleft=(0,0)
yangintupu=pygame.image.load("yangın tüpü.png")
yangintupu_koordinat=yangintupu.get_rect()
yangintupu_koordinat.topleft=(1200,307)
yangintupu2=pygame.image.load("yangın tüpü.png")
yangintupu2_koordinat=yangintupu2.get_rect()
yangintupu2_koordinat.topleft=(1150,307)


durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
    pencere.blit(altekran,altekran_koordinat)
    pencere.blit(üstekran,üstekran_koordinat)
    pencere.blit(yangintupu,yangintupu_koordinat)
    pencere.blit(yangintupu2,yangintupu2_koordinat)
    pygame.display.update()
pygame.quit()