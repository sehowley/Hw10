##################################################
# Name:
# Collaborators:
# Est Time Spent (hrs):
##################################################

import graphics as g #<- or import this however you like

class Car:
    def __init__(self,window,x,y):
        '''
        Creates a Car object at inital location in a
        particular window.

        Inputs:
            window (GraphWin): Window to draw Car in
            x (integer): Initial horizontal position
            y (integer): Initial vertical position

        Should initially have 5 attributes:
            self.win (GraphWin, from parameters)
            self.x (integer, from parameters)
            self.y (integer, from parameters)
            self.speed (float, value of 0.5)
            self.direction (integer, value of 1)

        Speed will determine how quickly your car moves and
        self.direction will toggle between 1 and -1 to indicate
        the direction your car is moving.

        You should also call the method to create the car at
        the end of this method.
        '''
        pass


    def createCar(self):
        '''
        Creates the component parts of the car *as data attributes*
        and draws the parts initially to the window. A "car" is
        composed of a 200 by 100 rectangle, with two "tires" of
        radius 25 on the bottom (you can adjust the exact location
        of the tires as you see fit to make a nice looking car).
        Fill the car body with your favorite color and make the
        tires black.

        Will create 3 new attributes:
            self.body (Rectangle)
            self.left_tire (Circle)
            self.right_tire (Circle)

        Draws the parts to the screen at the end.
        '''
        pass


    def move(self):
        '''
        Moves all the pieces of the car in the direction given by
        self.direction and by an amount given by self.speed. All
        motion is horizontal, nothing in the vertical direction.
        If the right edge of the car hits the right edge of the canvas,
        the car should reflect back in the opposite direction. And
        similarly for the left edge of the car hitting the left edge
        of the canvas.

        At the end of the function, you should call:

            self.win.after(10, self.move)

        This ensures that the move command will be run again in 10
        milliseconds. Queuing this command in this fashion will
        ensure that your car continues moving even if other movement
        commands might "hold up" the program.
        '''
        pass


def main():
    '''
    Primary function responsible for creating the canvas, initialing
    a single Car, starting it moving and then monitoring any key
    presses to terminate the program when the key 'q' is pressed.

    Should create the window, create the car, and then wait for a
    mouse press. Once the mouse is pressed, the move method of the
    created car should be activated and then a loop should be entered
    to monitor potential key presses. Loop should be broken and the
    window closed when the 'q' key is pressed.
    '''
    pass



# And here we will run main
if __name__ == '__main__':
    main()
