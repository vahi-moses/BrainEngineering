import pygame as pg
from pygame.locals import *
import show
pg.init()

pg.display.init()
screen = pg.display.set_mode((800,600))

img=pg.image.load('neuron.png')

cortex = pg.Surface.copy(img)
STR= pg.Surface.copy(img)
STN= pg.Surface.copy(img)
SNC=pg.Surface.copy(img)
SNR= pg.Surface.copy(img)
GPE= pg.Surface.copy(img)
GPI= pg.Surface.copy(img)
Thal=pg.Surface.copy(img)

sncpos = 350,10
cortexpos = 200,150
strpos=350,150
gpepos=500,150
stnpos=500,300
gpipos=275,300
thalpos=200,450
snrpos=500,450
stimpos=70,465,100,60
button1pos=20,100,160,30
button2pos=20,140,160,30


def arrow(begin,end,pos):
    x1=40
    x2=86
    colarrow=(102, 153, 153)
    width=1
    if pos=='down':
        pg.draw.line(screen, colarrow, (begin[0]+x1,begin[1]+x2), (end[0]+x1,end[1]), width)
        pg.draw.line(screen,colarrow,(end[0]+x1,end[1]),(end[0]+x1+5,end[1]-5),width)
        pg.draw.line(screen, colarrow, (end[0] + x1, end[1]), (end[0] + x1-5, end[1] - 5), width)
    elif pos=='up':
        pg.draw.line(screen, colarrow, (begin[0] + x1, begin[1] + x2), (end[0] + x1, end[1]),width)
        pg.draw.line(screen, colarrow, (begin[0] + x1, begin[1]+x2), (begin[0] + x1-5, begin[1]+x2+5 ), width)
        pg.draw.line(screen, colarrow, (begin[0] + x1, begin[1] + x2), (begin[0] + x1+5, begin[1]+x2+5), width)

    elif pos=='left':
        pg.draw.line(screen, colarrow, (begin[0], begin[1] + x1), (end[0]+x2, end[1]+x1), width)
        pg.draw.line(screen, colarrow, (end[0]+x2 , end[1]+x1), (end[0] + x2 +5, end[1] + x1+5), width)
        pg.draw.line(screen, colarrow, (end[0]+x2, end[1] + x1), (end[0] + x2 + 5, end[1] + x1 - 5), width)
    elif pos=='right':
        pg.draw.line(screen, colarrow, (begin[0]+x2, begin[1]+x1), (end[0], end[1]+x1),width)
        pg.draw.line(screen, colarrow, (end[0], end[1] + x1), (end[0] -5, end[1] + x1 + 5), width)
        pg.draw.line(screen, colarrow, (end[0], end[1] + x1), (end[0] - 5, end[1] + x1 -5), width)
    elif pos=='left-down':
        pg.draw.line(screen, colarrow, (begin[0]+x1, begin[1]+86), (end[0]+80, end[1]), width)
        pg.draw.line(screen, colarrow, (end[0]+x1+40, end[1]), (end[0]+80, end[1]-5), width)
        pg.draw.line(screen, colarrow, (end[0] + x1+40, end[1]), (end[0]+85, end[1]), width)
    elif pos=='right-down':
        pg.draw.line(screen, colarrow, (begin[0] + x1, begin[1] + x2), (end[0] , end[1]+x1-40), width)
        pg.draw.line(screen, colarrow, (end[0] , end[1]+x1-40), (end[0]+2 , end[1]+x1-40-5),width)
        pg.draw.line(screen, colarrow, (end[0], end[1] + x1-40), (end[0]-5, end[1] + x1-40), width)
    elif pos=='rights':
        pg.draw.line(screen, colarrow, (begin[0]+100, begin[1] +30), (end[0] , end[1] + x1), width)
        pg.draw.line(screen, colarrow, (end[0], end[1] + x1), (end[0] - 5, end[1] + x1 + 5), width)
        pg.draw.line(screen, colarrow, (end[0], end[1] + x1), (end[0] - 5, end[1] + x1 - 5), width)

x=0
y=0
while 1:
    x, y = pg.mouse.get_pos()
    for e in pg.event.get():
        if e.type ==QUIT:
            exit()
        elif e.type == MOUSEBUTTONDOWN:
            x, y = pg.mouse.get_pos()
            if x>sncpos[0] and x<sncpos[0]+81 and y>sncpos[1] and y<sncpos[1]+86:
                print('SNC')
                show.show_snc()
            if x>cortexpos[0] and x<cortexpos[0]+81 and y>cortexpos[1] and y<cortexpos[1]+86:
                print('CORTEX')
                show.show_cortex()
            if x>strpos[0] and x<strpos[0]+81 and y>strpos[1] and y<strpos[1]+86:
                print('STR')
                show.show_str()
            if x>gpepos[0] and x<gpepos[0]+81 and y>gpepos[1] and y<gpepos[1]+86:
                print('GPE')
                show.show_gpe()
            if x>stnpos[0] and x<stnpos[0]+81 and y>stnpos[1] and y<stnpos[1]+86:
                print('STN')
                show.show_stn()
            if x>gpipos[0] and x<gpipos[0]+81 and y>gpipos[1] and y<gpipos[1]+86:
                print('GPI')
                show.show_gpi()
            if x>thalpos[0] and x<thalpos[0]+81 and y>thalpos[1] and y<thalpos[1]+86:
                print('THAL')
                show.show_thalamus()
            if x>snrpos[0] and x<snrpos[0]+81 and y>snrpos[1] and y<snrpos[1]+86:
                print('SNR')
                show.show_snr()
            if x>stimpos[0] and x<stimpos[0]+81 and y>stimpos[1] and y<stimpos[1]+86:
                print('STIM')
                show.show_stim()
            if x>button1pos[0] and x<button1pos[0]+ 160 and y>button1pos[1] and y<button1pos[1]+30:
                print('BUTTON 1')
                show.show_state_stim_cortex()
            if x>button2pos[0] and x<button2pos[0]+ 160 and y>button2pos[1] and y<button2pos[1]+30:
                print('BUTTON 2')
                show.show_state_stim_str()

    x1=20
    x2=86

    arrow(sncpos,strpos,'down')
    arrow(gpepos,stnpos,'down')
    arrow(cortexpos,thalpos,'up')
    arrow(cortexpos,strpos,'right')
    arrow(strpos,gpepos,'right')
    arrow(strpos,gpipos,'left-down')
    arrow(strpos,snrpos,'right-down')
    arrow(stnpos,snrpos,'down')
    arrow(snrpos,thalpos,'left')
    arrow(gpipos,thalpos,'left-down')
    arrow(stimpos,thalpos,'rights')

    font = pg.font.SysFont("georgia", 20)
    screen.fill((255,255,255))
    screen.blit(cortex,cortexpos)
    tcortex = font.render('Cortex', 1, (0, 0, 0))
    screen.blit(tcortex, (cortexpos[0]+x1, cortexpos[1]+x2))

    screen.blit(SNC,sncpos)
    tsnc = font.render('SNC', 1, (0, 0, 0))
    screen.blit(tsnc, (sncpos[0] + x1, sncpos[1] + x2))

    screen.blit(STN,stnpos )
    tstn = font.render('STN', 1, (0, 0, 0))
    screen.blit(tstn, (stnpos[0] + x1, stnpos[1] + x2))

    screen.blit(STR,strpos)
    tstr = font.render('STR', 1, (0, 0, 0))
    screen.blit(tstr, (strpos[0] + x1, strpos[1] + x2))

    screen.blit(GPE,gpepos)
    tgpe = font.render('GPE', 1, (0, 0, 0))
    screen.blit(tgpe, (gpepos[0] + x1, gpepos[1] + x2))

    screen.blit(GPI,gpipos)
    tgpi = font.render('GPI', 1, (0, 0, 0))
    screen.blit(tgpi, (gpipos[0] + x1, gpipos[1] + x2))

    screen.blit(Thal,thalpos)
    tthal = font.render('Thal', 1, (0, 0, 0))
    screen.blit(tthal, (thalpos[0] + x1, thalpos[1] + x2))

    screen.blit(SNR,snrpos)
    tsnr = font.render('SNR', 1, (0, 0, 0))
    screen.blit(tsnr, (snrpos[0] + x1, snrpos[1] + x2))

    pg.draw.rect(screen, (169, 169, 169), stimpos)
    tstim = font.render('stim', 1, (0, 0, 0))
    screen.blit(tstim, (stimpos[0] + x1, stimpos[1] + x2-20))

    fontbuttons = pg.font.SysFont("georgia", 15)
    pg.draw.rect(screen, (192, 192, 192), button1pos)
    tbutton1 = fontbuttons.render('SS - stim/cortex', 1, (0, 0, 0))
    screen.blit(tbutton1, (button1pos[0]+10, button1pos[1]+5))

    pg.draw.rect(screen, (192, 192, 192), button2pos)
    tbutton2 = fontbuttons.render('SS - stim/striatum', 1, (0, 0, 0))
    screen.blit(tbutton2, (button2pos[0]+10, button2pos[1]+5))




    arrow(sncpos, strpos, 'down')
    arrow(gpepos, stnpos, 'down')
    arrow(cortexpos, thalpos, 'up')
    arrow(cortexpos, strpos, 'right')
    arrow(strpos, gpepos, 'right')
    arrow(strpos, gpipos, 'left-down')
    arrow(strpos, snrpos, 'right-down')
    arrow(stnpos, snrpos, 'down')
    arrow(snrpos, thalpos, 'left')
    arrow(gpipos, thalpos, 'left-down')
    arrow(stimpos, thalpos, 'rights')
    pg.display.flip()
    pg.time.delay(30)

