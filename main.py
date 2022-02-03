import pygame
import requests
import os
LON, LAT, SPN = 30.0, 55.005, 0.1
WIDTH, HEIGHT = size = 450, 450


def get_image(lon, lat, spn):
    params = {
        'l': 'map',
        'll': ','.join([str(lon), str(lat)]),
        'spn': ','.join([str(spn), str(spn)]),
        'size': ','.join([str(WIDTH), str(HEIGHT)])
    }
    request = requests.get('https://static-maps.yandex.ru/1.x/', params)
    with open('temporal.png', 'wb') as file:
        file.write(request.content)
    return pygame.image.load('temporal.png')


if __name__ == '__main__':
    running = True
    screen = pygame.display.set_mode(size)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.blit(get_image(LON, LAT, SPN), (0, 0))
        pygame.display.flip()
    pygame.quit()
    os.remove('temporal.png')
