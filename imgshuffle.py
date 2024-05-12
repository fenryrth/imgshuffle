import os
import json
import pygame
import random
from pygame.locals import *

def load_config():
    try:
        with open('config.json', 'r') as config_file:
            return json.load(config_file)
    except FileNotFoundError:
        print("The configuration file was not found.")
        raise SystemExit
    except json.JSONDecodeError:
        print("Configuration file is not a valid JSON.")
        raise SystemExit

def load_images(folder):
    supported_formats = ('.png', '.jpg', '.jpeg', '.bmp', '.webp')
    images = []
    for f in os.listdir(folder):
        if f.endswith(supported_formats):
            try:
                full_path = os.path.join(folder, f)
                img = pygame.image.load(full_path)
                images.append(img)
            except Exception as e:
                print(f"Failed to load image {full_path}: {e}")
    if not images:
        print("No images could be loaded.")
        raise SystemExit
    random.shuffle(images)  # Shuffle the list of images
    return images
    
def scale_image(image, screen_size):
    image_rect = image.get_rect()
    screen_rect = pygame.Rect(0, 0, *screen_size)
    scaling_factor = min(screen_rect.width / image_rect.width, screen_rect.height / image_rect.height)

    # Calculate the new dimensions preserving the aspect ratio
    new_width = int(image_rect.width * scaling_factor)
    new_height = int(image_rect.height * scaling_factor)

    # Use smoothscale instead of scale for better anti-aliasing
    scaled_image = pygame.transform.smoothscale(image, (new_width, new_height))

    # Calculate position to center the image
    x = (screen_rect.width - new_width) // 2
    y = (screen_rect.height - new_height) // 2

    return scaled_image, (x, y)

def main():
    try:
        pygame.init()
        config = load_config()
        screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.mouse.set_visible(False)  # Hide the mouse cursor
    except Exception as e:
        print(f"Failed to initialize Pygame or load configuration: {e}")
        raise SystemExit

    images = load_images(config['image_folder'])
    if not images:
        print("No images to display, exiting.")
        pygame.quit()
        raise SystemExit

    clock = pygame.time.Clock()
    run = True
    current_image = 0
    image_timer = 0  # Timer to manage image display duration

    while run:
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    run = False

        if image_timer > config['display_time'] * 1000:
            current_image = (current_image + 1) % len(images)
            image_timer = 0  # Reset timer

            # Fade effect
            for alpha in range(0, 255, 5):
                fade_surface = pygame.Surface(screen.get_size())
                fade_surface.fill((0, 0, 0))
                fade_surface.set_alpha(alpha)
                screen.blit(fade_surface, (0, 0))
                pygame.display.update()
                pygame.time.delay(10)  # Delay for fade effect

        screen.fill((0, 0, 0))  # Fill the background with black

        # Scale and display the image
        image, position = scale_image(images[current_image], screen.get_size())
        screen.blit(image, position)

        pygame.display.flip()  # Update the full display
        clock.tick(60)  # Maintains a steady frame rate
        image_timer += clock.get_time()  # Update the timer based on time elapsed since last tick

    pygame.quit()

if __name__ == "__main__":
    main()
