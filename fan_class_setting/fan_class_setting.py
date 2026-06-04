class Fan:
    slow = 1
    medium = 2
    fast = 3

    def __init__(self, speed=slow, radius=5, color="blue", on=False):
        self.speed = speed
        self.radius = radius
        self.color = color
        self.on = on