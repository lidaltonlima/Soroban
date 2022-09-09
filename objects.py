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
        self.value = value
    
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
                 weight_tb: int, weight_lr: int, weight_div: int, pos_div: float = 0.33) -> None:
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
          self.x = 0
          self.y = 0
    
    def draw(self, x: int, y: int):
          self.x = x
          self.y = y
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


class VerticalLine:
     def __init__(self, screen, color: tuple, width: int, height: int, ) -> None:
          self.screen = screen
          self.color = color
          self.width = width
          self.height = height
          
     def draw(self, x: int, y: int):
          line(self.screen, self.color, (x, y), (x, y + self.height), width=self.width)

class Column:
     def __init__(self, screen, frame, space: int, vl_color: tuple, vl_weight: int) -> None:
         self.screen = screen
         self.frame = frame
         self.height = int(self.frame.height - 2 * self.frame.weight_tb)
         self.space = space
         self.vl_color = vl_color
         self.vl_weight = vl_weight
     
     def draw(self, x):
          vertical_line = VerticalLine(self.screen, self.vl_color, self.vl_weight, self.height)
          vertical_line.draw(x, self.frame.y + self.frame.weight_tb)

    