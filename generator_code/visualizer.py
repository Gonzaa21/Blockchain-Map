import time
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import json

# configuration
with open('config.json','r') as file:
    config = json.load(file)

# visualize function
def visualizer_map(map):
    plt.imshow(map, cmap="terrain") # set "terrain" color
    plt.colorbar() # show color scale
    plt.title("Procedural Map - Natural Terrain") # set title
    plt.show() # show map
    
def save_map(map, filename, colormap="terrain"):
    # save maps in different file
    timestamp = time.strftime("%Y%m%d_%H%M%S")  # Generate unique label based on date
    filename = f"maps/png/map_{timestamp}.png"
    
    # save map in rgb scale
    cmap = plt.get_cmap(colormap)
    color = cmap(map)[:, :, :3]
    rgb = (color * 255).astype(np.uint8)

    img = Image.fromarray(rgb)
    img.save(filename)
    
if __name__ == "__main__":
    visualizer_map(map)
    save_map(map, config["output"]) # save map