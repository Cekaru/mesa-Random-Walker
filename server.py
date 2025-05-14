import mesa
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.UserParam import Slider
from mesa.visualization.ModularVisualization import ModularServer
from model import GridModel

def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Filled": "true",
        "Color": agent.color,  
        "stroke_color": "black",
        "Layer": 1,
        "r": 0.8
    }
    return portrayal


width = 10
height = 10


grid = CanvasGrid(agent_portrayal, width, height, 500, 500)


model_params = {
    "width": width,
    "height": height,
    "num_agents": Slider("Agent Number", 10, 1, 10, 1)
}


server = ModularServer(
    GridModel,
    [grid],
    "Random Walker Model",
    model_params
)

server.port = 8521

if __name__ == "__main__":
    server.launch()