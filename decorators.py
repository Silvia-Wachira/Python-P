# class AngryBird(self):
#   def  __init__(self):
#     self.x = 0
#     self.y = 0

# def move_up_by(self, delta):
#     self.y += delta 

class AngryBird:
    def __init__(self, x=0, y=0):
        """
        Construct a new AngryBird by setting its position to (0, 0).
        """
        self.x = x
        self.y = y

    def move_up_by(self, delta):
        self.y += delta

b1 = AngryBird()
b2 = AngryBird(x=1)
b3 = AngryBird(y=18)
b4 = AngryBird(10, 10) 