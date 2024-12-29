import pygame
import time
import random

#INITIALIZES FONT MODULE
pygame.font.init()

#ASSIGN HEIGHT AND WIDTH OF WINDOW
WIDTH , HEIGHT = 1400 , 890

#CREATES A SPECIFIED SIZE WINDOW FOR PYGAME 
WIN = pygame.display.set_mode((WIDTH , HEIGHT))

#SETS THE CAPTIONS FOR PYGAME WINDOW
pygame.display.set_caption("Space dodge")

#LOADS A BACKGROUND IMAGE
BG = pygame.transform.scale(pygame.image.load('/Users/somnathshinde/programming/game1/ai-generated-ethereal-cosmic-landscape-with-vibrant-nebula-and-stars-photo.jpeg'), (WIDTH , HEIGHT))

#SETS THE HEIGHT, WIDTH AND VELOCITY OF PLAYER
PLAYER_HEIGHT = 40
PLAYER_WIDTH =  60
PLAYER_VEL = 5

#SETS THE HEIGHT, WIDTH AND VELOCITY OF THE STARS
STAR_WIDTH = 10
STAR_HEIGHT = 20
STAR_VEL = 3

#SETS THE TYPE AND SIZE OF FONT
FONT = pygame.font.SysFont("comicsans", 30)

#DEFINE A FUNCTION FOR DRAWING ITEMS ON THE WINDOW
def draw(player, elapsed_time, stars):

    #TAKES BACKGROUND AND DRAW IT ONTO WINDOW AT SPECIFIED COORDINATES
    WIN.blit(BG, (0,0))

    #RENDERS THE TEXT
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10,10))

    #DRAWS A PLAYER ON WINDOW
    pygame.draw.rect(WIN, "red", player)

    #DRAWS STARS ON THE WINDOW
    for star in stars:
        pygame.draw.rect(WIN, "white", star)

    #UPDATES THE DISPLAY
    pygame.display.update()

#CREATE A main() FUNCTION
def main():
    run = True

    #ASSIGNS COORDINATES X, Y AND HEIGHT, WIDTH OF PLAYER
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)

    #SETS START TIME AND ELAPSED TIME FOR ARRIVAL OF THE STARS
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    #INITIALIZES THE NUMBER OF STARS AND INCREMENTATION TIME OF STARS
    star_add_increment = 2000
    star_count = 0

    #CREATE AN EMPTY LIST OF STARS
    stars =[]
    hit = False

    #WHILE LOOP FOR ADDING THE STARS ON WINDOW
    while run:
        star_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        #CHECKS FOR CONDITION AND ADDS STARS TO THE WINDOW
        if star_count > star_add_increment:
            for _ in range(3):
                star_x = random.randint(0, WIDTH - STAR_WIDTH)
                star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
                stars.append(star)

            star_add_increment = max(200, star_add_increment - 50)
            star_count = 0 

        #HELPS IN QUITING THE GAME
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break
        
        #THIS TRIGGERS WHICH KEYS ARE PRESSED AND PERFORMS SPECIFIED ACTION
        keys = pygame.key.get_pressed()

        #MOVES THE PLAYER TO THE LEFT IF LEFT_ARROW IS PRESSED
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL

        #MOVES THE PLAYER TO THE RIGHT IF RIGHT_ARROW IS PRESSED
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <=  WIDTH:
            player.x += PLAYER_VEL

        #FOR LOOP FOR CONTROLLING THE STARS
        for star in stars[:]:
            star.y += STAR_VEL
            if star.y > HEIGHT:
                stars.remove(star)
            elif star.y + star.height >= player.y and star.colliderect(player):
                stars.remove(star)
                hit = True
                break

        #IF THE STARS HIT THE PLAYER IT IMMIDIATELY STOPS THE GAME
        if hit:
            lost_text = FONT.render("You Lost!",1,"white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        #CALLS THE DRAW FUNCTION
        draw(player, elapsed_time, stars)

    #QUITS THE GAME
    pygame.quit()
    
#CHECKS IF THE SCRIPT IS RUN DIRECTLY AND NOT IMPORTED
if __name__ == "__main__":

    #CALLS main() FUNCTION
    main()

