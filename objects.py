from pygame.draw import polygon, line

class Count:
    def __init__(self, screen, color_top: tuple, color_button: tuple,
                 width: int, height: int, top_button: int, value: int = 1) -> None:
        self.screen = screen
        self.color_top = color_top
        self.color_button = color_button
        self.width = width
        self.height = height
        self.top_button = top_button
    
    def draw(self, x: int, y: int):
        polygon(self.screen, self.color_top, [(x - self.width / 2, y),
                                              (x - self.top_button / 2, y - self.height / 2),
                                              (x + self.top_button / 2, y - self.height / 2),
                                              (x + self.width / 2, y)])
        polygon(self.screen, self.color_button, [(x - self.width / 2, y),
                                                 (x - self.top_button / 2, y + self.height / 2),
                                                 (x + self.top_button / 2, y + self.height / 2),
                                                 (x + self.width / 2, y)])


class Frame:
    def __init__(self, screen, color_tb: tuple, color_lr: tuple, color_div: tuple, width: int, heigh: int,
                 weight_tb: int, weight_lr: int, weight_div: int, pos_div: float = 0.4) -> None:
        self.screen = screen
        self.color_tb = color_tb
        self.color_lr = color_lr
        self.color_div = color_div
        self.width = width
        self.height = heigh
        self.weight_tb = weight_tb
        self.weight_lr = weight_lr
        self.weight_div = weight_div
        self.pos_div = pos_div
    
    def draw(self, x: int, y: int):
        # right line
        line(self.screen, self.color_lr, (x + self.weight_lr / 2, y),
             (x + self.weight_lr / 2, y + self.height), width=self.weight_lr)
        # Left line
        line(self.screen, self.color_lr, (x + self.width - self.weight_lr / 2, y),
             (x + self.width - self.weight_lr / 2, y + self.height), width=self.weight_lr)
        # Top line
        line(self.screen, self.color_tb, (x, y + self.weight_tb / 2 - 1),
             (x + self.width, y + self.weight_tb / 2 - 1), width=self.weight_tb)
        # Button line
        line(self.screen, self.color_tb, (x, y + self.height - self.weight_tb / 2),
             (x + self.width, y + self.height - self.weight_tb / 2), width=self.weight_tb)
        # Middle line
        line(self.screen, self.color_div, (x + self.weight_lr,self.height * self.pos_div),
             (x + self.width - self.weight_lr - 1, self.height * self.pos_div), width=self.weight_div)
