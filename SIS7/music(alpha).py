import pygame

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption("SoundPlay(ALPHA)")
pygame.display.set_icon(pygame.image.load('images/music.png'))
_songs = [
    'music/Дос-Мұқасан - 16 қыз.mp3',
    'music/Kilgore Doubtfire - Escape.mp3',
    'music/The Weeknd - Out of Time.mp3',
    'music/XXXtentacion - Jocelyn Flores.mp3',
    'music/Justin Bieber - Confident.mp3',
    'music/Post Malone - Circles.mp3'
]
covers = [
    pygame.image.load('images/0.jpg'),
    pygame.image.load('images/1.jpg'),
    pygame.image.load('images/2.jpg'),
    pygame.image.load('images/3.jpg'),
    pygame.image.load('images/4.jpg'),
    pygame.image.load('images/5.jpg')
]
done = True
i = 0

while done:
    for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = False

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_a]:
        pygame.mixer.music.load(_songs[i])
        pygame.mixer.music.play()
        screen.blit(covers[i], (0, 0))
    if i == 0:
        if pressed[pygame.K_RIGHT]:
            pygame.mixer.music.unload()
            i = i + 1
            screen.blit(covers[i], (0, 0))
            pygame.mixer.music.load(_songs[i])
            pygame.mixer.music.play()
        if pressed[pygame.K_LEFT]:
            pygame.mixer.music.unload()
            i = 5
            screen.blit(covers[i], (0, 0))
            pygame.mixer.music.load(_songs[i])
            pygame.mixer.music.play()
        if pressed[pygame.K_SPACE]: pygame.mixer.music.pause()
        if pressed[pygame.K_p]: pygame.mixer.music.unpause()
    elif i > 0 and i < 5:
        if pressed[pygame.K_RIGHT]:
            pygame.mixer.music.unload()
            i = i + 1
            screen.blit(covers[i], (0, 0))
            pygame.mixer.music.load(_songs[i])
            pygame.mixer.music.play()
        if pressed[pygame.K_LEFT]:
            pygame.mixer.music.unload()
            i = i - 1
            screen.blit(covers[i], (0, 0))
            pygame.mixer.music.load(_songs[i])
            pygame.mixer.music.play()
        if pressed[pygame.K_SPACE]: pygame.mixer.music.pause()
        if pressed[pygame.K_p]: pygame.mixer.music.unpause()
    elif i == 5:
        if pressed[pygame.K_RIGHT]: 
            pygame.mixer.music.unload()
            i = 0
            screen.blit(covers[i], (0, 0))
            pygame.mixer.music.load(_songs[i])
            pygame.mixer.music.play()
        if pressed[pygame.K_LEFT]:
            pygame.mixer.music.unload()
            i = i - 1
            screen.blit(covers[i], (0, 0))
            pygame.mixer.music.load(_songs[i])
            pygame.mixer.music.play()
        if pressed[pygame.K_SPACE]: pygame.mixer.music.pause()
        if pressed[pygame.K_p]: pygame.mixer.music.unpause()
    pygame.display.flip()
    clock.tick(15)