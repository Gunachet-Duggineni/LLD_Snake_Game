

# The Animator class is used to handle sprite animations in the Pacman game.
# It is called in 
#   Pacman.py: to animate Pac-Man’s movements, like opening and closing his mouth while moving.
#   Ghosts.py: to animate the ghosts, including their movement and effects (like blinking).
#   Sprites.py: to display the animations on the screen and update them as the game runs.



class Animator(object):
    def __init__(self, frames=[], speed=100, loop=True):
        self.frames = frames
        self.current_frame = 0
        self.speed = speed
        self.loop = loop
        self.dt = 0
        self.finished = False

    def reset(self):
        self.current_frame = 0
        self.finished = False

    def update(self, dt):
        if not self.finished:
            self.nextFrame(dt)
        if self.current_frame == len(self.frames):
            if self.loop:
                self.current_frame = 0
            else:
                self.finished = True
                self.current_frame -= 1
   
        return self.frames[self.current_frame]

    def nextFrame(self, dt):
        self.dt += dt
        if self.dt >= (1.0 / self.speed):
            self.current_frame += 1
            self.dt = 0