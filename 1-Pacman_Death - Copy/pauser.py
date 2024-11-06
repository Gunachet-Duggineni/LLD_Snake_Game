# This file controls the pause feature in the game, allowing players to take a break.
# pauser.py is used for:
#   Pausing and unpausing the game when needed.
#   Stopping all characters and timers without affecting the game state.
#   Providing a smooth pause experience so players can resume right where they left off.

# pauser.py is used in:
#   pacman.py and ghosts.py: to temporarily stop movements when the game is paused.
#   modes.py: to freeze the current game mode until the game resumes.

# In short: pauser.py lets players take a break whenever they need, without disrupting the game!


class Pause(object):
    def __init__(self, paused=False):
        self.paused = paused
        self.timer = 0
        self.pauseTime = None
        self.func = None
        
    def update(self, dt):
        if self.pauseTime is not None:
            self.timer += dt
            if self.timer >= self.pauseTime:
                self.timer = 0
                self.paused = False
                self.pauseTime = None
                return self.func
        return None

    def setPause(self, playerPaused=False, pauseTime=None, func=None):
        self.timer = 0
        self.func = func
        self.pauseTime = pauseTime
        self.flip()

    def flip(self):
        self.paused = not self.paused