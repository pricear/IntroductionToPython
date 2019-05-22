"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Alexis Price.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################

import rosegraphics as rg

window = rg.TurtleWindow()
alexis = rg.SimpleTurtle('turtle')
alexis.pen = rg.Pen('red', 5)
alexis.speed = 30
size = 300

for k in range(13):

    alexis.draw_square(30)

    alexis.pen_up()
    alexis.left(12)
    alexis.forward(4)

    alexis.pen_down()
    size = size

    alexis.pen_up()
    alexis.left(12)
    alexis.forward(4)

    alexis.pen_down()
    size = size


    alexis.pen_up()
    alexis.left(12)
    alexis.forward(4)

    alexis.pen_down()
    size = size


    alexis.pen_up()
    alexis.left(12)
    alexis.forward(4)

    alexis.pen_down()
    size = size


    alexis.pen_up()
    alexis.left(12)
    alexis.forward(4)

    alexis.pen_down()
    size = size



    alexis.pen_up()
    alexis.left(24)
    alexis.forward(10)

    alexis.pen_down()
    size = size


    alexis.pen_up()
    alexis.left(24)
    alexis.forward(10)

    alexis.pen_down()
    size = size



    alexis.pen_up()
    alexis.left(24)
    alexis.forward(10)

    alexis.pen_down()
    size = size



    alexis.pen_up()
    alexis.left(24)
    alexis.forward(10)

    alexis.pen_down()
    size = size


    alexis.pen_up()
    alexis.left(30)
    alexis.forward(15)

    alexis.pen_down()
    size = size


    alexis.pen_up()
    alexis.left(30)
    alexis.forward(15)

    alexis.pen_down()
    size = size

    alexis.pen_up()
    alexis.left(30)
    alexis.forward(15)

    alexis.pen_down()
    size = size

window = rg.TurtleWindow()
lucas = rg.SimpleTurtle('turtle')
lucas.pen = rg.Pen('purple', 5)
lucas.speed = 30
size = 500

for k in range(13):

    lucas.draw_square(90)

    lucas.pen_up()
    lucas.left(12)
    lucas.forward(4)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(12)
    lucas.forward(4)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(12)
    lucas.forward(4)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(24)
    lucas.forward(10)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(24)
    lucas.forward(10)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(24)
    lucas.forward(10)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(24)
    lucas.forward(10)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(24)
    lucas.forward(10)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(24)
    lucas.forward(10)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(30)
    lucas.forward(15)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(30)
    lucas.forward(15)

    lucas.pen_down()
    size = size

    lucas.pen_up()
    lucas.left(30)
    lucas.forward(15)

    lucas.pen_down()
    size = size
window.close_on_mouse_click()