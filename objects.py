from pygame.draw import polygon

class Count:
    def __init__(self, screen, color_top: tuple, color_button: tuple,
                 width: int, height: int, top_button: int) -> None:
        self.screen = screen
        self.color_top = color_top
        self.color_button = color_button
        self.width = width
        self.height = height
        self.top_button = top_button
    
    def draw(self, x, y):
        polygon(self.screen, self.color_top, [(x - self.width / 2, y),
                                              (x - self.top_button / 2, y - self.height / 2),
                                              (x + self.top_button / 2, y - self.height / 2),
                                              (x + self.width / 2, y)])
        polygon(self.screen, self.color_button, [(x - self.width / 2, y),
                                                 (x - self.top_button / 2, y + self.height / 2),
                                                 (x + self.top_button / 2, y + self.height / 2),
                                                 (x + self.width / 2, y)])
        
