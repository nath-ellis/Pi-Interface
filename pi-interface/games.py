"""
Games for the game service

Games must be a class which has draw(screen), update(), manage_events(e) and reset()
For the game to be run a GameMenuItem(x, y, icon, name, game_class) must be added to services.games.menu_items
When it is chosen by the user update() and draw() are ran at the speed of values.Settings.fps
reset() is run when a player presses the cross which is visible in every game (this is so that if a player wishes
to play the game again it starts how it should instead of resuming where they left off)
manage_events(e) is also ran at the speed of values.Settings.fps and is for operations which require an event such
as pygame.MOUSEBUTTONDOWN
"""

import os.path
import random
from values import *
import pygame


class FlappyBird:
    """
    Flappy Bird Game
    """


    class Player:
        """
        The Player
        """

        def __init__(self):
            self.icons = [
                pygame.image.load(
                    os.path.join("../assets/games/flappybird", "bird_1.png")
                ),
                pygame.image.load(
                    os.path.join("../assets/games/flappybird", "bird_2.png")
                ),
                pygame.image.load(
                    os.path.join("../assets/games/flappybird", "bird_3.png")
                ),
                pygame.image.load(
                    os.path.join("../assets/games/flappybird", "bird_2.png")
                )
            ]
            self.rect = pygame.Rect(50, 50, self.icons[0].get_width(), self.icons[0].get_height())
            self.y_velocity = 10
            self.is_jumping = False
            self.jump_height = 10
            self.animation_frame = 0
            self.animation_speed = 2  # Lower the faster


        def draw(self, screen: pygame.surface):
            """
            Draws the player's animation
            :param screen: pygame surface for sprites to be drawn on
            """

            screen.blit(
                self.icons[self.animation_frame],
                (self.rect.x, self.rect.y)
            )

            if self.animation_speed <= 0:
                if self.animation_frame == len(self.icons) - 1:
                    self.animation_frame = 0
                else:
                    self.animation_frame += 1

                self.animation_speed = 2
            else:
                self.animation_speed -= 1


        def manage_jumps(self):
            """
            The player's controls
            """

            if self.is_jumping:
                if self.jump_height >= -10:
                    self.rect.y -= self.jump_height
                    self.jump_height -= 1
                else:
                    self.jump_height = 10
                    self.is_jumping = False
            else:
                self.rect.y += self.y_velocity  # Gravity


        def controls(self, e):
            """
            Controls for jumping
            :param e: pygame event
            """

            if e.type == pygame.MOUSEBUTTONDOWN and not self.is_jumping:
                self.is_jumping = True

            if self.is_jumping:
                if e.type == pygame.MOUSEBUTTONDOWN and self.jump_height <= 0:
                    self.jump_height = 10


    class Pipe:
        """
        The pipes
        """


        def __init__(self, x, y, upper_icon, lower_icon):
            self.upper_icon = upper_icon
            self.upper_rect = pygame.Rect(
                x,
                y,
                self.upper_icon.get_width(),
                self.upper_icon.get_height()
            )
            self.lower_icon = lower_icon
            self.lower_rect = pygame.Rect(
                x,
                y + self.upper_icon.get_height() + random.randint(70, 100),
                self.lower_icon.get_width(),
                self.lower_icon.get_height()
            )


        def move(self, speed):
            """
            Moves the pipe left
            """

            if self.upper_rect.x <= -self.upper_icon.get_width():
                self.lower_rect.y = self.upper_rect.y + self.upper_icon.get_height() + random.randint(70, 100)
                self.upper_rect.x = 520
                self.lower_rect.x = 520
            self.upper_rect.x -= speed
            self.lower_rect.x -= speed


        def draw(self, screen: pygame.surface):
            """
            Draws the pipe
            :param screen: pygame surface
            """

            screen.blit(self.upper_icon, (self.upper_rect.x, self.upper_rect.y))
            screen.blit(self.lower_icon, (self.lower_rect.x, self.lower_rect.y))


        def is_colliding(self, player):
            """
            Gets whether the pipe is colliding with the player
            :param player: player
            :return bool, bool: upper_colliding, lower_colliding
            """

            upper_colliding = self.upper_rect.colliderect(player)
            lower_colliding = self.lower_rect.colliderect(player)

            return upper_colliding, lower_colliding



    def __init__(self):
        self.player = self.Player()
        self.bg = pygame.image.load(
            os.path.join("../assets/games/flappybird", "bg.png")
        )
        self.bg_1_x = 0
        self.bg_2_x = self.bg.get_width()
        self.speed = 5
        # Only loads the sprites once
        self.pipe_upper_icon = pygame.image.load(
                os.path.join("../assets/games/flappybird", "upper_pipe.png")
            )
        self.pipe_lower_icon = pygame.image.load(
            os.path.join("../assets/games/flappybird", "lower_pipe.png")
        )
        self.pipes = [
            self.Pipe(520, -random.randint(0, 80), self.pipe_upper_icon, self.pipe_lower_icon),
            self.Pipe(720, -random.randint(0, 80), self.pipe_upper_icon, self.pipe_lower_icon),
            self.Pipe(920, -random.randint(0, 80), self.pipe_upper_icon, self.pipe_lower_icon)
        ]
        self.state = "menu"
        self.logo = pygame.image.load(
            os.path.join("../assets/games/flappybird", "flappy_bird.png")
        )
        self.input_prompt = pygame.image.load(
            os.path.join("../assets/games/flappybird", "input_prompt.png")
        )
        self.game_over_img = pygame.image.load(
            os.path.join("../assets/games/flappybird", "game_over.png")
        )
        self.start_buffer = 5  # To stop the game from immediately starting when clicked


    def draw(self, screen: pygame.surface):
        """
        For drawing the game's assets
        :param screen: pygame surface for sprites to be drawn on
        """

        screen.fill(Theme.background_colour)

        # Don't draw it if it is off the screen
        if not self.bg_1_x > Values.screen.get_width():
            screen.blit(self.bg, (self.bg_1_x, 0))
        if not self.bg_2_x > Values.screen.get_width():
            screen.blit(self.bg, (self.bg_2_x, 0))

        if self.state == "menu":
            screen.blit(self.logo, (144, 40))
            screen.blit(self.input_prompt, (174, 140))
        elif self.state == "game" or self.state == "game_over":
            for p in self.pipes:
                p.draw(screen)

            self.player.draw(screen)

        if self.state == "game_over":
            screen.blit(self.game_over_img, (144, 40))
            screen.blit(self.input_prompt, (174, 140))


    def update(self):
        """
        For updating the game
        """

        if self.state == "menu":
            self.start_buffer -= 1

        elif self.state == "game":
            # If player goes off the screen
            if self.player.rect.y > Values.screen.get_height() or self.player.rect.y < -100:
                self.state = "game_over"

            # Moves the backgrounds
            if self.bg_1_x <= -552:
                self.bg_1_x = self.bg_2_x + self.bg.get_width()
            self.bg_1_x -= self.speed

            if self.bg_2_x <= -552:
                self.bg_2_x = self.bg_1_x + self.bg.get_width()
            self.bg_2_x -= self.speed

            # Moves pipes and checks collisions
            for p in self.pipes:
                if p.is_colliding(self.player)[0] or p.is_colliding(self.player)[1]:
                    self.state = "game_over"

                p.move(self.speed)

            self.player.manage_jumps()


    def manage_events(self, e):
        """
        Manages events such as MOUSEBUTTONDOWN
        :param e: pygame event
        """

        if self.state == "menu":
            if e.type == pygame.MOUSEBUTTONDOWN and self.start_buffer <= 0:
                self.state = "game"
        elif self.state == "game":
            self.player.controls(e)
        else:
            if e.type == pygame.MOUSEBUTTONDOWN:
                self.reset("game")


    def reset(self, state = "menu"):
        """
        For resetting the game when closed
        """

        self.player = self.Player()
        self.speed = 5
        self.pipes = [
            self.Pipe(520, -random.randint(0, 80), self.pipe_upper_icon, self.pipe_lower_icon),
            self.Pipe(720, -random.randint(0, 80), self.pipe_upper_icon, self.pipe_lower_icon),
            self.Pipe(920, -random.randint(0, 80), self.pipe_upper_icon, self.pipe_lower_icon)
        ]
        self.state = state
        self.start_buffer = 5

