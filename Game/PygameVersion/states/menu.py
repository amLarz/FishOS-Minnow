import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
selection = 0

# Spec Variables
screenWidth = 1280
screenHeight = 720

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and selection != 0:
                selection -= 1
            if event.key == pygame.K_DOWN and selection != 1: # CHANGE LATER ON WHEN MORE SELECTION CHOICES
                selection += 1
    # fill the screen with a color to wipe away anything from last frame
    screen.fill("black")

    # RENDER YOUR GAME HERE
    
    # Rendering the font
    font = pygame.font.Font(r"C:\FishOS-Minnow\Game\Game Assets\determination.ttf", size=100)
    subfont = pygame.font.Font(r"C:\FishOS-Minnow\Game\Game Assets\determination.ttf", size=50)

    # Main menu texts
    titleText1 = font.render("FishOS: ", True, (0, 107, 166))
    titleText2 = font.render("Minnow", True, (135, 206, 250))
    playText = subfont.render("Play", True, (0, 107, 166))
    Placeholder = subfont.render("PlaceHolder", True, "white")
    select = subfont.render("><))>", True, (135, 206, 250))

    # Centering Title text
    titleTextWidth = titleText1.get_width() + titleText2.get_width()
    titleTextHeight = max(titleText1.get_height(), titleText2.get_width())
    titleX = (screenWidth - titleTextWidth) // 2
    titleY = (screenHeight - titleTextHeight) // 2

    # Centering Button Texts
    playTextWidth = playText.get_width()
    playTextHeight = playText.get_height()
    playX = (screenWidth - playTextWidth) // 2
    playY = (screenHeight - playTextHeight) // 2

    # Position of texts
    screen.blit(titleText1, (titleX, titleY - 100)) # Getting the wanted height
    screen.blit(titleText2, (titleX + titleText1.get_width(), titleY - 100))
    screen.blit(playText, (playX, playY - 100))
    screen.blit(Placeholder, (playX, playY))
    

    # Selection
    # select appears on start first, when moved then it will disappear and go to another one
    
    if selection == 0:
        screen.blit(select, (playX - 130, playY - 100))
    
    if selection == 1:
        screen.blit(select, (playX - 130, playY))


    




    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()