import arcade
import random

SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480

class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def xoc(self):
        self.change_x *= -1
        self.change_y *= -1

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1

def colisio(a,b):
    distancia = math.sqrt(math.pow((a.position_x - b.position_x),2) + math.pow((a.position_y - b.position_y),2))
    #print(distancia)
    if distancia <= (a.radius) + (b.radius):
        return True
    else:
        return False

def rectangle():
    arcade.draw_lrtb_rectangle_filled(0, 639, 240, 0, arcade.csscolor.GREEN)

def abre (px,py):
    arcade.draw_rectangle_filled(-20+px, 200+px, -20+py, 20+py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(-20+px, 230+px, py, arcade.csscolor.DARK_GREEN)

def home (px,py):
    arcade.draw_rectangle_filled(px, 75+px, 0+py, 20+py, arcade.csscolor.BLUE)
    arcade.draw_rectangle_filled(15+px, 75+px, 0+py, 20+py, arcade.csscolor.BLUE)
    arcade.draw_rectangle_filled(7+px, 95+px, 20+py, 20+py, arcade.csscolor.BLUE)
    arcade.draw_rectangle_filled(7+px, 100+px, 50+py, py, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(7+px, 123+px, 5+py, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(3+px, 127+px, -6+py, arcade.csscolor.RED)
    arcade.draw_circle_filled(12+px, 127+px, -6+py, arcade.csscolor.RED)
    
def home1 (px,py):
    arcade.draw_rectangle_filled(-3+px, 72+px, 0+py, 20+py, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(12+px, 72+px, 0+py, 20+py, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(5+px, 89+px, 20+py, 20+py, arcade.csscolor.RED)
    arcade.draw_rectangle_filled(5+px, 97+px, 50+py, py, arcade.csscolor.RED)
    arcade.draw_circle_filled(5+px, 120+px, 5+py, arcade.csscolor.RED)
    arcade.draw_circle_filled(px, 124+px, -6+py, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(9+px, 124+px, -6+py, arcade.csscolor.BLUE)
    
class Meteorit(Ball):
    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        super().__init__(position_x, position_y, change_x, change_y, radius, color)
    
    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.position_y = SCREEN_HEIGHT 
            
        

class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.SKY_BLUE)

        # Draw a rectangle
        # Left of 0, right of 599
        # Top of 300, bottom of 0
        
        self.llista = []
        px=0
        for i in range(10):
            self.llista.append(Meteorit(random.randrange(px-50, px+80),random.randrange(-50, 50), 0,random.randrange(-3,-1), random.randrange(3, 4), arcade.color.ORANGE))
            self.llista.append(Meteorit(random.randrange(px-60, px+90),random.randrange(-150, 150), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.ORANGE))
            self.llista.append(Meteorit(random.randrange(px-70, px+100),random.randrange(-200, 200), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.ORANGE))
            self.llista.append(Meteorit(random.randrange(px-80, px+120),random.randrange(-250,250), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.ORANGE))
            self.llista.append(Meteorit(random.randrange(px-90, px+150),random.randrange(-300, 300), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.ORANGE))
            self.llista.append(Meteorit(random.randrange(px-100, px+170),random.randrange(-350, 350), 0, random.randrange(-3,-1), random.randrange(3, 4), arcade.color.ORANGE))
            px +=65
        

    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        rectangle()
        #abre(20,40)
        abre(67,40)
        home1(30,10)
        home(10,10)
        home(100,10)
        home(150,10)
        
        for i in self.llista:
            i.draw()
        
    

    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        for i in self.llista:
            i.update()
      
      
def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()