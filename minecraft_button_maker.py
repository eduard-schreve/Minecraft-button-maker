# minecraft knoppie groottes: 400 x 40

import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 200), pygame.RESIZABLE)
clock = pygame.time.Clock()
running = True

btnSize = (400, 40)
btnSurf = pygame.Surface(btnSize)
pressBtnSurf = pygame.Surface(btnSize)
trans_btnSurf = pygame.Surface(btnSize, pygame.SRCALPHA)
trans_pressBtnSurf = pygame.Surface(btnSize, pygame.SRCALPHA)

myfont = pygame.font.Font("Minecraft.ttf", 16)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill((255, 255, 255))

    blue = pygame.image.load("blue texture.png").convert()
    grey = pygame.image.load("grey texture.png").convert()

    # get the text surfaces:
    text = "Start"
    blueTextSurf = myfont.render(text, True, (255, 255, 160))
    shadeBlueTextSurf = myfont.render(text, True, (63, 63, 40))
    greyTextSurf = myfont.render(text, True, (224, 224, 224))
    shadeGreyTextSurf = myfont.render(text, True, (56, 56, 56))

    # resize the surfaces:
    if pygame.mouse.get_pressed()[0]:
        btnSurf = pygame.transform.scale(btnSurf, pygame.mouse.get_pos())
        pressBtnSurf = pygame.transform.scale(pressBtnSurf, pygame.mouse.get_pos())
        trans_btnSurf = pygame.transform.scale(trans_btnSurf, pygame.mouse.get_pos())
        trans_pressBtnSurf = pygame.transform.scale(trans_pressBtnSurf, pygame.mouse.get_pos())

    # render the texture:
    for x in range(int(btnSurf.get_width() / 30) + 1):
        btnSurf.blit(grey, (x * 30, 0))
        pressBtnSurf.blit(blue, (x * 30, 0))
        for y in range(int(btnSurf.get_height() / 30) + 1):
            btnSurf.blit(grey, (x * 30, y * 30))
            pressBtnSurf.blit(blue, (x * 30, y * 30))

    # draw the outline:
    pygame.draw.line(btnSurf, (0, 0, 0), (0, 0), (btnSurf.get_width(), 0), 2) # top
    pygame.draw.line(btnSurf, (0, 0, 0), (0, 0), (0, btnSurf.get_height()), 2) # left
    pygame.draw.line(btnSurf, (0, 0, 0), (btnSurf.get_width() - 2, 0), 
                        (btnSurf.get_width() - 2, btnSurf.get_height()), 2) # right
    pygame.draw.line(btnSurf, (0, 0, 0), (0, btnSurf.get_height() - 2), 
                        (btnSurf.get_width(), btnSurf.get_height() - 2), 2) # bottom

    pygame.draw.line(pressBtnSurf, (0, 0, 0), (0, 0), (pressBtnSurf.get_width(), 0), 2) # top
    pygame.draw.line(pressBtnSurf, (0, 0, 0), (0, 0), (0, pressBtnSurf.get_height()), 2) # left
    pygame.draw.line(pressBtnSurf, (0, 0, 0), (pressBtnSurf.get_width() - 2, 0), 
                        (pressBtnSurf.get_width() - 2, pressBtnSurf.get_height()), 2) # right
    pygame.draw.line(pressBtnSurf, (0, 0, 0), (0, pressBtnSurf.get_height() - 2), 
                        (pressBtnSurf.get_width(), pressBtnSurf.get_height() - 2), 2) # bottom

    # draw the shading:
    pygame.draw.line(btnSurf, (170, 170, 170), (2, 2), (btnSurf.get_width() - 3, 2), 2) # top
    pygame.draw.line(btnSurf, (170, 170, 170), (2, 2), (2, btnSurf.get_height() - 3), 2) # left
    pygame.draw.line(trans_btnSurf, (0, 0, 0, 57), (btnSurf.get_width() - 4, 2), 
                     (btnSurf.get_width() - 4, btnSurf.get_height() - 2), 2) # right
    pygame.draw.line(trans_btnSurf, (0, 0, 0, 57), (2, btnSurf.get_height() - 5), 
                     (btnSurf.get_width() - 2, btnSurf.get_height() - 5), 4) # bottom

    pygame.draw.line(pressBtnSurf, (190, 199, 255), (2, 2), (pressBtnSurf.get_width() - 3, 2), 2) # top
    pygame.draw.line(pressBtnSurf, (190, 199, 255), (2, 2), (2, pressBtnSurf.get_height() - 3), 2) # left
    pygame.draw.line(trans_pressBtnSurf, (0, 0, 0, 57), (trans_pressBtnSurf.get_width() - 4, 2), 
                     (trans_pressBtnSurf.get_width() - 4, trans_pressBtnSurf.get_height() - 2), 2) # right
    pygame.draw.line(trans_pressBtnSurf, (0, 0, 0, 57), (2, trans_pressBtnSurf.get_height() - 5), 
                     (trans_pressBtnSurf.get_width() - 2, trans_pressBtnSurf.get_height() - 5), 4) # bottom

    # render the text:
    btnSurf.blit(shadeGreyTextSurf, ((btnSurf.get_width() - greyTextSurf.get_width()) / 2 + 2, 
                                     (btnSurf.get_height() - greyTextSurf.get_height()) / 2 + 2))
    btnSurf.blit(greyTextSurf, ((btnSurf.get_width() - greyTextSurf.get_width()) / 2,
                                (btnSurf.get_height() - greyTextSurf.get_height()) / 2))
    pressBtnSurf.blit(shadeBlueTextSurf, ((pressBtnSurf.get_width() - greyTextSurf.get_width()) / 2 + 2, 
                                     (pressBtnSurf.get_height() - greyTextSurf.get_height()) / 2 + 2))
    pressBtnSurf.blit(blueTextSurf, ((pressBtnSurf.get_width() - greyTextSurf.get_width()) / 2, 
                                (pressBtnSurf.get_height() - greyTextSurf.get_height()) / 2))

    # put it on the screen:
    btnSurf.blit(trans_btnSurf, (0, 0))
    screen.blit(btnSurf, (0, 0))

    pressBtnSurf.blit(trans_pressBtnSurf, (0, 0))
    screen.blit(pressBtnSurf, (0, btnSurf.get_height() + 2))

    if pygame.mouse.get_pressed()[2]:
        pygame.image.save(btnSurf, "button.png")
        pygame.image.save(pressBtnSurf, "pressed_button.png")
        print("Saving...")

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()