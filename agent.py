import mesa
from mesa import Agent
import random
import colorsys


class RandomWalker(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.color = self.unique_colors()
        

    def unique_colors(self):
        golden_ratio = 0.618033988749895
        hue = (self.unique_id * golden_ratio) % 1.0
        
        
        saturation = 0.5 + (self.unique_id % 3) * 0.2
        value = 0.7 + (self.unique_id % 2) * 0.2
        
        rgb = colorsys.hsv_to_rgb(hue, saturation, value)
        return "#{:02x}{:02x}{:02x}".format(
            int(rgb[0] * 255),
            int(rgb[1] * 255),
            int(rgb[2] * 255)
        )


    
    
    
        
    def step(self):  
        curr_pos = self.pos
        

        
        neighbors = self.model.grid.get_neighborhood(
            curr_pos,
            moore=True,
            include_center=False
        )

        available_neighbors=[
            pos for pos in neighbors
            if self.model.grid.is_cell_empty(pos)
        ]

        


        if available_neighbors:
            new_position = self.random.choice(available_neighbors)
            self.model.grid.move_agent(self, new_position)
