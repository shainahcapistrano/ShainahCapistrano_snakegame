import arcade
import random

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

## These numbers represent "states" that the game can be in.
GAME_INTRO = 1
GAME_RUNNING = 2
GAME_OVER = 3
TIMEBETWEENDROPS = 100


class Bunny(arcade.Sprite):
    def update(self):

        ## bounce off sides
        if self.left <= 0 or self.right >= SCREEN_WIDTH:
            self.change_x *= -1

        elif random.randrange(200) == 0:
            self.change_x *= -1

        self.center_x += self.change_x
        super(Bunny, self).update()


class MyApplication(arcade.Window):
    """ Main application class """

    def __init__(self, width, height):
        super().__init__(width, height)
        # Background image will be stored in this variable
        self.background = None

        self.frame_count = 0
        self.all_sprites_list = []
        self.Bunny = None
        self.lolli_list = []

        self.player = None
        self.score = 0
        self.score_text = None
        self.current_state = None
        self.dropTime = TIMEBETWEENDROPS
        self.difficulty = 70  ##Intial speed determiner

        # Do show the mouse cursor
        self.set_mouse_visible(True)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def setup(self):

        self.background = arcade.load_texture("./images/wall.jpg")
        self.all_sprites_list = arcade.SpriteList()
        self.lolli_list = arcade.SpriteList()
        # Score
        self.score = 0
        self.current_state = GAME_INTRO

        self.player = arcade.Sprite(":resources:images/tiles/plantPurple.png", 1)
        self.all_sprites_list.append(self.player)

        self.bunny = Bunny("../images/rabbit.png", 1)
        self.bunny.scale = .3
        self.bunny.center_x = 200
        self.bunny.center_y = SCREEN_HEIGHT - self.bunny.height
        self.bunny.angle = 0
        self.bunny.change_x = 1
        self.all_sprites_list.append(self.bunny)

    def on_draw(self):
        """Render the screen. """

        arcade.start_render()
        # Draw the background texture
        arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                                      SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

        if self.current_state == GAME_INTRO:
            arcade.draw_text("Welcome to Lolli Lunacy.", SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2 + 30, arcade.color.BLACK,
                             25)
            arcade.draw_text("Use the cake to catch the lollis.", SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, arcade.color.BLACK,
                             25)
            arcade.draw_text("Press the space bar to continue.", SCREEN_WIDTH // 3, (SCREEN_HEIGHT // 2 - 30),
                             arcade.color.BLACK, 25)

        elif self.current_state == GAME_RUNNING:
            self.draw_game()

        else:
            ##End game
            self.draw_game_over()

    def draw_game(self):

        self.bunny.draw()
        self.lolli_list.draw()
        self.player.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 550, arcade.color.BLACK, 14)

    def draw_game_over(self):
        """
        Draw "Game over" across the screen.
        """

        output = "Game Over"
        arcade.draw_text(output, 240, 400, arcade.color.WHITE, 54)

        if self.frame_count == 100:
            print("done")
            arcade.finish_render()
            arcade.close_window()

    def update(self, delta_time):
        """All the logic to move, and the game logic goes here. """

        # Use this if you want something to stay on the screen for a limited time
        self.frame_count += 1

        # Determine when to drop next lollipop
        if self.dropTime == 0:
            lolli = arcade.Sprite("../images/lollipopRed.png")
            lolli.scale = .5
            lolli.center_x = self.bunny.center_x
            lolli.angle = -90
            lolli.top = self.bunny.bottom
            lolli.change_y = -2

            self.lolli_list.append(lolli)
            self.all_sprites_list.append(lolli)
            self.dropTime = TIMEBETWEENDROPS * (random.randrange(self.difficulty, 100) / 100)

        else:
            self.dropTime = self.dropTime - 1

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player,
                                                        self.lolli_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for lolli in hit_list:
            lolli.kill()
            self.score += 10

        if self.score % 100 == 0 and self.score > 0 and self.difficulty > 0:
            self.difficulty -= 10

        # Get rid of the lolli when it flies off-screen
        for lolli in self.lolli_list:
            if lolli.top < 0:
                lolli.kill()
                self.current_state = GAME_OVER
                self.frame_count = 0

        self.lolli_list.update()
        self.bunny.update()

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """ Called whenever the mouse moves. """
        self.player.center_x = x
        self.player.center_y = 50

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            if self.current_state == GAME_INTRO:
                self.current_state= GAME_RUNNING
        elif key == arcade.key.ESCAPE:
            if self.current_state == GAME_OVER:
                self.close()



def main():
    """ Main method """
    window = MyApplication(SCREEN_WIDTH, SCREEN_HEIGHT)
    window.setup()
    arcade.run()


main()