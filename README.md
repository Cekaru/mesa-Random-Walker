# Mesa Random Walker

This is a simple agent-based simulation built with Python and Mesa.  
Agents move randomly on a 10x10 grid. Each agent has a unique color and only moves to empty neighboring cells.

## Requirements

- Python 3.7 or higher
- Mesa 1.2.1

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python server.py
```

Then open your browser and go to:

```
http://127.0.0.1:8521
```

## Files

- `agent.py`: Defines how the agents move and pick colors
- `model.py`: Creates the grid and the agents
- `server.py`: Starts the web-based visualization



