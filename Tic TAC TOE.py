#========================================================================
####################  import "pygame"#########################

import pygame
import time

###################  constant variables ########################

pygame.init()

GAME_DISPLAY_WIDTH=600
GAME_DISPLAY_HEIGHT=600



BLACK=(0,0,0)
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)

###################  making screen for the game ##################

gameDisplay=pygame.display.set_mode((GAME_DISPLAY_WIDTH,GAME_DISPLAY_HEIGHT))

################## set caption for the game #####################

pygame.display.set_caption('TIC TAC TOE')

clock=pygame.time.Clock()

################# loadnig X and O images #########################

x_Img=pygame.image.load('x_image.png')
o_Img=pygame.image.load('o_image.png')

################# partition of the frame table ##################


partion={1:[(100,234),(100,234),'no_one',(167,167)],
             2:[(234,368),(100,234),'no_one',(301,167)],
             3:[(368,500),(100,234),'no_one',(435,167)],
             4:[(100,234),(234,368),'no_one',(167,301)],
             5:[(234,368),(234,368),'no_one',(301,301)],
             6:[(368,500),(234,368),'no_one',(435,301)],
             7:[(100,234),(368,500),'no_one',(167,435)],
             8:[(234,368),(368,500),'no_one',(301,435)],
             9:[(368,500),(368,500),'no_one',(435,435)]}

#============================================================================

def turns(player_turns): ##############  check everyone turns #########################
    font = pygame.font.SysFont(None,25)
    text=font.render(player_turns+" turns ",True,GREEN)
    gameDisplay.blit(text,(0,0))

###########################  display a message ###########################


def text_objects(text,font):
    textSurface=font.render(text,True,BLACK)
    return textSurface,textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',60)
    textSurf,textRect =  text_objects(text,largeText)
    textRect.center = ((GAME_DISPLAY_WIDTH/2),GAME_DISPLAY_HEIGHT/2)
    gameDisplay.blit(textSurf,textRect)
    pygame.display.update()

    time.sleep(2)








def drawLine(start_coord,end_coord):        ################### drawing the line of the frame #################
    pygame.draw.line(gameDisplay,RED,start_coord,end_coord,2)


def find_partion(partion,pos):   ################# finding what part player click #####################
    for item in partion:
        if partion[item][0][0] <pos[0] <partion[item][0][1] and partion[item][1][0] < pos[1] < partion[item][1][1]:
            print(item)
            return item
            break





def win(partion,meter):      ################## checking the winning with check every row and columns and dioug###########
    if partion[1][2]==str(meter) and partion[2][2]==str(meter) and partion[3][2]==str(meter):
        return True

    elif partion[4][2]==str(meter) and partion[5][2]==str(meter) and partion[6][2]==str(meter):
        return True

    elif partion[7][2]==str(meter) and partion[8][2]==str(meter) and partion[9][2]==str(meter):
        return True

    elif partion[1][2]==str(meter) and partion[4][2]==str(meter) and partion[7][2]==str(meter):
        return True

    elif partion[2][2]==str(meter) and partion[5][2]==str(meter) and partion[8][2]==str(meter):
        return True

    elif partion[3][2]==str(meter) and partion[6][2]==str(meter) and partion[9][2]==str(meter):
        return True

    elif partion[1][2]==str(meter) and partion[5][2]==str(meter) and partion[9][2]==str(meter):
        return True

    elif partion[3][2]==str(meter) and partion[5][2]==str(meter) and partion[7][2]==str(meter):
        return True
    else:
        return False




def draw(partion):      ################ check if the game being draw#########################
    counter=0
    for item in partion:
        if partion[item][2]!='no_one':
            counter+=1
    if counter==9:
        return True
    else:
        return False


def showing_ticks(partion): ##################  showing X & O images  #################
    for items in partion:
        if partion[items][2]=='1':
            gameDisplay.blit(x_Img,partion[items][3])

        if partion[items][2]=='2':
            gameDisplay.blit(o_Img,partion[items][3])








def gameLoop():

    GAP_FROM_SCREEN=100
    FRAME_DISPLAY_WIDTH = 400
    FRAME_DISPLAY_HEIGHT = 400
    FRAME_WIDTH=3

    pos=0
    fp_turn=True
    sp_turn=False

    winning=False
    drawing=False


    gameDisplay.fill(WHITE)
    pygame.draw.rect(gameDisplay, GREEN,
                     [GAP_FROM_SCREEN, GAP_FROM_SCREEN, FRAME_DISPLAY_WIDTH, FRAME_DISPLAY_HEIGHT],
                     FRAME_WIDTH)
    drawLine((234, 100), (234, 500))
    drawLine((368, 100), (368, 500))
    drawLine((100, 234), (500, 234))
    drawLine((100, 368), (500, 368))
    turns('first player')






    game_exit=False
    while not game_exit:


        pygame.display.update()
        clock.tick(30)

        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                game_exit=True

            if events.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                part=find_partion(partion, pos)
                if (fp_turn==True and partion[part][2]=='no_one'):
                    partion[part][2]='1'
                    fp_turn=False
                    sp_turn=True
                    winning=win(partion,'1')


                    if winning==True:
                        for items in partion:
                            showing_ticks(partion)
                        message_display('First Player win')
                        time.sleep(2)
                        game_exit=True

                    else:
                        drawing = draw(partion)
                        if drawing==True:
                            showing_ticks(partion)
                            message_display('DRAWING!')
                            time.sleep(2)
                            game_exit = True

                    gameDisplay.fill(WHITE)
                    pygame.draw.rect(gameDisplay, GREEN,
                                            [GAP_FROM_SCREEN, GAP_FROM_SCREEN, FRAME_DISPLAY_WIDTH, FRAME_DISPLAY_HEIGHT],
                                            FRAME_WIDTH)
                    drawLine((234, 100), (234, 500))
                    drawLine((368, 100), (368, 500))
                    drawLine((100, 234), (500, 234))
                    drawLine((100, 368), (500, 368))
                    showing_ticks(partion)

                    turns('second player')






                if sp_turn==True and partion[part][2]=='no_one':
                    partion[part][2] = '2'
                    fp_turn = True
                    sp_turn = False
                    winning = win(partion,'2')
                    drawing = draw(partion)

                    if winning==True:
                        showing_ticks(partion)
                        message_display('Second Player win')
                        time.sleep(2)
                        game_exit = True

                    else:
                        drawing = draw(partion)
                        if drawing==True:
                            showing_ticks(partion)
                            message_display('DRAWING!')
                            time.sleep(2)
                            game_exit = True

                    gameDisplay.fill(WHITE)
                    pygame.draw.rect(gameDisplay, GREEN,
                                                 [GAP_FROM_SCREEN, GAP_FROM_SCREEN, FRAME_DISPLAY_WIDTH, FRAME_DISPLAY_HEIGHT],
                                                 FRAME_WIDTH)
                    drawLine((234, 100), (234, 500))
                    drawLine((368, 100), (368, 500))
                    drawLine((100, 234), (500, 234))
                    drawLine((100, 368), (500, 368))
                    showing_ticks(partion)
                    turns('first player')





                print(pos)



            #if events.type == pygame.MOUSEBUTTONUP:
                #pos=0





gameLoop()
