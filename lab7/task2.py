import pygame
import os
pygame.init()
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock()
music_dir = "C:/Users/Alinur/Music" 
music_files = [os.path.join(music_dir, file) for file in os.listdir(music_dir) if file.endswith(".mp3")]
pygame.mixer.init()
current_song_index = 0
pygame.mixer.music.load(music_files[current_song_index])
def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_song_index])
    pygame.mixer.music.play()
def play_previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(music_files)
    pygame.mixer.music.load(music_files[current_song_index])
    pygame.mixer.music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
            elif event.key == pygame.K_RIGHT:
                play_next_song()
            elif event.key == pygame.K_LEFT:
                play_previous_song()
    clock.tick(30)
pygame.quit()
