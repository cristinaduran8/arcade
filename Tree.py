# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the dimensions (width and height)
arcade.open_window(600, 600, "Drawing Example")



# Get ready to draw
arcade.start_render()

# Draw a rectangle
# Left of 0, right of 599
# Top of 300, bottom of 0
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)

def abre (px,py):
    arcade.draw_rectangle_filled(px, 220+px, py, 40+py, arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(px, 250+px, 20+py, arcade.csscolor.DARK_GREEN)

abre(20,20)

"""
# Tree trunk
arcade.draw_rectangle_filled(100, 320, 20, 60, arcade.csscolor.SIENNA)

# Tree top
arcade.draw_circle_filled(100, 350, 30, arcade.csscolor.DARK_GREEN)
"""

# Home

def home (px,py):
    arcade.draw_rectangle_filled(px, 75+px, 0+py, 20+py, arcade.csscolor.BLUE)
    
    arcade.draw_rectangle_filled(15+px, 75+px, 0+py, 20+py, arcade.csscolor.BLUE)
    arcade.draw_rectangle_filled(7+px, 95+px, 20+py, 20+py, arcade.csscolor.BLUE)
    arcade.draw_rectangle_filled(7+px, 100+px, 50+py, py, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(7+px, 123+px, 5+py, arcade.csscolor.BLUE)
    arcade.draw_circle_filled(3+px, 127+px, -6+py, arcade.csscolor.RED)
    arcade.draw_circle_filled(12+px, 127+px, -6+py, arcade.csscolor.RED)
    
home(10,10)
home(100,10)
home(200,10)





"""
arcade.draw_rectangle_filled(240, 305, 10, 30, arcade.csscolor.BLUE)
arcade.draw_rectangle_filled(285, 305, 10, 30, arcade.csscolor.BLUE)
arcade.draw_rectangle_filled(277, 325, 30, 30, arcade.csscolor.BLUE)
arcade.draw_rectangle_filled(277, 330, 60, 10, arcade.csscolor.BLUE)
arcade.draw_circle_filled(277, 353, 15, arcade.csscolor.BLUE)
arcade.draw_circle_filled(273, 357, 4, arcade.csscolor.RED)
arcade.draw_circle_filled(282, 357, 4, arcade.csscolor.RED)
"""
"""arcade.draw_rectangle_filled(280, 310, 10, 30, arcade.csscolor.BLUE)
arcade.draw_rectangle_filled(295, 285, 10, 30, arcade.csscolor.BLUE)
arcade.draw_rectangle_filled(287, 305, 30, 30, arcade.csscolor.BLUE)
arcade.draw_rectangle_filled(287, 310, 60, 10, arcade.csscolor.BLUE)
arcade.draw_circle_filled(287, 333, 15, arcade.csscolor.BLUE)
arcade.draw_circle_filled(283, 337, 4, arcade.csscolor.RED)
arcade.draw_circle_filled(292, 337, 4, arcade.csscolor.RED)
"""
# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()