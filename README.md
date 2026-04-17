# My-First-Game
Simple game like mole-hitting game

## How-to-run
* $ indicates prompt
* $ pip install pygame
* $ python game1.py

## Features
* Random target spawning
* Score system
* Time limit (30 seconds)
* Life system
* Visual hit effects (“BEAT!!”)

## Highlights
* Prevent overlapping targets using collision detection
* Smooth object management using lists (targets[:])
* Dynamic effects system for visual feedback

## Tech Stack
* Python
* Pygame
  
## Future Goals
* I'll consider about it through playing and watching some games like this

## New Knowledges for Me
* game is made by "loop & state managements"
* I can prevent overlapping to use collision detection to prevent overlapping objects
* I can avoid runtime errors during removal to apply safe list iteration (`targets[:]`)
* I can implement time-based mechanics using `pygame.time.get_ticks()` and loop sentences to realize time-limit and manage object lifetime

## Methods Used
* `pygame.init()` – Initialize the game
* `pygame.display.set_mode()` – Create game window
* `pygame.time.Clock()` – Control frame rate
* `pygame.image.load()` – Load images
* `pygame.transform.scale()` – Resize images
* `pygame.font.SysFont()` – Create font object
* `pygame.event.get()` – Handle events
* `pygame.Rect()` – Create rectangles for collision detection
* `colliderect()` – Check collision between objects
* `collidepoint()` – Detect mouse click on object
* `screen.blit()` – Draw images on screen
* `pygame.draw.circle()` – Draw visual effects
* `font.render()` – Render text
* `pygame.time.get_ticks()` – Get elapsed time
* `pygame.display.flip()` – Update display
* `clock.tick()` – Limit FPS

## Comments
* I'm japanese student and I'm major in programming. I want to make AI and some games which add AI. This is first step. I want to make more game day by day.
