from mesa import Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation
from agent import RandomWalker
import random

class GridModel(Model):
    def __init__(self, width, height, num_agents):
        super().__init__()
        self.num_agents=num_agents
        self.grid=MultiGrid(width, height, torus=True)
        self.schedule=RandomActivation(self)
        
        


        for i in range(num_agents):
             agent=RandomWalker(i, self)
             self.schedule.add(agent)
             x=self.random.randrange(self.grid.width)
             y=self.random.randrange(self.grid.height)
             self.grid.place_agent(agent,(x, y))

    def step(self):
        self.schedule.step()    




